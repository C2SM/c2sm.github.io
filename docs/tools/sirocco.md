# Sirocco

Sirocco is a Python workflow tool for climate and weather applications running on HPC systems.
Workflows are described in a YAML dialect inspired by [Cylc :material-open-in-new:](https://cylc.github.io/){:target="_blank"}
and [AiiDA :material-open-in-new:](https://www.aiida.net/){:target="_blank"}, and unrolled into a graph of tasks and data.

For any questions, please contact [Matthieu Leclair :material-open-in-new:](https://c2sm.ethz.ch/the-center/people/person-detail.html?persid=221860){:target="_blank"}.

## Features

- Tasks explicitly declare the data they consume and produce, making workflows composable
- Cycles with their own periodicity for climate and weather workflows
- Parameterized tasks and data for ensemble and sensitivity experiments
- Tasks submitted ahead of time and chained by scheduler dependencies
- A general-purpose `shell` plugin and a dedicated plugin for the ICON model, including coupled runs on hybrid CPU/GPU
  architectures
- A standalone engine running autonomously on the HPC system and an AiiDA-based engine (under development)

## Usage on Säntis

Sirocco is readily available on Säntis as a uenv. Pull the image and start it:

```shell
uenv image pull sirocco/v0.1.0:v1
uenv start sirocco/v0.1.0:v1
```

Loading the uenv activates the default view `app` in which the `sirocco` command is available.

Further releases will follow the same naming convention, the `:v1` tag beeing required for a uenv. List availalble uenvs
with

```shell
uenv image find sirocco
```

## Code and Documentation

- [Sirocco repo :material-open-in-new:](https://github.com/C2SM/Sirocco){:target="_blank"}
- [Documentation :material-open-in-new:](https://sirocco.ethz.ch){:target="_blank"}
- [Getting started :material-open-in-new:](https://sirocco.ethz.ch/usage/standalone/){:target="_blank"}
