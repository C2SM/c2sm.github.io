# Santis

The vCluster `santis` is dedicated to **Climate and Weather** applications. It includes the following:

- [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"}: Project for ICON-based km-scale climate simulations
- Projects by C2SM community members
- User lab projects in climate and weather domains

## User Environments (uenvs)

| uenv                   | Description                    |
|------------------------|--------------------------------|
| `icon/25.2:v3`         | Build and run ICON             |
| `netcdf-tools/2025:v1` | Pre- and post-processing tools |

You can find the most important commands when working with uenvs on the [CSCS Docs pages :material-open-in-new:](https://docs.cscs.ch/software/uenv/#downloading-uenv){:target="_blank"}.

### netcdf-tools

The netcdf-tools uenv provides a set of CLI tools and GUI tools frequently used in climate and weather workflows,
including `cdo`, `ncview`, `ncdump` and others.

It is recommended that the `netcdf-tools` uenv should be loaded with the `--view=netcdf` argument to instantly
access all of the tools that are shipped with this uenv:

```bash
uenv start --view=netcdf netcdf-tools/2025:v1
```

The software is now available, e.g.:

```bash
which cdo
/user-environment/env/netcdf/bin/cdo
```

More information about the `netcdf-tools` uenv can be found at the [CSCS Docs page :material-open-in-new:](https://docs.cscs.ch/software/cw/netcdf-tools/){:target="_blank"}.

### Pre-release uenvs

User environments that are not (yet) part of the official CSCS uenv 
registry can be found in the following folder:

```
/capstor/store/cscs/userlab/cwd01/leclairm/uenvs/images
```

| uenv                   | Description                    |
|------------------------|--------------------------------|
| `/capstor/store/cscs/userlab/cwd01/leclairm/uenvs/images/climtools_25.2.sqfs`         | Like `netcdf-tools` but with additional software such as `git-lfs` and `eccodes`             |
| `/capstor/store/cscs/userlab/cwd01/leclairm/uenvs/images/climtools_25.2_v2.sqfs`         | Like `netcdf-tools` but with additional software such as `git-lfs`, `eccodes` and `icontools`             |
| `/capstor/store/cscs/userlab/cwd01/leclairm/uenvs/images/sirocco_25.9.sqfs` | Sirocco |


Note that the `climtools` uenvs should also be loaded with
the `--view=modules` argument. 


## SLURM Partitions

| SLURM partition | Default wall time | Max. wall time | Limitations |
|-----------------|-------------------|----------------|-------------|
| normal          | 01:00:00          | 24:00:00       | -           |
| debug           | 00:30:00          | 00:30:00       | Single node |  
| xfer            | 06:00:00          | 24:00:00       | Single node |
