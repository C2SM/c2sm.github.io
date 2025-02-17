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

Host balfrin* 
  Hostname %h.cscs.ch
  User cscsusername
  IdentityFile ~/.ssh/cscs-key
  ProxyJump ela

Host santis* daint* todi*
  Hostname %h.alps.cscs.ch
  User cscsusername
  IdentityFile ~/.ssh/cscs-key
  ProxyJump ela
```

This allows standard connections like `ssh santis`, but you can also specify a login node if needed, e.g., `ssh santis-ln002`. Replace `cscsusername` with your actual username.

## Santis

The vCluster `santis` is dedicated to **Climate and Weather** and may initially host only [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"} and related projects.

### Deployment Status

Currently, the deployment is approximately 95% complete. 

### Differences to the Environment on `todi`

- `$HOME` is now on a new NFS file system
    - Your folder `/users/$USER` will initially be mostly empty
    - The NFS system still requires fine-tuning, and file system performance may be low.
    - We recommend running tasks, especially heavy ones, on $SCRATCH.
- `todi`'s $HOME is mounted as `/users.OLD/$USER`.
    - ⚠️ The mount is read-only!
    - You are responsible for copying your data from `/users.OLD/$USER` to `/users/$USER/...`.
    - The mount is temporary and will be removed by the end of January 2025.

!!! info

    Despite the need to work on the deployment in the upcoming days, users are invited to already access the system and start familiarising themselves with it and they might also start the data migration of their old home.

    The activities on CSCS side should not require any reboot, however, some services might need to be restarted, e.g., SLURM. This could lead to short interruptions or even failing jobs. CSCS will provide more information in the upcoming days and will try to minimise the risk of interferences by consolidating changes.

### Uenvs

To find and use already existing uenvs from `todi`, you need to modify the `CLUSTER_NAME` environment variable.

```shell
export CLUSTER_NAME=todi
uenv image find
```

| uenv                       | activity                       |
|----------------------------|--------------------------------|
| `icon-wcp/v1:rc4`          | build and run ICON             |
| `netcdf-tools/2024:v1-rc1` | pre- and post-processing tools |

### Storage

!!! note "TODO"

The migration of the previous storage is not yet finished. Once there is an update from CSCS, we will inform you here. Also note that the environment variables `$STORE` and `$PROJECT` are not yet set.

## Daint

Daint (Alps) is the vCluster dedicated to the **User Lab**. It is accessible at `daint.alps.cscs.ch`.

The Climate and Weather Platform (CWP) has the dedicated vCluster `santis` (see [below](#santis)).
User Lab projects in climate and weather domain should be on  `santis`.

### Uenvs

As on `santis`, you can access the uenvs from `todi`:

```shell
export CLUSTER_NAME=todi
uenv image find
```

| uenv                       | activity                       |
|----------------------------|--------------------------------|
| `icon-wcp/v1:rc4`          | build and run ICON             |
| `netcdf-tools/2024:v1-rc1` | pre- and post-processing tools |

### Storage

!!! note "TODO"

The migration of the previous storage is not yet finished. Once there is an update from CSCS, we will inform you here.

