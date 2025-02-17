# Supported vClusters

This page is hosting information about C2SM supported vClusters (not all CSCS vClusters). 

## Access

Connection to vClusters happens as for any other CSCS machine, e.g. `ssh santis.cscs.ch` with a `ProxyJump` on `ela.cscs.ch`.
A section in the `~/.ssh/config` could look as follows:

```config title="~/.ssh.config"
Host ela
  Hostname ela.cscs.ch
  User cscsusername
  IdentityFile ~/.ssh/cscs-key

Host santis* daint* 
  Hostname %h.alps.cscs.ch
  User cscsusername
  IdentityFile ~/.ssh/cscs-key
  ProxyJump ela

Host balfrin* 
  Hostname %h.cscs.ch
  User cscsusername
  IdentityFile ~/.ssh/cscs-key
  ProxyJump ela
```

This allows standard connections like `ssh santis`, but you can also specify a login node if needed, e.g., `ssh santis-ln002`. Replace `cscsusername` with your actual username.

## Santis

The vCluster `santis` is dedicated to **Climate and Weather** applications. It includes the following:

- [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"}: Project for ICON-based km-scale climate simulations
- Projects by C2SM community members
- User lab projects in climate and weather domains

### Uenvs

To find and use already existing uenvs from previous `todi`, you need to prepend the `CLUSTER_NAME` environment variable to any `uenv` command.

```shell
CLUSTER_NAME=todi uenv image find
```

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

## Daint

Daint (Alps) is the vCluster dedicated to the **User Lab**. It is accessible at `daint.alps.cscs.ch`.

The Climate and Weather Platform (CWP) has the dedicated vCluster `santis` (see [above](#santis)).
User Lab projects in climate and weather domain should be on  `santis`.

### Uenvs

As on `santis`, you can access the uenvs from `todi`:

```shell
CLUSTER_NAME=todi uenv image find
```

| uenv                       | activity                       |
|----------------------------|--------------------------------|
| `icon-wcp/v1:rc4`          | build and run ICON             |
| `netcdf-tools/2024:v1-rc1` | pre- and post-processing tools |

## Storage

The migration of the previous storage from old Piz Daint has been finished in January 2025. 

=== "Alps"
    ```console
    /capstor/store/cscs/c2sm
    ```
=== "Balfrin"
    ```console
    /capstor/store/cscs/c2sm
    ```
