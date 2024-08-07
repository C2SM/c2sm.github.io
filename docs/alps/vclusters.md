# Virtual Clusters

## Available Clusters

### Santis

The vCluster dedicated to Weather and Climate is called `santis`.

- [CSCS Knowledge Base for Santis](https://confluence.cscs.ch/display/KB/Santis+Early+Access)

### Todi

An early-access vCluster with the new Grace-Hopper nodes is called `todi`.

- [CSCS Knowledge Base for Todi](https://confluence.cscs.ch/display/KB/Todi+early+access)

### Eiger

The production partition on Alps is called `eiger`.

- [CSCS Knowledge Base for Eiger](https://confluence.cscs.ch/display/KB/Alps+%28Eiger%29+User+Guide)

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

