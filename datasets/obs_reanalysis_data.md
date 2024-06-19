---
title: Observational and Re-analysis Datasets
layout: default
nav_order: 1
parent: Datasets
---

# Observational and Re-analysis Datasets
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
  - TOC
  {:toc}
</details>

{: .note-title }
File size information last updated in May 2022.

## "Raw" Archives (as downloaded from the original source)

### E-OBS
- Size: 660 GB
- Location: IAC
- Access: direct
- Status: different versions, updated irregularly
- Time period: 1950 - present
- Variables:
    - TG: mean temperature
    - TN: minimum temperature
    - TX: maximum temperature
    - RR: precipitation sum
    - PP: mean sea level pressure
    - FG: mean wind speed
    - HU: mean relative humidity
    - QQ: global radiation
- Temporal Resolution: daily
- Spatial Resolution: 0.1° and 0.25°
- More information: [E-OBS](https://www.ecad.eu/download/ensembles/download.php), [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-gridded-observations-europe?tab=overview)

### MERRA2
- Size: 15 TB
- Location: IAC
- Access: direct
- Status: updated
- Time period: 1980 - present
- Variables: many, temperature, precipitation, radiation, sea level pressure etc.
- Temporal Resolution: hourly, sst monthly
- Spatial Resolution: 0.5 lat x 0.625 lon (~50km)
- More information: [MERRA-2](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/), [Climate Data Guide](https://climatedataguide.ucar.edu/climate-data/nasas-merra2-reanalysis)

### ERAInterim
- Size: 5 TB
- Location: CSCS: `/store/c2sm/c2sme/reanalyses_dkrz/ERAInterim`
- Access: direct
- Status: static
- Time period: 1979-2019
- Variables: W_SO_REL, T_SO, W_SNOW, FR_LAND, T_SKIN, T_SNOW, FIS, T, U, V, QV, PS, QC, QI, FR_SEA_ICE
- Temporal Resolution: 6-hourly
- Spatial Resolution: 0.7° x 0.7° (80 km) global

### ERA5 (for ICON-CLM)
- Size: 50 TB
- Location: CSCS: `/store/c2sm/c2sme/reanalyses_dkrz/ERA5`
- Access: direct
- Status: updated
- Time period: 1979 - present
- Variables: FIS, FR_LAND, FR_SEA_ICE, PS, QC, QI, QR, QS, QV, T, T_SKIN, T_SNOW, T_SO, U, V, W_SNOW, W_SO_REL
- Temporal Resolution: hourly
- Spatial Resolution: 0.28125° x 0.28125° (31 km)
- More information: [ERA5 at CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview)

### ERA5
- Size: 17 TB
- Location: IAC: `/net/atmos/data/era5_cds/original`
- Access: direct
- Status: updated
- Time period: 1940 - present
- Variables: 2t, tp, 10si, mn2t, mx2t
- Temporal Resolution: monthly, hourly (variable dependent)
- Spatial Resolution: 0.25° x 0.25°

### ERA5-Land
- Size: 40 TB
- Location: IAC: `/net/atmos/data/era5-land_cds/original`
- Access: direct
- Status: updated
- Time period: 1950 - present
- Variables: 2t, snom
- Temporal Resolution: hourly (variable dependent)
- Spatial Resolution: 0.1° x 0.1°
- More information: [ERA5-Land](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)

### CERRA
- Size: 16 TB
- Location: IAC: `/net/atmos/data/cerra/original`
- Access: direct
- Status: updated
- Time period: 1985 - present
- Variables: 2t, t, r, ...
- Temporal Resolution: 3-hourly
- Spatial Resolution: 5 km x 5 km
- More information: sub-daily regional reanalysis data for Europe, [Wishlist](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp), [Download Status](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0)

### CERRA-Land
- Size: 12 TB
- Location: IAC: `/net/atmos/data/cerra-land/original`
- Access: direct
- Status: updated
- Time period: 1985 - present
- Variables: snom, sro, tp, ...
- Temporal Resolution: 3-hourly
- Spatial Resolution: 5 km x 5 km
- More information: [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview), [Wishlist](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp), [Download Status](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0)

## Processed Archives (e.g. aggregated or regridded)

### E-OBS and MCH
- Size: 50 GB
- Location: IAC: `/net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v23.1e/processed/, /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v26.0e/processed/`
- Access: direct
- Status: static
- Time period: 1971-2020
- Variables: tas, tasmax, tasmin, pr
- Temporal Resolution: daily
- Spatial Resolution: 0.11°
- More information: E-OBS (v23.1e and v26.0e) data with higher resolution MCH data over Switzerland (prepared for CH2025)

### MCH
- Size: 7 GB
- Location: IAC: `/net/co2/c2sm-data/ch202X/Obs_Data/MCH/processed/`
- Access: direct
- Status: static
- Time period: 1971-2021
- Variables: tas, tasmax, tasmin, pr
- Temporal Resolution: daily
- Spatial Resolution: ~2km
- More information: Gridded observational data from MeteoSwiss over Switzerland

### MERRA2
- Size: 17 GB
- Location: IAC: `/net/co2/c2sm-data/rlorenz/MERRA2/`
- Access: direct
- Status: updated
- Time period: v0: 1980-2015, v1: 1980-2018
- Variables: tas, tasmax, tasmin, huss, psl, pr, hfss, hfls, rlus, rlds, rsds, rsus, tos
- Temporal Resolution: daily, monthly
- Spatial Resolution: 2.5 lat x 2.5 lon (same as cmip6-ng)
- More information: Files are consistent with cmip-ng archives, no time period is indicated in filenames

### CERRA
- Size: 6 TB
- Location: IAC: `/net/atmos/data/cerra/processed/v1/`
- Access: direct
- Status: updated
- Time period: 1985-2020
- Variables: 2t, t, r, ...
- Temporal Resolution: daily, monthly
- Spatial Resolution: 5x5km
- More information: Sub-daily regional reanalysis data for Europe, [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-single-levels?tab=overview), [Status](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0)

### CERRA-Land
- Size: 1.8 TB
- Location: IAC: `/net/atmos/data/cerra-land/processed/v1/`
- Access: direct
- Status: updated
- Time period: 1985-2020
- Variables: snom, sro, tp, ...
- Temporal Resolution: daily, monthly
- Spatial Resolution: 5x5km
- More information: [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview), [Status](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0)

### ERA5
- Size: 500 GB
- Location: IAC: `/net/atmos/data/era5_cds/processed/`, Euler
- Access: direct
- Status: updated
- Time period: v1: 1940-present, v2: 1980-present
- Variables:
    - v1: 2t, tp, mx2t, mn2t
    - v2: `/net/atmos/data/era5_cds/processed/v2/`, [Variable list and progress](https://www.polybox.ethz.ch/index.php/s/5efYkkFrSVC64lZ)
- Temporal Resolution: daily, monthly
- Spatial Resolution: 0.25° x 0.25°
- More information: [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview)

### ERA5-Land
- Size: 2.2 TB
- Location: IAC: `/net/atmos/data/era5-land_cds/processed/v1/`
- Access: direct
- Status: updated
- Time period: 1950-present
- Variables: 2d, 2t, sd, snom
- Temporal Resolution: daily, monthly
- Spatial Resolution: 0.1° x 0.1°
- More information: [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)

