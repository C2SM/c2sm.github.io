# Balfrin

Balfrin is a high-performance computing (HPC) cluster used by MeteoSwiss, located in Lugano and hosted by CSCS (Swiss National Supercomputing Centre). It is an [MPI :material-open-in-new:](https://en.wikipedia.org/wiki/Message_Passing_Interface){:target="_blank"} cluster managed by [Slurm :material-open-in-new:](https://slurm.schedmd.com/){:target="_blank"}, primarily used for research and development (R&D) and as a production failover system.

> Note: C2SM does not officially support Balfrin. However, instructions for setting up ICON on Balfrin are available in the [Compile section of ICON](../models/icon/compile.md#balfrin).


## Hardware Specifications

Balfrin's hardware is designed for scalability. The maximum configuration is outlined below, but resources can be scaled down based on demand in the future.

Node type           | Nodes |                                                    GPU type    |  GPUs |  GPU RAM per GPU | CPU model type                                                      |  CPU Sockets |  Cores per socket |  Threads per core | Threads |           RAM |
--------------------|-------|----------------------------------------------------------------|-------|------------------|---------------------------------------------------------------------|--------------|-------------------|-------------------|---------|---------------|
Login node          |     3 |                                                              - |     0 |                - |  [AMD EPYC 7713 :material-open-in-new:](https://www.amd.com/en/products/cpu/amd-epyc-7713){:target="_blank"} |            2 |                64 |                 2 |     256 | 256 or 512 GB |
GPU node            |    46 |  [NVIDIA A100 :material-open-in-new:](https://www.nvidia.com/en-us/data-center/a100/){:target="_blank"} |     4 |            96 GB |  [AMD EPYC 7713 :material-open-in-new:](https://www.amd.com/en/products/cpu/amd-epyc-7713){:target="_blank"} |            1 |                64 |                 2 |     128 |        512 GB |
Postprocessing node |    15 |                                                              - |     0 |                - |  [AMD EPYC 7713 :material-open-in-new:](https://www.amd.com/en/products/cpu/amd-epyc-7713){:target="_blank"} |            2 |                64 |                 2 |     256 |        512 GB | 
User Access Node*   |     1 |                                                              - |     0 |                - |  [AMD EPYC 7713 :material-open-in-new:](https://www.amd.com/en/products/cpu/amd-epyc-7713){:target="_blank"} |            2 |                64 |                 2 |     256 |        512 GB |


## Storage and Quota


### Storage
For detailed storage documentation, refer to the [CSCS Storage Documentation :material-open-in-new:](https://docs.cscs.ch/storage/){:target="_blank"}.

### Quota

Home Directory Limits:

- Soft limit: 80 GB
- Hard limit: 100 GB

To check your quota usage, use one of the following commands:
```bash
# Check home directory usage
df -h $HOME

# Check Lustre attributes
lsattr -p -d $HOME

# Check project quota (example for /users)
lfs quota -p 74 /users -h
```

For more information, see the CSCS [Lustre Quotas Guide :material-open-in-new:](https://confluence.cscs.ch/x/v4EzMw){:target="_blank"}.

## Network Access

The login nodes can be accessed via `balfrin.cscs.ch`. This will forward you to a random login node, so you can profit form their redundancy.


## Example Job Script
Below is a template for submitting jobs using Slurm on Balfrin:
```bash
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

## Software Stack
### Overview
CSCS provides a curated software stack for general-purpose and domain-specific applications. The stack is installed in `/mch-environment/` and is organized by version, with each version being immutable but subject to eventual decommissioning.

### General purpose software
The `$USER_ENV_ROOT` environment variable points to the latest production-grade software stack.

### Loading Modules
To use the modules in the stack:
```bash
# Add the stack's module directory to your MODULEPATH
module use $USER_ENV_ROOT/modules

# List available modules
module avail
```
> Tip: Consider adding `module use $USER_ENV_ROOT/modules` to your `~/.bashrc` for convenience.

### Domain-Specific Software (UENV)
Some software (e.g., ncview) is available in user environments (uenvs). To use these:

1. Install the CSCS UENV CLI: Follow the [Getting Started Guide :material-open-in-new:](https://confluence.cscs.ch/display/KB/UENV+user+environments){:target="_blank"}.

2. Using UENV: There are three ways to use uenvs:

   - Option 1: Load modules from a uenv
   
     ```bash
     uenv start --view=modules climana/24.7\:v1-rc4
     module load ncview/2.1.9
     ncview
     ```

   - Option 2: Directly add applications
   
     ```bash
     uenv start --view=default netcdf-tools/2024\:v1
     ncview
     ```

   - Option 3: Run scripts with a specific uenv
   
     ```bash
     uenv run {uenv/version\:tag} -- ./job-using-uenv.sh
     ```


## Spack and Spack-C2SM

### Spack
Spack is a flexible package manager for HPC. It allows users to install software without sudo rights and manage complex dependencies.

### Spack-C2SM
Spack-C2SM is an extension of Spack, tailored for MeteoSwiss. It includes proprietary packages and machine-specific configurations.

#### Setup
```bash
# Clone the Spack-C2SM repository
git clone --depth 1 --recurse-submodules --shallow-submodules \
  https://github.com/C2SM/spack-c2sm.git -b latest

# Source the environment
. spack-c2sm/setup-env.sh \$USER_ENV_ROOT
```
#### Usage
```bash
# List available packages
spack find

# Install a package (e.g., libelf)
spack install libelf
```
> Note: Spack-C2SM is designed to complement the CSCS software stack, providing additional tools and libraries specific to MeteoSwiss workflows.