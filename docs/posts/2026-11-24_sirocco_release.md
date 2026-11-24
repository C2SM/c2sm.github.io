---
date:
  created: 2026-11-24
categories:
  - Sirocco
  - Alps
---

# New workflow tool Sirocco v0.1.0 released

The first release of [Sirocco](../tools/sirocco.md), a Python workflow tool for climate and weather applications on HPC
systems, is now available and part of the C2SM tools.

<!-- more -->

## What it does

Sirocco describes workflows in a YAML dialect inspired by
[Cylc :material-open-in-new:](https://cylc.github.io/){:target="_blank"} and
[AiiDA :material-open-in-new:](https://www.aiida.net/){:target="_blank"}. Tasks explicitly declare the data they consume
and produce, cycles can have their own periodicity, and tasks and data can be parameterized for ensemble and sensitivity
experiments. Besides a general purpose `shell` plugin, a dedicated ICON plugin supports coupled runs on hybrid CPU/GPU
architectures.

## Getting started on Säntis

Sirocco is available on Säntis as a uenv:

```bash
uenv image pull sirocco/v0.1.0
uenv start sirocco/v0.1.0
```

## Related links

- [Sirocco page](../tools/sirocco.md)
- [Documentation :material-open-in-new:](https://sirocco.ethz.ch){:target="_blank"}
- [Repository at C2SM :material-open-in-new:](https://github.com/C2SM/Sirocco){:target="_blank"}
- [Release notes v0.1.0 :material-open-in-new:](https://github.com/C2SM/Sirocco/releases/tag/v0.1.0){:target="_blank"}
