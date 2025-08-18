# C2SM User Landing Page

## MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Material for MkDocs

For full documentation visit https://squidfunk.github.io/mkdocs-material/.

### Quick Start

> [!IMPORTANT]
> to run the serve script, you need to first install [uv](https://docs.astral.sh/uv/getting-started/installation/).

To quickly generate a view of the documenation

Clone this repository on your PC/laptop, then view the documentation in a browser run `./serve`:

```console
$ git clone git@github.com:${githubusername}/c2sm.github.io.git
$ cd c2sm.github.io
./serve
...
INFO    -  [08:33:34] Serving on http://127.0.0.1:8000/
```

This generates the documentation locally, which can be viewed using a local link, typically [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The documentation will be rebuilt and the webpage reloaded when changed files are saved.

To build the docs in a `site` sub-directory:
```bash
./serve build
```

### Using MkDocs Manually

First install MkDocs

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The following commands are available:

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server (open second terminal to make changes).
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
