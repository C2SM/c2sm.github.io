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
The `SUMMARY.md` navigation files are excluded in `.markdownlint-cli2.yaml`.

External links in `docs/` must carry an icon and open in a new tab. `scripts/format_external_links.py` adds both,
and a GitHub workflow fails if a link is not formatted.

### Setup

Install the [pre-commit](https://pre-commit.com) hooks once after cloning. Node.js is not required, since pre-commit
installs it automatically on the first run:

```console
pip install pre-commit
pre-commit install
```

From then on, every `git commit` formats external links and fixes most lint issues in the staged files. If a hook
changes a file, the commit is aborted: review the changes, stage them with `git add`, and commit again. Errors that
cannot be fixed automatically are listed with file, line, and rule (e.g., `docs/index.md:12 MD013/line-length`).

### Checking all files

To check and fix all files at once, for example after a failed CI check, run:

```console
pre-commit run --all-files
```

To skip the hooks for a single commit, use `git commit --no-verify`. The CI checks still apply.

### Editor integration

The [markdownlint extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
for VS Code reads `.markdownlint.yaml` and shows errors while typing.

### Common pitfalls

* Line length (MD013) cannot be fixed automatically; wrap long prose lines by hand. Lines in code blocks and tables are
  exempt.
* Do not start a wrapped line with `-`, `*`, `+`, or `1.`, as it would become a new list item.
* Indent content that belongs to a list item (paragraphs, code blocks) by 4 spaces. Otherwise, the list is split and
  its numbering restarts.
* Use headings instead of bold text on a line of its own (MD036).
* To disable a rule for a single line, add `<!-- markdownlint-disable-next-line MD013 -->` above it. Use this
  sparingly.
