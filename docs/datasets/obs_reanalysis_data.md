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
- More information: sub-daily regional reanalysis data for Europe, [Wishlist :material-open-in-new:](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp){:target="_blank"}, [Download Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0){:target="_blank"}

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
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview){:target="_blank"}, [Wishlist :material-open-in-new:](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp){:target="_blank"}, [Download Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0){:target="_blank"}

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
- More information: [E-OBS :material-open-in-new:](https://www.ecad.eu/download/ensembles/download.php){:target="_blank"}, [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-gridded-observations-europe?tab=overview){:target="_blank"}

### ERAInterim

=== "CSCS"
    ```console
    /store/c2sm/c2sme/reanalyses_dkrz/ERAInterim
    ```

- Size: 5 TB
- Access: direct
- Status: static
- Time period: 1979-2019
- Variables: `FIS`, `FR_LAND`, `FR_SEA_ICE`, `PS`, `QC`, `QI`, `QV`, `T`, `T_SKIN`, `T_SNOW`, `T_SO`, `U`, `V`, `W_SNOW`, `W_SO_REL`
- Temporal Resolution: 6-hourly
- Spatial Resolution: 0.7° x 0.7° (80 km) global

### ERA5 (for ICON-CLM)

=== "CSCS"
    ```console
    /store/c2sm/c2sme/reanalyses_dkrz/ERA5
    ```

- Size: 50 TB
- Access: direct
- Status: updated
- Time period: 1979 - present
- Variables: `FIS`, `FR_LAND`, `FR_SEA_ICE`, `PS`, `QC`, `QI`, `QR`, `QS`, `QV`, `T`, `T_SKIN`, `T_SNOW`, `T_SO`, `U`, `V`, `W_SNOW`, `W_SO_REL`
- Temporal Resolution: hourly
- Spatial Resolution: 0.28125° x 0.28125° (31 km)
- More information: [ERA5 at CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview){:target="_blank"}

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
- More information: [ERA5-Land :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form){:target="_blank"}

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

- Size: 6 TB
- Access: direct
- Status: updated
- Time period: 1985-2020
- Variables: `2t`, `r`, `t`, ...
- Temporal Resolution: daily, monthly
- Spatial Resolution: 5x5km
- More information: Sub-daily regional reanalysis data for Europe, [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-single-levels?tab=overview){:target="_blank"}, [Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0){:target="_blank"}

### CERRA-Land

=== "IAC"
    ```console
    /net/atmos/data/cerra-land/processed/v1/
    ```

- Location: IAC: `/net/atmos/data/cerra-land/processed/v1/`
- Size: 1.8 TB
- Access: direct
- Status: updated
- Time period: 1985-2020
- Variables: `sro`, `snom`, `tp`, ...
- Temporal Resolution: daily, monthly
- Spatial Resolution: 5x5km
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview){:target="_blank"}, [Status :material-open-in-new:](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0){:target="_blank"}

### E-OBS and MCH

=== "IAC"
    ```console
    /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v23.1e/processed/
    /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v26.0e/processed/
    ```

- Size: 50 GB
- Access: direct
- Status: static
- Time period: 1971-2020
- Variables: `pr`, `tas`, `tasmax`, `tasmin`
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
    /net/atmos/data/era5_cds/processed/
    ```

- Size: 500 GB
- Access: direct
- Status: updated
- Time period: v1: 1940-present, v2: 1980-present
- Variables:
    - v1: `2t`, `mn2t`, `mx2t`, `tp`
- v2: [Variable list and progress :material-open-in-new:](https://www.polybox.ethz.ch/index.php/s/5efYkkFrSVC64lZ){:target="_blank"}
- Temporal Resolution: daily, monthly
- Spatial Resolution: 0.25° x 0.25°
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview){:target="_blank"}

### ERA5-Land

=== "IAC"
    ```console
    /net/atmos/data/era5-land_cds/processed/v1/
    ```

- Size: 2.2 TB
- Access: direct
- Status: updated
- Time period: 1950-present
- Variables: `2d`, `2t`, `sd`, `snom`
- Temporal Resolution: daily, monthly
- Spatial Resolution: 0.1° x 0.1°
- More information: [CDS :material-open-in-new:](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form){:target="_blank"}

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
