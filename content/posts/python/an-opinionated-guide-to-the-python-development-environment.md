Title:   An Opinionated Guide to the Python Development Environment
Date:    2018-02-24
Summary: Creating the ultimate Python development environment and workflow, starring [Pyenv](https://github.com/pyenv/pyenv) and [Pipenv](https://github.com/pypa/pipenv).


I've been writing [Python](https://www.python.org/) for about a decade now, and I can't say I've ever been truly content with my development environment until recently. I've always found the workflow to be clunky, overcomplicated and require a large number of tools just to work in a sane manner.  

Thanks to the recent introduction of [Pipenv](https://github.com/pypa/pipenv), in conjunction with some old friends, the process has been greatly simplified. The community now has an official tool for managing Python environments and packages, and I have refined my development environment to a small number of enormously powerful tools.


# Table of Contents

* [Requirements](#requirements)
* [Verify Dependencies](#verify-dependencies)
* [Install Pyenv, Pipenv and Flake8](#install-pyenv-pipenv-and-flake8)
* [Install Additional Tools](#optional-install-additional-tools)
* [Wrapping Up](#wrapping-up)


# Requirements

I've been trying to build the ideal development environment on and off for years, iterating between various tools and workflows, but was never really happy with the results. Heading into my most recent overhaul, I wanted to have clear goals in mind. I had only a few simple requirements:  

1. I should be required to manually interact with and configure as few tools as possible.   
2. I should be able to quickly and easily choose a Python version (Python 2, Python 3, [anaconda](https://www.anaconda.com/), [Jython](http://www.jython.org/), [PyPy](http://pypy.org/), etc.).  
3. Package management needs to be isolated and simple. I don't even want to think about keeping track of packages, and I definitely don't want them polluting my system's global namespace.  
4. My tools should **never** get in my way or slow me down. Few things piss me off more than tools that try to be too "helpful".  
5. All tools should be open source, and have good (or great!) documentation.  

After months research and experimentation, I settled on the following tools:  

* [Pyenv](https://github.com/pyenv/pyenv) - "Simple Python version management"   
* [Pipenv](https://github.com/pypa/pipenv) - "Python Development Workflow for Humans"  
* [Flake8](https://gitlab.com/pycqa/flake8) - "... a python tool that glues together pep8, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code"  

I consider these essential to the development workflow at this point. I find [Pylint](https://www.pylint.org/) to be a bit on the aggressive side; it almost works a bit *too* well. For this reason, I use Flake8 in its place.  

In addition, I use the following tools, however these mostly come down to preference:  

* [Visual Studio Code](https://code.visualstudio.com/) - "Code editing. Redefined."    
* [Microsoft Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - "... rich support for the Python language (including Python 3.6), including features such as linting, debugging, IntelliSense, code navigation, code formatting, refactoring, unit tests, snippets, and more!"  
* [Pytest](https://docs.pytest.org/en/latest/) - "... makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries."  
* [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/) - "Coverage plugin for pytest."  


# Verify Dependencies

Before we get started, it's vital that we have Python installed on our system (I know, go figure). In addition, we'll also require [Pip](https://pip.pypa.io/en/stable/), the [PyPA](https://pypa.io/) recommended tool for installing Python packages. To verify both are installed and available on our *PATH*, run the following commands in a terminal:  

```
$ python --version
Python 2.7.12  
$ python3 --version
Python 3.5.2
$ pip --version
pip 9.0.1 from /usr/local/lib/python3.5/dist-packages (python 3.5)
```

*(Note that your output may vary depending on which Python and Pip versions you have installed, and your operating system.)*

Python should come pre-installed on macOS, as well as on most Linux distributions (I am running Xubuntu 16.04.3, for example). If Python is *not* installed on your system, you can find operating system-specific installation guides in the Python documentation's [beginner's guide](https://wiki.python.org/moin/BeginnersGuide/Download). At this point in time, there is really no reason to still be using Python 2, so do everybody a favor and use Python 3. You also get all sorts of cool new language features in return!  

Pip is not always included with your operating system. If Pip is not installed, again you can find operating system-specific installation guides [in the documentation](https://pip.pypa.io/en/stable/installing/). In Ubuntu and derivatives it's as simple as:  

```
$ # For Python 3 (recommended)  
$ sudo apt install python3-pip  
$ # For Python 2  
$ sudo apt install python-pip  
```


# Install Pyenv, Pipenv and Flake8

## Pyenv

Pyenv is a fantastic little script that allows us to download and install a variety of Python versions with ease. A handful of installation methods are described in the [github repository](https://github.com/pyenv/pyenv), but I recommend using the **Basic GitHub Checkout** method, as per their Readme. The main benefit of this approach is being able to easily upgrade Pyenv by running `git checkout origin master` from within the `~/.pyenv` directory.  

```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Once the repository is checked out, edit your `.bashrc` file (or `.zshrc` if you are using ZSH, for example), and add the following lines, changing the path if required, to configure Pyenv. Lastly, enable shims and autocompletion. For more information on this, refer to the [How It Works](https://github.com/pyenv/pyenv#how-it-works) section of the Readme.  

```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc  
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc  
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc  
$ # Reload your shell's configuration  
$ source ~/.bashrc  
```

Below are some quick examples of using Pyenv:

```
$ # List every version of Python available
$ pyenv install --list
$ # Install new versions of Python
$ pyenv install 3.6.2  
$ pyenv install pypy3.5-5.10.1  
$ # If you would like, you can set a global Python version
$ pyenv global 3.6.2
```

If you installed Pyenv in the default location, the installed Python binaries can be found in `~/.pyenv/shims/`.


## Pipenv

Installing Pipenv is even easier. You can also (*optionally*) enable shell completion (a really nifty feature, more information in the [Readme](https://github.com/pypa/pipenv#shell-completion)):  

```
$ sudo pip install --user pipenv  
$ echo 'eval "$(pipenv --completion)"' >> ~/.bashrc  
$ # Reload your shell's configuration  
$ source ~/.bashrc  
```

With Pipenv installed and configured, it's time to test it out. We will create a small sample project, activate the virtual environment, and install a package in order to verify Pipenv is functioning properly.  

```
$ mkdir -p pipenv_test/ && cd $_  
$ # Use whichever version of Python you have available
$ pipenv --three --python 3.6.2
$ ls -al
total 12
drwxrwxr-x  2 jesse jesse 4096 Feb 24 08:21 .
drwxr-xr-x 77 jesse jesse 4096 Feb 24 08:22 ..
-rw-rw-r--  1 jesse jesse  152 Feb 24 08:22 Pipfile
```

If all goes well, you should now have a **Pipfile** in the project's directory. Examining its contents shows some default configuration and scaffolding, as well as our specified version of Python.

```
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"


[packages]



[requires]

python_version = "3.6"


[dev-packages]
```

It should be noted at this point that this file generally should *not* be editted manually, as it gets updated by Pipenv. Once packages have been installed, an additional **Pipfile.lock** file is created as well; this should not be editted either.  

To make use of Pipenv, we need to activate the virtual environment that was ever so kindly created for us by running `pipenv shell`:

```zsh
$ python --version  
2.7.12  
$ pipenv shell  
(pipenv_test-omjIZu3A) $ python --version  
3.6.2  
$ # Make sure you use pipenv, not pip!
(pipenv_test-omjIZu3A) $ pipenv install flask
```

Now that we have a package installed, our Pipfile has been updated accordingly:

```
[packages]

flask = "*"
```

To deactivate the virtual environment, just `exit`, or close your terminal.


## Flake8

While not ideal, I've found the simplest approach to get Flake8 working with Visual Studio Code (see below) is to just install it globally. This is the last "unsolved" piece of the puzzle, but it's a small enough issue that I'm willing to overlook it for now.  

```
$ # Explicitly choose to use Python 3's version of Pip just to be safe.
$ sudo pip3 install --user flake8  
$ flake8 --version  
3.5.0 (mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.6.0) CPython 3.5.2 on Linux  
```


# Install Additional Tools

This section is incredibly opinionated, and can be skipped entirely if you already have a go-to editor or unit-testing framework.  


## Visual Studio Code with Python Plugin

Text editors, for whatever reason, are a touchy subject. I'm not looking to start any flame wars here, so I'm going to keep this brief and to the point. If you have any opinions on text editors, you can probably ignore this section altogether.  

I mostly use [Visual Studio Code](https://code.visualstudio.com/), and sometimes (usually only when required) I'll use [Vim](http://www.vim.org/). I generally avoid Microsoft software like the plague, but I have to give them props on this one. After trying [Sublime Text]() and [Atom]() I was deeply dissatisfied with both (not to say there's anything wrong with either project, they just didn't work out) and I decided to give VS Code a shot; I'm glad I did. You can download **DEB**s or **RPM**s from the [VS Code website](https://code.visualstudio.com/), but I chose to use the [Visual Studio Code PPA](https://github.com/tagplus5/vscode-ppa) instead.  

```
$ curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg  
$ sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
$ sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'  
$ sudo apt update && sudo apt install code
```

Once VS Code is installed, launch a new window, and press `Ctrl + Shift + X` to view the *Extensions* panel. I use the official [Microsoft Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), and have had an overall pleasant experience with it. This extension provides support for linting, debugging, IntelliSense, code formatting, unit tests and much more. I would definitely recommend installing it.  

Next, navigate to `File > Preferences > Settings`, or alternatively just press `Ctrl + ,`. I've added the following lines to my `settings.json` file:  

```json
"python.pythonPath": "/home/jesse/.pyenv/shims/python3",
"python.linting.enabled": true,
"python.linting.pylintEnabled": false,
"python.linting.flake8Enabled": true,
"python.linting.flake8Path": "/usr/local/bin/flake8"
```

This sets the path of the Python binary to use, in this case whichever version of Python 3 that we have installed via Pyenv. It also enables linting, and configures VS Code to use Flake8 rather than Pylint.


## Pytest and Pytest-Cov

I like using Pytest and Pytest-Cov for unit testing and coverage on my projects. To install these, from within an activated virtual environment, run:  

```
(pipenv_test-omjIZu3A) $ pipenv install pytest pytest-cov
```

These two tools are too complex to discuss here, and frankly deserve their own posts. For more information, check out the [Pytest](https://docs.pytest.org/en/latest/) and [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/) documentation.


# Wrapping Up

Thanks to the above tools, starting a new project has been simplified down to a few commands:  

```
$ mkdir -p project && cd $_  
$ pipenv --three --python 3.6.2  
$ pipenv shell  
(project-Mge6DASd) $ pipenv install flake8 pytest pytest-cov  
```

This approach requires me to use a total of two tools manually, Pyenv and Pipenv, and accommodates all of my requirements. I don't find myself getting frustrated with over-aggressive IntelliSense, everything coexists without friction, and it takes very little work to spin up a fresh new environment. Flake8 keeps me writing clean, pythonic code, and Pytest along with Pytest-Cov help make testing softare incredibly straight forward.  

I believe these tools have made Python much more acessible for beginners, and made the experience much more pleasant for experienced developers. It's important to have standard tools within a community, and Pipenv was a huge step forward for us in that regard.
