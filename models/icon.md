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

To stay informed about what is going on in the ICON world and to get to know other ICON users, please attend our [quarterly ICON meeting](https://c2sm.github.io/events/icon_meeting.html).

## Support status
C2SM facilitates the utilization of ICON on the [Piz Daint](https://www.cscs.ch/computers/piz-daint) and [Euler](https://scicomp.ethz.ch/wiki/Euler) computing platforms for the CPU and GPU architectures.

The following table summarizes the features ported to GPU and their correspoding namelist parameters.

<details close markdown="block">
<summary>gpu ported ICON features </summary>

TODO
{: .label .label-red }

###### Parameters in namelist `XXX`
{: .no_toc }

| scheme/parameterization | namelist parameter | GPU porting status |
|-------------------------|--------------------|--------------------|
| feature a               | `lfeature_a`       | ported             |
| feaure b                | `lfeature_b`       | partly ported      |

</details>

### Supported release
The latest release distributed by C2SM, currently `2.6.6`, is continuously tested on both Piz Daint and Euler and receives patches when necessary.

## Access
To gain access to the [ICON repository](https://github.com/C2SM/icon) hosted on the C2SM GitHub organization, please contact your group's technical contact. They will be responsible for adding you to the appropriate user group. 

 Once you have access, clone the repository from GitHub using the SSH protocol:

  ```bash
  git clone --recurse-submodules git@github.com:C2SM/icon.git
  ```
  If you don't already have an SSH key set up for GitHub, but would like to do so, follow the [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
    
## Configure and compile
The ICON build process varies between Piz Daint and Euler. The CSCS platform Piz Daint uses Spack, whereas the ETHZ machine Euler requires manual build configuration for ICON. Instructions for both platforms are provided below.

### Piz Daint
For configuring and building ICON with Spack, please refer to the official spack-c2sm documentation, which provides instructions for [setting up a Spack instance](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin) and [installing ICON](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon). When cloning Spack, be sure to use the Spack tag provided in the ICON repository at [config/cscs/SPACK_TAG](https://github.com/C2SM/icon/blob/main/config/cscs/SPACK_TAG).

### Euler
Before compiling ICON, it is essential to configure it using the respective script in the *config* folder. The configuration process using these files remains consistent across different machines and compilers.

Configure ICON with GCC using -O2 and CPU-specific optimizations:
```bash
./config/ethz/euler.cpu.gcc.O2
```
Load required modules:
```bash
source modules.env
```
Compile ICON:
```bash
make -j 8
```

## Run test case with ICON
In the *run* folder, you find many prepared test cases, which you can convert into run scripts. To generate the runscript of one of the experiment files, e.g. *mch_ch_lowres*, you can use the `make_runscripts` function.

```bash
./make_runscripts mch_ch_lowres
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

```bash
cd run && sbatch ./exp.mch_ch_lowres.run
```
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include `--account <my_account_id>` in the `sbatch` command.

## Input data
ICON input data are stored at the following locations:
- **Piz Daint (CSCS):** `/users/icontest/pool/data/ICON`
- **Euler:** `/cluster/work/climate/icon_input`


## Toolset
In the [Tools](https://c2sm.github.io/tools) section, you will find relevant tools for working with ICON:
* [**Extpar:**](https://c2sm.github.io/tools/extpar.html) External parameters for the ICON grid (preprocessing)
* [**Processing Chain**](https://c2sm.github.io/tools/processing_chain.html): Python workflow tool for ICON
* [**SPICE**](https://c2sm.github.io/tools/spice.html): Starter package for ICON-CLM experiments
* [**icon-vis**](https://c2sm.github.io/tools/icon-vis.html): Python scripts to visualize ICON data

## Projects
Learn more about ongoing projects involving ETHZ in the development of ICON:
  * [EXCLAIM](https://exclaim.ethz.ch/) 
  * [ICON-HAMMOZ](https://redmine.hammoz.ethz.ch/projects/icon-hammoz)

## Documentation
ICON documentation is available at:
   * [ICON Tutorial (DWD)](https://www.dwd.de/EN/ourservices/nwv_icon_tutorial/nwv_icon_tutorial_en.html)
   * [MPI-M documentation](https://code.mpimet.mpg.de/projects/iconpublic/wiki/Documentation)
     
## External Software
The following external software is useful for working with ICON data:
   * [CDO](https://code.zmaw.de/projects/cdo)
