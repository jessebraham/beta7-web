PY          ?= python3
PELICAN     ?= pelican
PELICANOPTS =

BASEDIR     = $(CURDIR)
INPUTDIR    = $(BASEDIR)/content
EXTRADIR    = $(BASEDIR)/extra
OUTPUTDIR   = $(BASEDIR)/output
CONFFILE    = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py

SSH_HOST       = localhost
SSH_PORT       = 22
SSH_USER       = root
SSH_TARGET_DIR = /var/www


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '


theme:
	cd "$(BASEDIR)"/beta7-theme && make all

html: theme
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)
	if test -d "$(EXTRADIR)"; then cp "$(EXTRADIR)"/* "$(OUTPUTDIR)/"; fi

regenerate:
	$(PELICAN) -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" "$(PELICANOPTS)"

publish:
	$(PELICAN) "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s $(PUBLISHCONF) $(PELICANOPTS)
	if test -d "$(EXTRADIR)"; then cp "$(EXTRADIR)"/* "$(OUTPUTDIR)/"; fi


clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"
	cd "$(BASEDIR)"/beta7-theme && make clean


serve:
ifdef PORT
	cd "$(OUTPUTDIR)" && $(PY) -m pelican.server $(PORT)
else
	cd "$(OUTPUTDIR)" && $(PY) -m pelican.server
endif

serve-global:
ifdef SERVER
	cd "$(OUTPUTDIR)" && $(PY) -m pelican.server 8000 $(SERVER)
else
	cd "$(OUTPUTDIR)" && $(PY) -m pelican.server 8000 0.0.0.0
endif


ssh_upload: publish
	scp -P $(SSH_PORT) -r "$(OUTPUTDIR)/*" $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete "$(OUTPUTDIR)/" $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude


.PHONY: help html regenerate publish clean serve serve-global ssh_upload rsync_upload
