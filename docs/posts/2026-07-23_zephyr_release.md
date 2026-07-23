---
date:
  created: 2026-07-23
categories:
  - Zephyr
---

# Zephyr: Multi-variable requests and new documentation

[Zephyr](../tools/zephyr.md), C2SM's climate data extraction tool, now supports requesting multiple variables (or other fields) in a single request, and comes with a brand-new documentation site.

<!-- more -->

### Multi-variable requests

Any field in a Zephyr request — `variable`, `ensemble_member`, and others — can now hold a list of values instead of a single one, e.g. `"variable": ["tas", "pr"]`. Zephyr builds the Cartesian product across all list-valued fields and processes every matching file, so you no longer need to submit one request per variable.

### New documentation

Zephyr's documentation has moved out of the repository's README into a full documentation site, covering installation, running extractions locally on IAC machines, using the web interface, the request JSON format, supported datasets, architecture, and how the four repositories in the [Zephyr ecosystem :material-open-in-new:](https://c2sm.github.io/zephyr/docs/ecosystem.html){:target="_blank"} fit together.

### Related links

- [Repository at C2SM :material-open-in-new:](https://github.com/C2SM/zephyr){:target="_blank"}
- [Release notes v1.3 :material-open-in-new:](https://github.com/C2SM/zephyr/releases/tag/v1.3){:target="_blank"}
- [Release notes v1.4 :material-open-in-new:](https://github.com/C2SM/zephyr/releases/tag/v1.4){:target="_blank"}
- [Zephyr Documentation :material-open-in-new:](https://c2sm.github.io/zephyr/docs/){:target="_blank"}
