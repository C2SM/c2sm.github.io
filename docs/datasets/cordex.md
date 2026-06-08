## Raw CORDEX (primary)

!!! info
    The data is available as downloaded.

### CORDEX

=== "IAC"
    ```console
    /net/atmos/data/cordex
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm/cordex
    ```
=== "Santis"
    ```console
    /capstor/store/cscs/c2sm/c2sme/cordex
    ```

- Size: 356.98 TB :material-information-outline:{ title="last updated: 2026-05-31 01:47:21" }
- Number of files: 552,596 :material-information-outline:{ title="last updated: 2026-05-31 01:47:21" }
- Access: direct / rsync
- Status: monthly updated
- Resolution: 0.44° and 0.11°
- Coverage: Europe

### CORDEX-ReKliEs

=== "IAC"
    ```console
    /net/atmos/data/cordex-reklies
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm/cordex-reklies
    ```

- Size: 22.41 TB :material-information-outline:{ title="last updated: 2026-05-31 01:45:25" }
- Number of files: 94,936 :material-information-outline:{ title="last updated: 2026-05-31 01:45:25" }
- Access: direct
- Status: monthly updated
- Resolution: 0.11°
- Coverage: Europe

## CORDEX Data for Climate Scenarios (derived)

!!! info
    The data is checked, and regridded to identical grids if necessary.

### CORDEX.ch2018

=== "IAC"
    ```console
    /net/ch4/data/cordex.ch2018-freeze-2.1
    ```
=== "Santis"
    ```console
    /capstor/store/cscs/c2sm/c2sme/cordex.ch2018-freeze-2.1
    ```

- Size: 11 TB
- Number of files: 1.800
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
- Coverage: Europe

### CORDEX.ch2025

=== "IAC"
    ```console
    /net/ch4/data/cordex.ch2025/
    ```

- Size: 46 TB
- Number of files: 3.500
- Access: direct
- Status: frozen (2025-11)
- Variables:
    - daily: `pr`, `tas`, `tasmax`, `tasmin`, `hurs`, `rsds`, `sfcWind`, `zg500`, `evspsbl`, `ta500`, `ta850`
- Resolution: 0.11°
- Coverage: Europe
- [List with issues on polybox :material-open-in-new:](https://www.polybox.ethz.ch/index.php/s/RQQrUnRPlg86Apx){:target="_blank"}

### CORDEX-FPSCONV

=== "IAC"
    ```console
    /net/krypton/hyclimm_nobackup/CORDEX-FPSCONV/ALP-3/
    ```
=== "Santis"
    ```console
    /capstor/store/cscs/c2sm/c2sme/CH202X/CORDEX-FPSCONV/ALP-3/
    ```

- Size: 30 TB
- Number of files: 22.949
- Access: direct / rsync
- Status: frozen (2023-12)
- Variables:
    - 1hr: `pr`, `tas`
    - daily: `pr`, `tas`, `tasmax`, `tasmin`
- Resolution: 2-3 km
- Coverage: European Alpine domain

