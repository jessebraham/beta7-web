# beta7-web

Configuration and plugins for [Pelican](https://blog.getpelican.com/), a static site generator written in [Python](https://python.org/). Used for generating the site found at [beta7.io](https://beta7.io). Uses [beta7-theme](https://github.com/jessebraham/beta7-theme).  


### Plugins

This site requires a number of third-party packages for all plugins and features to work as intended. Below are a list of notable packages; the full list can be found in `requirements.txt`.    

| Package        | Description                                                            |  
|:---------------|:-----------------------------------------------------------------------|  
| markdown-extra | Provides some nice enhancements to the default Markdown specification  |  
| webassets      | Provides a pipeline for static assets, with many plugins               |  
| pyscss         | Compiles SCSS syntax to CSS                                            |  
| cssmin         | Minifies CSS files                                                     |  
| pendulum       | Provides helpful date utilities for use with the readable_dates plugin |  


This site uses a number of plugins from the [pelican-plugins](https://github.com/getpelican/pelican-plugins) repository, which is included as a submodule for convenience. The full list of used plugins can be found by checking the `PLUGINS` configuration variable found in `pelicanconf.py`.    


### To Do:

* [ ] Add a favicon  
