---
title: ICON
layout: default
nav_order: 1
parent: Models
---

# ICON
ICON (Icosahedral Nonhydrostatic Weather and Climate Model) is a global model suitable for climate and weather prediction at regional and global domains.
It is a joint project of [DWD](https://www.dwd.de/DE/Home/home_node.html), [MPI-M](https://mpimet.mpg.de/startseite) and [KIT](https://www.kit.edu/).

C2SM facilitates the utilization of ICON on the [Piz Daint](https://www.cscs.ch/computers/piz-daint) and [Euler](https://scicomp.ethz.ch/wiki/Euler) computing platforms.

## Access
To gain access to the [ICON repository hosted on the C2SM GitHub organization](https://github.com/C2SM/icon), please contact your group's technical contact. They will be responsible for adding you to the appropriate user group. 

 Once you have access, clone the repository from GitHub using the SSH protocol:

  ```bash
  git clone --recurse-submodules git@github.com:C2SM/icon.git
  ```
  If you don't already have an SSH key set up for GitHub, but would like to do so, follow the [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
    
## Configure and compile
The ICON build process varies between Piz Daint and Euler. The CSCS platform Piz Daint uses Spack, whereas the ETHZ machine Euler requires manual build configuration for ICON. Instructions for both platforms are provided below.

### Piz Daint
For configuring and building ICON with Spack, please refer to the official spack-c2sm documentation, which provides instructions for [setting up a Spack instance](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin) and [installing ICON](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon).

### Euler
Before compiling ICON, it is essential to configure it using the respective script in the *config* folder. The configuration process using these files remains consistent across different machines and compilers.

Configure ICON:
```bash
./config/[platform]/[configuration_file]
```
Load required modules:
```bash
source modules.env
```
Compile ICON:
```bash
make -j 8
```

#### Compile with GCC using -O2 and CPU-specific optimizations:
- platform = ethz
- configuration_file = euler.cpu.gcc.O2


## Run test case with ICON
In the *run* folder, you find many prepared test cases, which you can convert into run scripts. To generate the runscript of one of the experiment files, e.g. *mch_ch_lowres*, you can use the *make_runscripts* function.

```bash
./make_runscripts mch_ch_lowres
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

```bash
cd run && sbatch ./exp.mch_ch_lowres.run
```
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include `--account <my_account_id>` in the `sbatch` command.

## Input files

- **CSCS:** `/users/icontest/pool/data/ICON`
- **Euler:** `/cluster/work/climate/icon_input`


## Toolset
In the [Tools](https://c2sm.github.io/tools) section, you can find all scripts and software related to pre- and postprocessing, toolchains and visualization.

## Quarterly C2SM ICON Meeting
[Minutes of the previous meetings](https://c2sm.github.io/events/icon_meeting.html){: .btn .btn-blue}

## Projects
[EXCLAIM - Extreme scale computing and data platform for cloud-resolving weather and climate modeling](https://exclaim.ethz.ch/){: .btn .btn-blue}  
[ICON-HAMMOZ](https://redmine.hammoz.ethz.ch/){: .btn .btn-blue}  


## Documentation
   * [ICON Tutorial (DWD) last update: Mar 2023](https://www.dwd.de/EN/ourservices/nwv_icon_tutorial/nwv_icon_tutorial_en.html)
   * MPI-M documentation [webpage](https://code.mpimet.mpg.de/projects/iconpublic/wiki/Documentation)
     
## External Software
   * [CDO](https://code.zmaw.de/projects/cdo), Climate Data Operators
