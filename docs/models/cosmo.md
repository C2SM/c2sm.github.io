---
title: COSMO
layout: default
nav_order: 1
parent: Models
---

# COSMO
The COSMO model is a limited-area, non-hydrostatic model developed by a collaboration of National Weather Services called the [Consortium for Small-scale Modeling](http://www.cosmo-model.org/).

## Support status
C2SM currently facilitates the utilisation of COSMO on the [Piz Daint](https://www.cscs.ch/computers/piz-daint) computing platform for CPU and GPU architectures. The `master` and `c2sm-features` branches are being continuously tested an Piz Daint.

The following table summarises the features ported to GPU and their correspoding namelist parameters.

<details close markdown="block">
<summary>gpu ported COSMO features</summary>
{: .text-delta }

##### Parameters in `INPUT_ORG`

| scheme/parameterisation                       | namelist parameter                                                                                                                                                                  | GPU porting status                                 |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Physics                                       | `lphys`                                                                                                                                                                             | ported                                             |
| Diagnostics                                   | `ldiagnos`                                                                                                                                                                          | ported                                             |
| Digital filtering                             | `ldfi`                                                                                                                                                                              | not ported                                         |
| Use observations                              | `luseobs`                                                                                                                                                                           | ported                                             |
| Ensemble mode                                 | `leps`                                                                                                                                                                              | ported                                             |
| Stochastic perturbation of physics tendencies | `lsppt`                                                                                                                                                                             | ported                                             |
| Synthetic satellite images                    | `luse_rttov`                                                                                                                                                                        | not ported                                         |
| Radar forward operator                        | `luse_radarfwo`                                                                                                                                                                     | not ported                                         |
| Aerosol and Reactive Tracer module (ART)      | `l_cosmo_art`                                                                                                                                                                       | not ported                                         |
| Pollen module                                 | `l_pollen`                                                                                                                                                                          | ported (available in MeteoSwiss Fork only)         |
| Online trajectory module                      | `l_traj`                                                                                                                                                                            | ported                                             |
| Zero vertical velocity on lower boundary      | `llm`                                                                                                                                                                               | not supported in the C++ dycore                    |
| Incremental analysis update                   | `itype_iau = 0`, `1`, `2`                                                                                                                                                           | Only itype_iau = 0 ported                          |
| Idealised runs                                | `lartif_data`                                                                                                                                                                       | not ported                                         |
| 2D model runs                                 | `l2dim`                                                                                                                                                                             | not ported                                         |
| Periodic boundary conditions in X direction   | `lperi_x`                                                                                                                                                                           | ported (not tested)                                |
| Periodic boundary conditions in Y direction   | `lperi_y`                                                                                                                                                                           | ported (not tested)                                |
| Reproducible results in parallel mode         | `lreproduce`                                                                                                                                                                        | ported                                             |
| Reorder MPI process numbering                 | `lreorder`                                                                                                                                                                          | not ported                                         |
| Implicit MPI buffering                        | `ldatatypes`                                                                                                                                                                        | ported                                             |
| Additional MPI barriers                       | `ltime_barrier`                                                                                                                                                                     | ported                                             |
| Write ASCII files every time step             | `ldump_ascii`                                                                                                                                                                       | ported                                             |
| All processors write debug output             | `lprintdeb_all`                                                                                                                                                                     | ported                                             |
| Debug statements in various model sections    | `ldebug_dyn`, `ldebug_gsp`, `ldebug_rad`, `ldebug_sso`, `ldebug_tur`, `ldebug_con`, `ldebug_soi`, `ldebug_io`, `ldebug_mpe`, `ldebug_dia`, `ldebug_lhn`, `ldebug_ass`, `ldebug_art` | partially ported, not all prints are active on GPU |
| Initialise local variables                    | `linit_fields`                                                                                                                                                                      | not ported                                         |

##### Parameters in `INPUT_PHY`

| scheme/parameterization                   | namelist parameter                                    | GPU porting status                                                          |
|-------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------|
| Grid-scale precipitation scheme           | `lgsp`                                                | ported                                                                      |
| Grid-scale precipitation scheme type      | `itype_gscp = 1`, `2`, `3`, `4`                       | only `itype_gscp = 3`, `4` ported to gpu                                    |
| Run grid-scale precipitation scheme first | `lgsp_first`                                          | only `lgsp_first = .TRUE.` ported to gpu                                    |
| Radiation                                 | `lrad`                                                | ported                                                                      |
| Cloud representation mode                 | `icldm_rad = 0`, `1`, `3`, `4`                        | all options ported                                                          |
| Forest                                    | `lforest`                                             | ported                                                                      |
| Topographic correction of radiation       | `lradtopo`                                            | ported                                                                      |
| External surface emissivity               | `lemiss`                                              | ported                                                                      |
| Aerosol scheme type                       | `itype_aerosol = 1`, `2`, `3`                         | only `itype_aerosol = 1`, `2` ported                                        |
| Albedo scheme type                        | `itype_albedo = 1`, `2`, `3`, `4`                     | all options ported                                                          |
| Convection scheme                         | `lconv`                                               | ported                                                                      |
| Convection scheme type                    | `itype_conv = 0`, `2`, `3`                            | all options ported                                                          |
| Vertical turbulent diffusion              | `ltur`                                                | ported                                                                      |
| Old turbulence scheme behavior            | `loldtur`                                             | Only `loldtur = .TRUE.` is ported and tested                                |
| Vertical diffusion calculation location   | `itype_vdif = -1`, `0`, `1`                           | `itype_vdif = -1` is ported. `itype_vdif = 0`, `1` is ported but NOT tested |
| Turbulence scheme type                    | `itype_turb = 1`, `3`, `5/7`                          | only `itype_turb = 3` is tested                                             |
| 3D turbulence                             | `l3dturb`                                             | not ported                                                                  |
| TKE equation type                         | `imode_turb = 0`, `1`, `2`                            | only `imode_turb` is tested                                                 |
| SSO wake turbulent production             | `ltkesso`                                             | ported                                                                      |
| TKE convective buoyancy production        | `ltkecon`                                             | ported                                                                      |
| TKE horizontal shear production           | `ltkeshs`                                             | ported - not tested                                                         |
| Shear production type                     | `itype_sher = 0`, `1`, `2`                            | only `0` is tested                                                          |
| Transfer scheme type                      | `itype_tran = 1`, `2`                                 | only `0` is tested                                                          |
| TKE equation type in transfer scheme      | `imode_tran = 0`, `1`, `2`                            | only `1` is tested                                                          |
| Soil model                                | `lsoil`                                               | ported                                                                      |
| Sea ice scheme                            | `lseaice`                                             | not ported                                                                  |
| Flake lake model                          | `llake`                                               | ported                                                                      |
| Multi-layer snow model                    | `lmulti_snow`                                         | ported but NOT tested                                                       |
| Vegetation transpiration type             | `itype_trvg = 1`, `2`                                 | all options ported                                                          |
| Bare soil evaporation type                | `itype_evsl = 2`, `3`, `4`                            | all options ported                                                          |
| Root distribution type                    | `itype_root = 1`, `2`                                 | all options ported                                                          |
| Canopy parameterization type              | `itype_canopy = 1`, `2`                               | all options ported                                                          |
| Soil heat conductivity type               | `itype_heatcond = 1`, `2`, `3`                        | all options ported                                                          |
| Mire parameterization type                | `itype_mire = 0`, `1`                                 | all options ported                                                          |
| Hydraulic lower boundary parameterization | `itype_hydbound = 1`, `3`                             | all options ported                                                          |
| Snow-cover fraction type                  | `idiag_snowfrac = 1`, `2`, `3`, `4`, `20`, `30`, `40` | all options ported                                                          |
| Subgrid scale orography                   | `lsso`                                                | ported                                                                      |

##### Parameters in `INPUT_DYN`

The GPU porting of the dynamical core of COSMO was accomplished by rewriting the dynamics with the Gridtools stencil library. The Gridtools dycore supports a subset of the parameters of the COSMO Fortran dynamical core. The list of features currently supported in the Gridtools dycore can be found in the [documentation in the code repository] (https://github.com/C2SM-RCM/cosmo/blob/master/dycore/doc/Dycore/supported_configuration.tex).

</details>

{: .attention-title }

> Warnings
>
> - The support status on the future Alps system is not yet known. It strongly depends on the ability to use an old interpretation of the OpenACC standard.
>
> - C2SM's support for COSMO is scheduled to stop end of 2024

## Access
In order to get access to the [COSMO repository](https://github.com/C2SM-RCM/cosmo) hosted on the C2SM-RCM GitHub organisation,
please contact [C2SM Support](mailto:support@c2sm.ethz.ch).

Once you have access, clone the repository from GitHub using the SSH protocol:
```
git clone git@github.com:C2SM-RCM/cosmo.git
```
If you do not already have an SSH key set up for GitHub but would like to do so, follow the [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

## Configure and compile
For configuring and building COSMO with Spack, please refer to the official spack-c2sm documentation, which provides instructions for [setting up a Spack instance](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin) and [installing COSMO](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#cosmo) on Piz Daint.

## Related tools
In the [Tools](https://c2sm.github.io/tools) section, you will find relevant tools for working with COSMO:
* [**Extpar:**](https://c2sm.github.io/tools/extpar.html) External parameters for the COSMO-grid (preprocessing)
* [**int2lm:**](https://c2sm.github.io/tools/int2lm.html) The interpolation software for the COSMO-model (preprocessing)
* [**Processing Chain**](https://c2sm.github.io/tools/processing_chain.html): Python workflow tool for COSMO


## Documentation
COSMO documentation is available at:
* [Official website of the Consortium for Small-scale Modeling (COSMO)](http://www.cosmo-model.org/)
* [COSMO Model System Overview](https://www.cosmo-model.org/content/model/cosmo/default.htm)
* [COSMO User's Guide](https://www.cosmo-model.org/content/model/cosmo/coreDocumentation/cosmo_userguide_6.00.pdf) 

## Asynchronous IO for NetCDF - A Guide for an optimal model setup

### Node configuration
When using asynchronous IO (Input/Output), the workload of the IO processors must be carefully balanced.
In general, no robust "rule of thumb" has been found, so some benchmark runs may be necessary.
Finding an optimal setup is not trivial, since the number of output namelists, the number of fields, and the number of IO processors may vary between different setups.
In particular, overloading the IO processors during model cleanup at the end of a job leads to additional runtime.
Note that using online compression can sometimes significantly increase the time and resources required for IO.

A quick overview of the actual workload on the IO processors can be obtained from the COSMO logs by increasing the verbosity settings of the log (`ldebug_io=.true.`, `idbg_level=6`):
```
Asyn-IO: block number xx was filled. Allocating a new block
```

The above log is printed each time a new buffer block is allocated.
This means that the Compute PEs (Processing Elements) store output data until the IO processors write it to disk.
If the number of allocated blocks increases during the simulation, i.e., more and more buffer blocks must be stored on the compute PEs after each output step, the IO processors will not write as fast as the model generates new output.

When the speed of writing data to disk by the IO processors and the model timestepping are in balance, the log message changes to:
```
 Asyn-IO: block number xx was filled, but the oldest one was released
```
It indicates that a balance has been reached between writing data to disk and the model generating new output.
In addition, each time an output file is completely written to disk, the corresponding IO processor prints a message that looks like this:

```
start_ionode:  Next asynchronous output will be done in step: xx
```

This log can give additional insight into how long it takes to write a file to disk.
In addition, there is a timer called `asyncio_wait` in the output section of YUTIMING. 

```
Output                         0.19         0.43         0.86        72.65
  computations O               0.08         0.11         0.16        17.71
  meta  data                   0.00         0.00         0.00         0.00
  write data                   0.00         0.19         0.55        32.70
  gather data                  0.10         0.12         0.14        20.35
  asynIO wait                  0.00         0.78         4.31       130.84
```
It provides information about how long all compute-PEs had to wait at the end of the simulation for all IO processors to finish writing data to disk.
This timer should be as small as possible.

### Zlib replacement for NetCDF compression
Online compression, enabled with the `lcompress_netcdf=.true.` parameter, uses the slower Zlib by default.
A speedup of a factor of two can be achieved by using Zlib_ng instead.
The `+zlib_ng` variant for building COSMO is required in combination with the command `spack load cosmo@master%pgi cosmo_target=gpu +zlib_ng` before execution.
Unfortunately, the convenient way of using RPATH for this feature is not possible.
