# Santis



This allows standard connections like `ssh santis`, but you can also specify a login node if needed, e.g., `ssh santis-ln002`. Replace `cscsusername` with your actual username.

## Santis

The vCluster `santis` is dedicated to **Climate and Weather** applications. It includes the following:

- [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"}: Project for ICON-based km-scale climate simulations
- Projects by C2SM community members
- User lab projects in climate and weather domains

### User Environments (uEnvs)

| uenv                       | activity                       |
|----------------------------|--------------------------------|
| `icon-wcp/v1:rc4`          | build and run ICON             |
| `netcdf-tools/2024:v1-rc1` | pre- and post-processing tools |

### SLURM Partitions

| SLURM partition | Default wall time | Max. wall time | Limitations |
|-----------------|-------------------|----------------|-------------|
| normal          | 01:00:00          | 24:00:00       | -           |
| debug           | 00:30:00          | 00:30:00       | Single node |  
| xfer            | 06:00:00          | 24:00:00       | Single node |
