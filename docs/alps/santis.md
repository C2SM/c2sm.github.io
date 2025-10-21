# Santis

The vCluster `santis` is dedicated to **Climate and Weather** applications. It includes the following:

- [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"}: Project for ICON-based km-scale climate simulations
- Projects by C2SM community members
- User lab projects in climate and weather domains

## User Environments (uenvs)

| uenv                   | Description                    |
|------------------------|--------------------------------|
| `icon/25.2:v3`         | Build and run ICON             |
| `netcdf-tools/2024:v1` | Pre- and post-processing tools |

You can find the most important commands when working with uenvs on the [CSCS Docs pages :material-open-in-new:](https://docs.cscs.ch/software/uenv/#downloading-uenv){:target="_blank"}.

The `netcdf-tools` uenv should be loaded with the `--view=modules` argument to get access to the `module load` command:

```
uenv start --view=modules netcdf-tools/2024:v1
module avail
```

This will show the list of available modules:

```
cdo/2.4.0            hdf5/1.14.3     netcdf-c/4.9.2          python/3.12.1
cray-mpich/8.1.30    nco/5.1.9       netcdf-cxx4/4.3.1
gcc/13.2.0           ncview/2.1.9    netcdf-fortran/4.6.1
```

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
