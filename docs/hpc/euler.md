# Euler

Euler is ETH Zurich's central high-performance computing (HPC) cluster, providing computational resources for research across all disciplines.

## Access

Groups at IAC have shares for storage and CPU via the Euler **Climate** group. As a group member, you should have an existing account and access to Euler. If this is not the case, contact your group leader or Urs Beyerle.

## Useful Links

- [Euler documentation :material-open-in-new:](https://docs.hpc.ethz.ch/){:target="_blank"}
- [Climate Euler users :material-open-in-new:](https://wiki.iac.ethz.ch/Collaboration/EulerUsers){:target="_blank"} (:material-lock: IAC login required)
- [Accounting :material-open-in-new:](https://wiki.iac.ethz.ch/Collaboration/EulerAccounting){:target="_blank"} (:material-lock: IAC login required)
- [Euler Climate members :material-open-in-new:](https://wiki.iac.ethz.ch/Collaboration/EulerClimateMembers){:target="_blank"} (:material-lock: IAC login required)

## Software Stack

Euler provides a [software stack :material-open-in-new:](https://docs.hpc.ethz.ch/software/software-stack/){:target="_blank"} via the module command:

```bash
module load stack openmpi
module list
# Currently Loaded Modules:
#  1) gcc/12.2.0   2) stack/2025-06   3) openmpi/4.1.7
```

Afterwards, one can load specific software such as:

```bash
module load cdo nco ncview netcdf-c
module list
# Currently Loaded Modules:
#  1) gcc/12.2.0   2) stack/2025-06   3) openmpi/4.1.7   4) cdo/2.4.4   5) nco/5.2.4   6) ncview/2.1.9   7) netcdf-c/4.9.2
```

With that, one has access to the most commonly used tools for climate applications:

```bash
which cdo ncdump ncview ncrcat
# /cluster/software/stacks/2025-06/linux-ubuntu22.04-x86_64_v3/gcc-12.2.0/cdo-2.4.4-spns4mysmzmbj7eh37zswj64efou4xvr/bin/cdo
# /cluster/software/stacks/2025-06/linux-ubuntu22.04-x86_64_v3/gcc-12.2.0/netcdf-c-4.9.2-sekz6xps6vd4zyacqlj6e4gesed7hi7t/bin/ncdump
# /cluster/software/stacks/2025-06/linux-ubuntu22.04-x86_64_v3/gcc-12.2.0/ncview-2.1.9-hszhkgti42fealjswfivjjk5r3i3xcob/bin/ncview
# /cluster/software/stacks/2025-06/linux-ubuntu22.04-x86_64_v3/gcc-12.2.0/nco-5.2.4-zhb3mn5upr3rniqoebeyfreb7uabpohi/bin/ncrcat

```