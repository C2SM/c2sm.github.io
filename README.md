# C2SM User Landing Page

## MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Material for MkDocs

For full documentation visit <https://squidfunk.github.io/mkdocs-material/>.

### Quick Start

> [!TIP]
> You can also preview any open pull request at
> [https://c2sm.github.io/pr-preview/pr-&lt;pr-id&gt;/](https://c2sm.github.io/pr-preview/pr-<pr-id>/)

To quickly generate a view of the documentation clone this repository on your PC/laptop, then view the documentation in
a browser run `./serve`:
> [!IMPORTANT]
> To run the serve script, you need to first install [uv](https://docs.astral.sh/uv/getting-started/installation/).

```console
$ git clone git@github.com:${githubusername}/c2sm.github.io.git
$ cd c2sm.github.io
./serve
...
INFO    -  [08:33:34] Serving on http://127.0.0.1:8000/
```

This generates the documentation locally, which can be viewed using a local link, typically
[http://127.0.0.1:8000/](http://127.0.0.1:8000/). The documentation will be rebuilt and the webpage reloaded when
changed files are saved.

To build the docs in a `site` sub-directory:

```bash
./serve build
```

### Using MkDocs Manually

First install MkDocs

```console
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

## Markdown linting

All Markdown files are checked with
[markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) on every push and pull request.
The rules are configured in `.markdownlint.yaml` and adapted to Material for MkDocs
(4-space list indentation, admonitions, inline HTML elements, 120-character lines).

External links in `docs/` must carry an icon and open in a new tab. `scripts/format_external_links.py` adds both,
and a GitHub workflow fails if a link is not formatted.

To format links and fix most lint issues automatically before each commit, install the
[pre-commit](https://pre-commit.com) hooks once:

```console
pip install pre-commit
pre-commit install
```

To check and fix all files manually, run:

```console
pre-commit run --all-files
```

Line length (MD013) cannot be fixed automatically; wrap long prose lines by hand.
