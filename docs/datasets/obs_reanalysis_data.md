# Observational and Re-analysis Datasets

!!! note
    File size information last updated in May 2022.

## Raw Archives

!!! info
    Dataset available as downloaded from the original source.

### CERRA

=== "IAC"
    ```console
    /net/atmos/data/cerra/original
    ```

- Size: 16 TB
- Access: direct
- Status: updated
- Time period: 1985 - present
- Variables: `2t`, `t`, `r`, ...
- Temporal Resolution: 3-hourly
- Spatial Resolution: 5 km x 5 km
- More information: sub-daily regional reanalysis data for Europe, [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-single-levels?tab=overview){:target="_blank"},  [Wishlist :material-open-in-new:](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp){:target="_blank"}, [Download Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0){:target="_blank"}

### CERRA-Land

=== "IAC"
    ```console
    /net/atmos/data/cerra-land/original
    ```

- Size: 12 TB
- Access: direct
- Status: updated
- Time period: 1985 - present
- Variables: `snom`, `sro`, `tp`, ...
- Temporal Resolution: 3-hourly
- Spatial Resolution: 5 km x 5 km
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-land?tab=overview){:target="_blank"}, [Wishlist :material-open-in-new:](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp){:target="_blank"}, [Download Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0){:target="_blank"}

### E-OBS

=== "IAC"
    ```console
    /net/atmos/data/E-OBS
    ```

- Size: 660 GB
- Access: direct
- Status: different versions, updated irregularly
- Time period: 1950 - present
- Variables:
    - `TG`: mean temperature
    - `TN`: minimum temperature
    - `TX`: maximum temperature
    - `RR`: precipitation sum
    - `PP`: mean sea level pressure
    - `FG`: mean wind speed
    - `HU`: mean relative humidity
    - `QQ`: global radiation
