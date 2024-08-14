!!! construction "Page under construction"

    Information in this page is not yet complete nor final. It will be updated following the progress of

    - the Alps system deployment at CSCS
    - C2SM's adaptation to this new system

# Supported vClusters

## Available Clusters

### Daint

Daint is the vCluster dedicated to the User Lab. Even though Weather and Climate 

### Santis

The vCluster dedicated to Weather and Climate is called `santis`.

- [CSCS Knowledge Base for Santis :material-open-in-new:](https://confluence.cscs.ch/display/KB/Santis+Early+Access){:target="_blank"}

### Todi

An early-access vCluster with the new Grace-Hopper nodes is called `todi`.

- [CSCS Knowledge Base for Todi :material-open-in-new:](https://confluence.cscs.ch/display/KB/Todi+early+access){:target="_blank"}

### Eiger

The production partition on Alps is called `eiger`.

- [CSCS Knowledge Base for Eiger :material-open-in-new:](https://confluence.cscs.ch/display/KB/Alps+%28Eiger%29+User+Guide){:target="_blank"}

## Access

Connection to vClusters happens as for any other CSCS machine, e.g. `ssh santis.cscs.ch` with a `ProxyJump` on `ela.cscs.ch`.
A section in the `~/.ssh/config` could look as follows:

```config title="~/.ssh.config"
Host ela
    HostName ela.cscs.ch
    User cscsusername
    ForwardAgent yes
    IdentityFile ~/.ssh/cscs-key
Host santis
    HostName santis.cscs.ch
    User cscsusername
    ProxyJump ela
    IdentityFile ~/.ssh/cscs-key
```

## Software Stacks

Software stacks are provided through the so-called [user environments](uenvs.md).

