!!! construction "Page under construction - last update: 2024-09-06"

    Information in this page is not yet complete nor final. It will be updated following the progress of

    - the Alps system deployment at CSCS
    - C2SM's adaptation to this new system

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

Host balfrin* daint* santis* todi*
  Hostname %h.cscs.ch
  User cscsusername
  IdentityFile ~/.ssh/cscs-key
  ProxyJump ela
```

This would allow standard connections like `ssh santis` but also specifying the login node like `ssh santis-ln002` if needed. Replace `cscsusername` with your actual user name.

## Daint

Daint (Alps) is the vCluster dedicated to the User Lab. It is currently accessible at `daint.alps.cscs.ch` (until the current Piz Daint gets decommissioned), so connect with `ssh daint.alps` with the `ssh` settings above.

Even though Weather and Climate also has the dedicated vCluster Santis (see [below](#santis)), traditional projects might also land on Daint.

### Uenvs

List of currently supported Uenvs on Daint:

| uenv                     | activity                       | Remark              |
|--------------------------|--------------------------------|---------------------|
| icon-vx:rcy              | build and run ICON             | Not deployed (yet?) |
| netcdf-tools/2024:v1-rc1 | pre- and post-processing tools |                     |

### Storage

!!! note "TODO"

    - [ ] Storage

## Santis

!!! warning "Santis has not been deployed yet."

Santis is dedicated to Weather and Climate. It might, at the beginning, only host [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"} and related projects.

### Uenvs

| uenv                     | activity                       |
|--------------------------|--------------------------------|
| icon-vx:rcy              | build and run ICON             |
| netcdf-tools/tag:version | pre- and post-processing tools |

### Storage

!!! note "TODO"

    - [ ] Storage


## Tödi

Tödi is the testing vCluster and is currently deployed on the most of the Alps system.

### Uenvs

| uenv                     | activity                       |
|--------------------------|--------------------------------|
| icon-wcp/v1:rc4          | build and run ICON             |
| netcdf-tools/2024:v1-rc1 | pre- and post-processing tools |
