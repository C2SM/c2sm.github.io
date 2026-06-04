# Balfrin

Balfrin is an Alps cluster used by MeteoSwiss.
Located in Lugano and hosted by CSCS.
Balfrin is a MPI cluster with slurm. Balfrin is used for R&D and for production failover.

## Hardware

Node type           | Nodes |  GPU type    |  GPUs |  GPU RAM per GPU | CPU model type |  CPU Sockets |  Cores per socket |  Threads per core | Threads |           RAM |                Comment |
--------------------|-------|--------------|-------|------------------|----------------|--------------|-------------------|-------------------|---------|---------------|------------------------|
Login node          |     3 |         -    |     0 |                - |  AMD EPYC 7713 |            2 |                64 |                 2 |     256 | 256 or 512 GB |                        |
GPU node            |    46 |  nvidia A100 |     4 |            96 GB |  AMD EPYC 7713 |            1 |                64 |                 2 |     128 |        512 GB |                        |
Postprocessing node |    15 |            - |     0 |                - |  AMD EPYC 7713 |            2 |                64 |                 2 |     256 |        512 GB |                        | 
User Access Node*   |     1 |            - |     0 |                - |  AMD EPYC 7713 |            2 |                64 |                 2 |     256 |        512 GB | Has a RMDCN connection |

This is the maximum configuration, and can be scaled down according to the demand.

C2SM does not officially support Balfrin. Nevertheless,  you can find instructions on how
to set up ICON on Balfrin at the [Compile section of ICON](../models/icon/compile.md#balfrin).


## Storage
CSCS Documentation 

## Quota
User's home has a size limit per user with a soft limit at 80GB and a hard limit at 100GB.
Use `df -h $HOME`, `lsattr -p -d $HOME` or `lfs quota -p 74 /users -h` to get more info.

CSCS' documentation on Lustre quotas: https://confluence.cscs.ch/x/v4EzMw

## Network
The login nodes can be accessed via balfrin.cscs.ch and tasna.cscs.ch. This will forward you to a random login node, so you can profit form their redundancy.


## Example Job Script

```
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --output=output.txt
#SBATCH --error=error.txt
#SBATCH --time=01:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --partition=partition_name
module load my_module
srun my_program
```

## Software stack
CSCS installs lower-level and general purpose software in `/mch-environment/`. It contains a directory for each version of the stack. Versions are immutable, but will be decommissioned eventually.


Details of the software stack content

Scientific applications, libraries and tools are available through different uenv’s. 

Module is used for dynamically loading and unloading environments for software (like paths to software executables and libraries), inside and outside of the uenvs.

Spack is the package manager available to install software easily. Additionally, CSCS uses their stackinator to build software stacks.

### General purpose software
The environment variable $USER_ENV_ROOT contains the path to the latest production-grade version of the software stack - all version are installed under “/mch-environment/”. To use its modules, run

```
module use $USER_ENV_ROOT/modules
```
to see an overview of its content, run

```
module avail
```
This might be a good candidate to put in your bashrc.

Domain specific software available in user environments (uenv)
Some software (e.g. ncview) is available in specific user environment. 

To use those environments, you first need to install a command-line tool provided by CSCS, see "Getting Started" on https://confluence.cscs.ch/display/KB/UENV+user+environments . 

This page also explains how to use those uenvs, in short there are three options (example for ncview, versions as of 6 August 2024):

Use an uenv that defines modules:
```
uenv start --view=modules climana/24.7:v1-rc4
module load ncview/2.1.9
ncview
```
or

```
uenv start climana/24.7:v1-rc4
uenv view modules
module load ncview/2.1.9
ncview
```
Use an uenv that directly adds applications:
```
uenv start --view=default netcdf-tools/2024:v1
ncview
```
or
```
uenv start netcdf-tools/2024:v1
uenv view default
ncview
```
Run scripts with specific uenvs without loading them in the shell 
```
uenv run {uenv/version:tag} -- ./job-using-uenv.sh
```
:light_bulb_on: deactivate a loaded uenv with uenv stop.

## Spack
You can use Spack to install software, as it is capable of installing lots of software without sudo rights.

Spack-C2SM is an extension of Spack, that contains additional MeteoSwiss specific software and can be used by cloning the repo and sourcing its env:

```
git clone --depth 1 --recurse-submodules --shallow-submodules https://github.com/C2SM/spack-c2sm.git -b latest
. spack-c2sm/setup-env.sh $USER_ENV_ROOT
```
to see an overview of its content, run

```
spack find
```
to install software, run
```
spack install libelf
```
Spack is a package manager, like apt, yum, pip, conda.

Spack-c2sm is an extension of spack, that hosts proprietary packages and machine specific configs.