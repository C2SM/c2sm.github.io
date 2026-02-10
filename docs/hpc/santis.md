# Santis

The vCluster `santis` is dedicated to **Climate and Weather** applications. It includes the following:

- [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"}: Project for ICON-based km-scale climate simulations
- Projects by C2SM community members
- User lab projects in climate and weather domains

## User Environments (uenvs)

| uenv                   | Description                    |
|------------------------|--------------------------------|
| `icon/25.2:v3`         | Build and run ICON             |
| `climtools/25.2:v1`    | Pre- and post-processing tools |

You can find the most important commands when working with uenvs on the [CSCS Docs pages :material-open-in-new:](https://docs.cscs.ch/software/uenv/#downloading-uenv){:target="_blank"}.

### climtools

The climtools uenv provides a set of CLI tools and GUI tools frequently used in climate and weather workflows,
including `cdo`, `ncview`, `ncdump` and others. For more information consider the [corresponding Spack spec](https://github.com/C2SM/software-stack-recipes/blob/main/recipes/climtools/25.2/gh200/environments.yaml).

It is recommended that the `climtools` uenv is loaded with the `--view=climtools` argument to instantly
access all of the tools that are shipped with this uenv:

```bash
uenv start climtools/25.2:v1 --view=climtools
```

The software is now available, e.g.:

```bash
which cdo
# /user-environment/env/netcdf/bin/cdo
```

### Pre-release uenvs

User environments that are not (yet) part of the official CSCS uenv 
registry can be found in the following folder:

```
/capstor/store/cscs/userlab/cwd01/leclairm/uenvs/images
```

| uenv                   | Description                    |
|------------------------|--------------------------------|
| `/capstor/store/cscs/userlab/cwd01/leclairm/uenvs/images/sirocco_25.9.sqfs` | Sirocco |


## SLURM Partitions

| SLURM partition | Default wall time | Max. wall time | Limitations |
|-----------------|-------------------|----------------|-------------|
| normal          | 01:00:00          | 24:00:00       | -           |
| debug           | 00:30:00          | 00:30:00       | Single node |  
| xfer            | 06:00:00          | 24:00:00       | Single node |