- Temporal Resolution: daily
- Spatial Resolution: 0.1° and 0.25°
- More information: [E-OBS :material-open-in-new:](https://www.ecad.eu/download/ensembles/download.php){:target="_blank"}, [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/insitu-gridded-observations-europe?tab=overview){:target="_blank"}

### ERAInterim

=== "Santis"
    ```console
    /capstor/store/cscs/c2sm/c2sme/reanalyses_dkrz/ERAInterim
    ```

=== "Balfrin"
    ```console
    /capstor/store/cscs/c2sm/c2sme/reanalyses_dkrz/ERAInterim
    ```    

- Size: 5 TB
- Access: direct
- Status: static
- Time period: 1979-2019
- Variables: `FIS`, `FR_LAND`, `FR_SEA_ICE`, `PS`, `QC`, `QI`, `QV`, `T`, `T_SKIN`, `T_SNOW`, `T_SO`, `U`, `V`, `W_SNOW`, `W_SO_REL`
- Temporal Resolution: 6-hourly
- Spatial Resolution: 0.7° x 0.7° (80 km) global

### ERA5 (for ICON-CLM)

=== "Santis"
    ```console
    /capstor/store/cscs/c2sm/c2sme/reanalyses_dkrz/ERA5
    ```

=== "Balfrin"
    ```console
    /capstor/store/cscs/c2sm/c2sme/reanalyses_dkrz/ERA5
    ```    

- Size: 100 TB (last updated: 2025-01-31)
- Number of files: 22'035 (last updated: 2025-01-31)
- Access: direct
- Status: updated
- Time period: 1940-01 - 2024-08
- Variables: `FIS`, `FR_LAND`, `FR_SEA_ICE`, `PS`, `QC`, `QI`, `QR`, `QS`, `QV`, `T`, `T_SKIN`, `T_SNOW`, `T_SO`, `U`, `V`, `W_SNOW`, `W_SO_REL`
- Temporal Resolution: hourly
- Spatial Resolution: 0.28125° x 0.28125° (31 km)
- Vertical levels: [40 - 137 :material-open-in-new:](https://confluence.ecmwf.int/display/UDOC/L137+model+level+definitions){:target="_blank"}
- More information: [ERA5 at CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview){:target="_blank"}

### ERA5

=== "IAC"
    ```console
    /net/atmos/data/era5_cds/original
    ```

- Size: 17 TB
- Access: direct
- Status: updated
- Time period: 1940 - present
- Variables: `2t`, `tp`, `10si`, `mn2t`, `mx2t`
- Temporal Resolution: monthly, hourly (variable dependent)
- Spatial Resolution: 0.25° x 0.25°

### ERA5-Land

=== "IAC"
    ```console
    /net/atmos/data/era5-land_cds/original
    ```

- Size: 40 TB
- Access: direct
- Status: updated
- Time period: 1950 - present
- Variables: `2t`, `snom`
- Temporal Resolution: hourly (variable dependent)
- Spatial Resolution: 0.1° x 0.1°
- More information: [ERA5-Land :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=form){:target="_blank"}

### MERRA2

=== "IAC"
    ```console
    /net/atmos/data/MERRA2
    ```

- Location: IAC
- Size: 15 TB
- Access: direct
- Status: updated
- Time period: 1980 - present
- Variables: many, temperature, precipitation, radiation, sea level pressure etc.
- Temporal Resolution: hourly, sst monthly
- Spatial Resolution: 0.5 lat x 0.625 lon (~50km)
- More information: [MERRA-2 :material-open-in-new:](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/){:target="_blank"}, [Climate Data Guide :material-open-in-new:](https://climatedataguide.ucar.edu/climate-data/nasas-merra2-reanalysis){:target="_blank"}


## Processed Archives

!!! info
    Datasets are aggregated or regridded.

### CERRA

=== "IAC"
    ```console
    /net/atmos/data/cerra/processed/v1/
    ```

- Size: 7.77 TB :material-information-outline:{ title="last updated: 2025-04-13 01:45:12" }
- Number of files: 1,898 :material-information-outline:{ title="last updated: 2025-04-13 01:45:12" }
- Access: direct
- Status: updated
- Time period: 1985-2020
- Variables: 
  `10si`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `10wdir`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `2r`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `2t`{ title="day (native): 1985-2021, mon (native): 1985-2021" },
  `eva`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `gph500`{ title="day (native): 1986-2020, mon (native): 1986-2020" },
  `liqvsm`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `mn2t`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `mx2t`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `r`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sd`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sde`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sf`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `skt`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `slhf`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sp`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sshf`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `ssr`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `ssrd`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `str`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `strd`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `t`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `tcc`{ title="day (native): 1985-2021, mon (native): 1985-2021" },
  `u`{ title="day (native): 1986-2020, mon (native): 1986-2020" },
  `v`{ title="day (native): 1986-2020, mon (native): 1986-2020" },
  `vsw`{ title="day (native): 1985-2020, mon (native): 1985-2020" }
- Temporal Resolution: daily, monthly
- Spatial Resolution: 5x5km
- More information: Sub-daily regional reanalysis data for Europe, [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-single-levels?tab=overview){:target="_blank"}, [Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0){:target="_blank"}

### CERRA-Land

=== "IAC"
    ```console
    /net/atmos/data/cerra-land/processed/v1/
    ```

- Size: 1.82 TB :material-information-outline:{ title="last updated: 2025-04-13 01:45:12" }
- Number of files: 1,060 :material-information-outline:{ title="last updated: 2025-04-13 01:45:12" }
- Access: direct
- Status: updated
- Time period: 1985-2020
- Variables: 
  `eva`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `perc`{ title="day (native): 1985-2006, mon (native): 1985-2006" },
  `sd`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `skt`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `slhf`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `snom`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sro`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `sshf`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `ssr`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `ssrd`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `str`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `strd`{ title="day (native): 1985-2020, mon (native): 1985-2020" },
  `tcc`{ title="day (native): N/A, mon (native): N/A" },
  `tp`{ title="mon (native): 1985-2020" },
  `vsw`{ title="day (native): 1985-2020, mon (native): 1985-2020" }
- Temporal Resolution: daily, monthly
- Spatial Resolution: 5x5km
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-cerra-land?tab=overview){:target="_blank"}, [Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0){:target="_blank"}

### E-OBS and MCH

=== "IAC"
    ```console
    /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v23.1e/processed/
    /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v26.0e/processed/
    ```

- Size: 141 GB
- Number of files: 12
- Access: direct
- Status: static
- Time period: 1971-2020
- Variables: 
    - v23.1e: `CDD`, `TXx`, `pr`, `tas`, `tasmax`, `tasmin`
    - v26.0e: `pr`, `tas`, `tasmax`, `tasmin`
- Temporal Resolution: daily
- Spatial Resolution: 0.11°
- More information: E-OBS (v23.1e and v26.0e) data with higher resolution MCH data over Switzerland (prepared for CH2025)

### ERA5

=== "IAC"
    ```console
    /net/atmos/data/era5_cds/processed/
    ```
=== "Euler"
    ```console
    /nfs/atmos/c2sm/era5/processed/
    ```

- Size: 45.93 TB :material-information-outline:{ title="last updated: 2025-04-13 01:46:10" }
- Number of files: 139,817 :material-information-outline:{ title="last updated: 2025-04-13 01:46:10" }
- Access: direct
- Status: updated
- Time period: v1: 1940-2022, v2: 1980-2023, v3: 1940-present
- Variables: 
  `cbh`{ title="day (native): 194001-202412, mon (native): 194001-202412" },
  `cl`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `clt`{ title="day (native): 198001-202312, mon (native): 194012-202410" },
  `d2m`{ title="day (native): 194001-202412, mon (native): 194012-202412" },
  `hur`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `hurs`{ title="day (native): 194001-202312, mon (native): 198001-198512" },
  `orog`{ title="fx (native): N/A" },
  `pr`{ title="day (native): 194001-202406, mon (native): 194012-202406" },
  `ps`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `psl`{ title="day (05x05): 195001-202212, mon (05x05): 195001-202212" },
  `rlds`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `rls`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `rsds`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `sfcWind`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `sftlf`{ title="fx (native): N/A" },
  `strd`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `ta`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `tas`{ title="day (native): 194001-202405, mon (native): 194001-202405" },
  `tasmax`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `tasmin`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `tos`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `ua`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `uas`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `va`{ title="day (native): 194001-202312, mon (native): 194001-202312" },
  `vas`{ title="day (native): 194001-202312, mon (native): 194012-202312" },
  `zg`{ title="day (native): 194001-202312, mon (native): 194001-202312" }
- [Variable list and progress :material-open-in-new:](https://www.polybox.ethz.ch/index.php/s/5efYkkFrSVC64lZ){:target="_blank"}
- v2: variable names and units are standardized to CMIP. Inconsistency in clt, clt is provided as fraction (as original ERA5) not % (as supposed to be in CMIP)
- v3: variable names and units are standardized to CMIP (incl. clt)
- Temporal Resolution: daily, monthly
- Spatial Resolution: 0.25° x 0.25°
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview){:target="_blank"}

### ERA5-Land

=== "IAC"
    ```console
    /net/atmos/data/era5-land_cds/processed/v1/
    ```

- Size: 7.61 TB :material-information-outline:{ title="last updated: 2025-04-13 01:45:16" }
- Number of files: 1,722 :material-information-outline:{ title="last updated: 2025-04-13 01:45:16" }
- Access: direct
- Status: updated
- Time period: 1950-present
- Variables: 
  `2d`{ title="day (native): 2000-2022, mon (native): 2000-2022" },
  `2t`{ title="day (native): 1950-2022, mon (native): 1950-2022" },
  `e`{ title="day (native): 1950-2022, mon (native): 1950-2022" },
  `pev`{ title="day (native): 1950-2022, mon (native): 1950-2022" },
  `sd`{ title="day (native): 1950-2022, mon (native): 1950-2022" },
  `snom`{ title="day (native): 1950-2022, mon (native): 1950-2022" },
  `ssrd`{ title="day (native): 1971-2024, mon (native): 1971-2024" },
  `strd`{ title="day (native): 1970-2024, mon (native): 1970-2024" },
  `swvl1`{ title="day (native): 1950-2022, mon (native): 1950-2022" },
  `swvl2`{ title="day (native): 1959-2022, mon (native): 1959-2022" },
  `swvl3`{ title="day (native): 1950-2023, mon (native): 1950-2023" },
  `swvl4`{ title="day (native): 1950-2023, mon (native): 1950-2023" },
  `tp`{ title="day (native): 1950-2022, mon (native): 1950-2022" }
- Temporal Resolution: daily, monthly
- Spatial Resolution: 0.1° x 0.1°
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=form){:target="_blank"}

### MERRA2

=== "IAC"
    ```console
    /net/co2/c2sm-data/rlorenz/MERRA2/
    ```

- Size: 17 GB
- Access: direct
- Status: updated
- Time period: v0: 1980-2015, v1: 1980-2018
- Variables: `tas`, `tasmax`, `tasmin`, `huss`, `psl`, `pr`, `hfss`, `hfls`, `rlus`, `rlds`, `rsds`, `rsus`, `tos`
- Temporal Resolution: daily, monthly
- Spatial Resolution: 2.5 lat x 2.5 lon (same as cmip6-ng)
- More information: Files are consistent with cmip-ng archives, no time period is indicated in filenames

### MCH

=== "IAC"
    ```console
    /net/co2/c2sm-data/ch202X/Obs_Data/MCH/processed/
    ```

- Size: 7 GB
- Access: direct
- Status: static
- Time period: 1971-2021
- Variables: `tas`, `tasmax`, `tasmin`, `pr`
- Temporal Resolution: daily
- Spatial Resolution: ~2km
- More information: Gridded observational data from MeteoSwiss over Switzerland
