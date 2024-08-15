!!! construction "Page under construction"

    Information in this page is not yet complete nor final. It will be updated following the progress of

    - the Alps system deployment at CSCS
    - C2SM's adaptation to this new system

# Supported vClusters

This page is hosting information about C2SM supported vClusters. 

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

This would allow standard connections like `ssh santis.cscs.ch` but also specifying the login node like `ssh santis-ln002.cscs.ch` if needed.

## Daint

Daint is the vCluster dedicated to the User Lab. It is deployed on ~800 Grace-Hopper nodes.

Even though Weather and Climate also has the dedicated vCluster Santis (see [below](#santis){:target="_blank"}), traditional projects will be running on Daint.

!!! warning "Hostname conflict"

    For the duration of the overlap between the current expiring Piz Daint and its reincarnation as a vCluster, there will be two different host names. Most probably the current Piz Daint will continue being accessible at `daint.cscs.ch` while the vCluster hostname is not known yet.

### Uenvs

List of currently supported Uenvs on Daint:

| uenv        | activity                      |
|-------------|-------------------------------|
| icon-vx:rcy | build and run icon            |
| prepost-vx  | pre and post processing tools |
|             |                               |

### Storage

!!! note "TODO"

    - [ ] Storage

## Santis

Santis is dedicated to Weather and Climate and is deployed on ~400 Grace-Hopper nodes. At least at the beginning, it will be hosting only [EXCLAIM :material-open-in-new:](https://c2sm.ethz.ch/research/exclaim.html){:target="_blank"} and related projects.

### Uenvs

| uenv        | activity                      |
|-------------|-------------------------------|
| icon-vx:rcy | build and run icon            |
| prepost-vx  | pre and post processing tools |
|             |                               |

### Storage

!!! note "TODO"

    - [ ] Storage
