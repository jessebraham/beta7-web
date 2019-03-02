# beta7.io

Generates the content hosted at [beta7.io](https://beta7.io) using [Pelican](https://blog.getpelican.com), a static site generator written in [Python](https://python.org).


# Usage

The CSS for the theme must be built prior to building and publishing the site.

```bash
$ cd theme
$ npm i
$ npm run {build|dist}
$ cd ..
```

Next, the site can be built and deployed using `make`:

```bash
$ pip install -r requirements.txt
$ make ssh_upload
```

## To Do

- Add favicon
- Write proper meta description
