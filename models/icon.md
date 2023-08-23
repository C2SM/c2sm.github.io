---
title: ICON Icosahedral Nonhydrostatic Weather and Climate Model
layout: default
nav_order: 1
parent: Models
---

## ICON: Icosahedral Nonhydrostatic Weather and Climate Model
ICON is a global model suitable for climate and weather predictions for both, regional and global domains.
It is a joint project of [DWD](https://www.dwd.de/DE/Home/home_node.html), [MPI-M](https://mpimet.mpg.de/startseite) and [KIT](https://www.kit.edu/).

### Access
In order to get access to the [ICON repository hosted on the C2SM GitHub organization](https://github.com/C2SM/icon), please contact your group's technical contact. They will be responsible for adding you to the appropriate user group. 

 Once you have access, clone the repository from GitHub using the SSH protocol:

  ```bash
  git clone --recurse-submodules git@github.com:C2SM/icon.git
  ```
  If you don't already have an ssh key set up for GitHub, but would like to do so, follow the [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
    
### Configure and compile
The ICON build mechanism is different on Piz Daint and Euler. On Daint, Spack is used, whereas on Euler, ICON is build manually with configuration files. 

#### Piz Daint
Spack takes care of configuring and building ICON. For detailed instructions, please consider the official spack-c2sm [documentation](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon)

#### Euler (ETHZ)

ICON needs to be configured before compilation. There is a configure-script for each compiler and/or machines located in config. The general procedure using configuration files is independent of machines or compilers.

```bash
./config/[machine_you_want_to_compute_on]/[configuration_filename]
```
On Euler, compile with gcc, O2 and CPU:

```bash
./config/ethz/euler.cpu.gcc.O2

# load the required modules
source modules.env

# compile
make -j 8
``` 
### Input files

**CSCS:** ```/users/icontest/pool/data/ICON```

**Euler:** ```/cluster/work/climate/icon_input```


### Toolset
   * **Extpar:** External parameters for the ICON-grid (preprocessing)
   * **Icontools:** A set of tools for extracting and remapping ICON fields (preprocessing)
   * **Spice:** The Starter Package for ICON-CLM Experiments (processing chain)
   * **Processing Chain:** COSMO and ICON Processing Chain 
   * [icon-vis](https://github.com/C2SM/icon-vis): Visualizing ICON output data on the native grid

### Documentation
   * [ICON Tutorial (DWD) last update: Mar 2023](https://www.dwd.de/EN/ourservices/nwv_icon_tutorial/nwv_icon_tutorial_en.html)
   * MPI-M documentation [webpage](https://code.mpimet.mpg.de/projects/iconpublic/wiki/Documentation)
     
### External Software
   * [CDO](https://code.zmaw.de/projects/cdo), climate data operator
