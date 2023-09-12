---
title: Supported Software and Libraries
layout: default
nav_order: 2.1
has_children: false
---

# Supported Software and Libraries
{: .no_toc }

This page has two main goals:
- to list currently used C2SM software and their support details
- to list existing library dependencies in C2SM used software and their support details.

It clarifies the responsibility for different levels of support across all involved institutions in the C2SM-community. It is intended to provide an overview of the current status of C2SM software that can be used by C2SM members to make informed decisions about which model versions are the best fit for their current and future needs. This page is updated regularly, and also thoroughly checked for correctness at the beginning of every year.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>


## Supported software

For each piece of software, we list elements like software dependencies, target architecture, systems where it is supported, a contact email address or the procedure to obtain support.

[//]: # ( - ML - support here is also understood as how WE get support, not the C2SM users directly )

### ICON

TODO!
{: .label .label-red }

### COSMO

##### Description
{: .no_toc }

The most recent version of the COSMO weather and climate model. Active development of the software by the COSMO Consortium has stoped at the 6.0 version. This code version has been partially ported to gpu architecture using the stencil library Gridtools 2.0 for the dynamical core and OpenACC for the rest of the code. Not all features in the Fortran dynamical core are available in the Gridtools dycore. You will find a list of supported features at the [COSMO GitHub page](https://github.com/C2SM-RCM/cosmo/blob/master/dycore/doc/Dycore/supported_configuration.tex) (Note: this list is stored in the COSMO code repository, so this link requires Github access to the C2SM hosted COSMO code). Additionally, not all features of the COSMO model have been ported to gpu. The current status of the gpu porting for COSMO features is detailed in the following table.

<details close markdown="block">
<summary> gpu ported COSMO features </summary>

###### Parameters in `INPUT_ORG`
{: .no_toc }

| scheme/parameterization                       | namelist parameter                                                                                                                                                                  | GPU porting status                                 |
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
| Idealized runs                                | `lartif_data`                                                                                                                                                                       | not ported                                         |
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
| Initialize local variables                    | `linit_fields`                                                                                                                                                                      | not ported                                         |

###### Parameters in `INPUT_PHY`
{: .no_toc }

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

###### Parameters in `INPUT_DYN`
{: .no_toc }

The GPU porting of the dynamical core of COSMO was accomplished by rewriting the dynamics with the Gridtools stencil library. The Gridtools dycore supports a subset of the parameters of the COSMO Fortran dynamical core. The list of features currently supported in the Gridtools dycore can be found [here](https://github.com/C2SM-RCM/cosmo/blob/master/dycore/doc/Dycore/supported_configuration.tex) in the documentation in the code repository.

</details>


##### Target architecture
{: .no_toc }

cpu (without C++ dycore) and gpu

##### Dependencies
{: .no_toc }

* [Gridtools](.)
* [C++ Dycore (Gridtools 2.0)](.)
* [Serialbox](.)
* [Eccodes](.)
* Grib1 library

##### Support status
{: .no_toc }

actively supported
{: .label .label-green }

##### Supported branches
{: .no_toc }

`master` : Only the latest commit of the code is tested and supported.

`c2sm-features` : Only the latest commit of the code is tested and supported.

##### Supported systems
{: .no_toc }

Piz Daint (CSCS) and Euler (ETHZ).  The COSMO code is tested daily on Piz Daint using the Jenkins tool, as well as every time changes are made to the official source code. Euler does not yet have regular testing with Jenkins.

##### Contact person
{: .no_toc }

C2SM: C2SM-Support (support@c2sm.ethz.ch)

CSCS: Sam Omlin (samuel.omlin@cscs.ch)

##### Procedure to get support
{: .no_toc }

1. Reproduce bug in master branch, if not already there.
2. Contact C2SM contact person by email.  If C2SM contact person can’t resolve, they will escalate to CSCS through CSCS ticket. They then evaluate together and decide when to escalate to other experts (Gridtools/Dycore team, for example).

##### Procedure for planned maintenance at CSCS
{: .no_toc }

{: .note-title }

> Outdated
>
> This needs to be updated or even removed. The relevance is at a higher level now, more C2SM than COSMO only.


A team consisting of people from C2SM and MeteoSwiss will meet every 2-3 months to make sure COSMO-ORG is aligned with the current environment on Piz Daint (by upgrading the compiler version, etc.).

The C2SM-RCM COSMO repository includes a `master` branch, which remains aligned with the DWD bugfix releases of the code, and a `c2sm-features` branch, which contains any new features from further developments of C2SM members.  Both branches will be supported and tested regularly on Piz Daint with Jenkins. the `master` branch is regularly merged into the `c2sm-features` branch.

C2SM will be notified by CSCS at least one month before upgrades take place on Piz Daint. They will then proceed to compile COSMO and run the technical testsuite and a full-scale simulation on Dom, working with CSCS to resolve any issues that are encountered. If there is a serious issue with running COSMO on an upgraded system, then either the upgrade will be delayed until it can be resolved, or COSMO will be deployed into a container.
