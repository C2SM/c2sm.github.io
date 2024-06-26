---
title: Climate Model Data
layout: default
nav_order: 1
parent: Datasets
---

# Climate Model Data
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
  - TOC
  {:toc}
</details>


## "Raw" CMIP archives (as downloaded from ESGF)

{: .note-title }

"Resolution: native" means that each model output is available on the native grid on which it was run. Size and file information last updated in June 2021.

### CMIP2
- Size: 0.01 TB 
- Number of files: 500
- Location: IAC
- Access: direct / rsync
- Status: frozen (2010-10)
- Resolution: native

### CMIP3
- Size: 6 TB
- Number of files: 40’000
- Location: IAC
- Access: direct / rsync
- Status: frozen (2016-12)
- Resolution: native

### CMIP5
- Size: 130 TB
- Number of files: 700’000
- Location: IAC
- Access: direct / rsync
- Status: monthly updated
- Resolution: native

### CMIP6
- Size: 520 TB 
- Number of Files: 5’500’000
- Location: IAC, Euler: `/nfs/atmos/c2sm`
- Access: direct / rsync
- Status: weekly updated
- Resolution: native

## CMIP next generation (checked, standardized, regridded to common grid)

{: .note-title }

Next Generation (ng) archives were maintained by Reto’s group (Jan Sedlacek/Lukas Brunner). Ruth Lorenz / C2SM took over cmip6-ng in 2022. Contact: [cmip6-archive@env.ethz.ch](mailto:cmip6-archive@env.ethz.ch). Documentation: [https://doi.org/10.5281/zenodo.373412](https://doi.org/10.5281/zenodo.3734128).

### CMIP3-ng
- Size: 0.5 TB
- Number of files: 5’000
- Location: IAC
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
- Resolution: native and 2.5°x2.5°

### CMIP5-ng
- Size: 33 TB
- Number of files: 100’000
- Location: IAC
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
- Resolution: native and 2.5° x 2.5°

### CMIP6-ng
- Size: 175 TB
- Number of files: 500’000
- Location: IAC, Euler: `/nfs/atmos/c2sm`
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
    - monthly: `areacella`, `clt`, `co2mass`, `evspsbl`, `evspsblsoi`, `evspsblveg`, `gpp`, `hfds`, `hfss`, `hfls`, `hurs`, `huss`, `lai`, `mrsol`, `mrsos`, `mrro`, `mrros`, `mrso`, `npp`, `nbp`, `pr`, `prw`, `ra`, `rh`, `rlus`, `rlut`, `rlutcs`, `rlds`, `rldscs`, `rsds`, `rsdscs`, `rsus`, `rsuscs`, `rsut`, `rsutcs`, `rtmt`, `sftlf`, `siconc`, `tas`, `tasmax`, `tasmin`, `tos`, `tran`, `treeFrac`, `zg500`, `zos`
    - daily: `mrro`, `pr`, `tas`, `tasmax`, `tasmin`, `zg500`
- Resolution: native and 2.5° x 2.5°

## "Raw" CORDEX (as downloaded)

### CORDEX
- Size: 370 TB
- Number of files: 800’000
- Location: IAC, Euler: `/nfs/atmos/c2sm`, CSCS: `/store/c2sm/c2sme`
- Access: direct / rsync
- Status: monthly updated
- Resolution: 0.44° and 0.11°

### CORDEX-ReKliEs
- Size: 23 TB
- Number of files: 100’000
- Location: IAC, Euler
- Access: direct
- Status: monthly updated
- Resolution: 0.11°

## CORDEX data for climate scenarios (checked, regridded to identical grids if necessary)

### CORDEX.ch2018
- Size: 11 TB
- Number of files: 1’800
- Location: IAC, CSCS
- Access: direct
- Status: frozen (2019-04)
- Variables:
    - daily: `hurs`, `huss`, `pr`, `rsds`, `sfcWind`, `sfcWindmax`, `snw`, `tas`, `tasmax`, `tasmin`
- Resolution: 0.44° and 0.11°

### CORDEX.ch2025
- Size: 46 TB 
- Number of files: 3’500
- Location: IAC: `/net/ch4/data/cordex.ch2025/`
- Access: direct
- Status: ongoing
- Variables: 
    - daily: `pr`, `tas`, `tasmax`, `tasmin`, `zg500`
- Resolution: 0.44° and 0.11°

### CORDEX-FPSCONV
- Size: 30 TB
- Number of files: 22'949
- Location: CSCS: `/store/c2sm/c2sme/CH202X/CORDEX-FPSCONV/ALP-3/`, IAC: `/net/krypton/hyclimm_nobackup/CORDEX-FPSCONV/ALP-3/`
- Access: direct / rsync
- Status: ongoing
- Variables:
    - 1hr: `pr`, `tas`
    - daily: `pr`, `tas`, `tasmax`, `tasmin`
- Resolution: 2-3 km
