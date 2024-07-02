# Climate Model Data

## Raw CMIP Archives

!!! info
    The data is available as downloaded from ESGF.

!!! note
    "Resolution: native" means that each model output is available on the native grid on which it was run. Size and file information last updated in June 2021.

### CMIP2

- Location: IAC
- Size: 0.01 TB 
- Number of files: 500
- Access: direct / rsync
- Status: frozen (2010-10)
- Resolution: native

### CMIP3

- Location: IAC
- Size: 6 TB
- Number of files: 40’000
- Access: direct / rsync
- Status: frozen (2016-12)
- Resolution: native

### CMIP5

- Location: IAC
- Size: 130 TB
- Number of files: 700’000
- Access: direct / rsync
- Status: monthly updated
- Resolution: native

### CMIP6

=== "IAC"
    ```console
    /nfs/atmos/c2sm
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm
    ```

- Size: 520 TB 
- Number of Files: 5’500’000
- Access: direct / rsync
- Status: weekly updated
- Resolution: native

## CMIP Next Generation

!!! info
    The datasets are checked, standardized, and regridded to common grid.

!!! note
    Next Generation (ng) archives were maintained by Reto’s group (Jan Sedlacek/Lukas Brunner). Ruth Lorenz / C2SM took over cmip6-ng in 2022. Contact: [cmip6-archive@env.ethz.ch](mailto:cmip6-archive@env.ethz.ch). Documentation: [https://doi.org/10.5281/zenodo.373412 :material-open-in-new:](https://doi.org/10.5281/zenodo.3734128){:target="_blank"}.

### CMIP3-ng

- Location: IAC
- Size: 0.5 TB
- Number of files: 5’000
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
- Resolution: native and 2.5°x2.5°

### CMIP5-ng

- Location: IAC
- Size: 33 TB
- Number of files: 100’000
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: n/a
- Resolution: native and 2.5° x 2.5°

### CMIP6-ng

=== "IAC"
    ```console
    /nfs/atmos/c2sm
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm
    ```

- Size: 175 TB
- Number of files: 500’000
- Access: direct / rsync
- Status: frozen (2019-03)
- Variables: 
  `areacella`{ title="fx (native)" },
  `clt`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `co2mass`{ title="mon (native)" },
  `evspsbl`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `evspsblsoi`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `evspsblveg`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `gpp`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hfds`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hfls`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hfss`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `hurs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `huss`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `lai`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `masks`{ title="fx (native)" },
  `mrro`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `mrros`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrso`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrsol`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `mrsos`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `nbp`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `npp`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `pr`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `prw`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `ps`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `psl`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `ra`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rh`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlds`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rldscs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlus`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlut`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rlutcs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsds`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsdscs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsdt`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsus`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsuscs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsut`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rsutcs`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `rtmt`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `sfcWind`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `sftlf`{ title="fx (native)" },
  `siconc`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `ta`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tas`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `tasmax`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `tasmin`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `tauu`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tauv`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tos`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tran`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `treeFrac`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `tsl`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `uas`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `vas`{ title="ann (g025), ann (native), mon (g025), mon (native)" },
  `zg500`{ title="ann (g025), ann (native), day (g025), day (native), mon (g025), mon (native)" },
  `zos`{ title="ann (g025), ann (native), mon (g025), mon (native)" }
- Resolution: native and 2.5° x 2.5°

## Raw CORDEX

!!! info
    The data is available as downloaded.

### CORDEX

=== "IAC"
    ```console
    /nfs/atmos/c2sm
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm
    ```
=== "CSCS"
    ```console
    /store/c2sm/c2sme
    ```

- Size: 370 TB
- Number of files: 800’000
- Access: direct / rsync
- Status: monthly updated
- Resolution: 0.44° and 0.11°

### CORDEX-ReKliEs

- Location: IAC, Euler
- Size: 23 TB
- Number of files: 100’000
- Access: direct
- Status: monthly updated
- Resolution: 0.11°

## CORDEX Data for Climate Scenarios

!!! info
    The data is checked, and regridded to identical grids if necessary.

### CORDEX.ch2018

- Location: IAC, CSCS
- Size: 11 TB
- Number of files: 1’800
- Access: direct
- Status: frozen (2019-04)
- Variables: 
  `hfls`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `hfss`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `hurs`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `huss`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `pr`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `prc`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `ps`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `psl`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day — rcp85: 3hr, day, mon, sem" },
  `rlds`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `rlus`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `rsds`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `rsus`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `sfcWind`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `sund`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `tas`{ title="historical: 3hr, day, mon, sem — rcp26: 3hr, day, mon, sem — rcp85: 3hr, day, mon, sem" },
  `evspsbl`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `hus850`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `mrro`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `mrso`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `rlut`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `rsdt`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `rsut`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `snd`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `snw`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `ta200`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `ta500`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `ta850`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `ts`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `ua500`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `ua850`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `uas`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `va500`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `va850`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `vas`{ title="historical: 6hr, day, mon, sem — rcp26: 6hr, day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `zg500`{ title="historical: 6hr, day, mon, sem — rcp26: day, mon, sem — rcp85: 6hr, day, mon, sem" },
  `clt`{ title="historical: day, mon, sem — rcp26: day — rcp85: day, mon, sem" },
  `prhmax`{ title="historical: day — rcp85: day" },
  `prsn`{ title="historical: day, mon, sem — rcp26: day, mon, sem — rcp85: day, mon, sem" },
  `sfcWindmax`{ title="historical: day, mon, sem — rcp26: day, mon, sem — rcp85: day, mon, sem" },
  `snc`{ title="historical: day, mon, sem — rcp26: day, mon, sem — rcp85: day, mon, sem" },
  `tasmax`{ title="historical: day, mon, sem — rcp26: day, mon, sem — rcp85: day, mon, sem" },
  `tasmin`{ title="historical: day, mon, sem — rcp26: day, mon, sem — rcp85: day, mon, sem" },
  `wsgsmax`{ title="historical: day — rcp26: day — rcp85: day" },
  `orog`{ title="historical: fx — rcp26: fx — rcp85: fx" },
  `sftlf`{ title="historical: fx — rcp26: fx — rcp85: fx" }
- Resolution: 0.44° and 0.11°

### CORDEX.ch2025

=== "IAC"
    ```console
    /net/ch4/data/cordex.ch2025/
    ```

- Size: 46 TB 
- Number of files: 3’500
- Access: direct
- Status: ongoing
- Variables: 
    - daily: `pr`, `tas`, `tasmax`, `tasmin`, `zg500`
- Resolution: 0.44° and 0.11°

### CORDEX-FPSCONV

=== "IAC"
    ```console
    /net/krypton/hyclimm_nobackup/CORDEX-FPSCONV/ALP-3/
    ```
=== "CSCS"
    ```console
    /store/c2sm/c2sme/CH202X/CORDEX-FPSCONV/ALP-3/
    ```

- Size: 30 TB
- Number of files: 22'949
- Access: direct / rsync
- Status: ongoing
- Variables:
    - 1hr: `pr`, `tas`
    - daily: `pr`, `tas`, `tasmax`, `tasmin`
- Resolution: 2-3 km