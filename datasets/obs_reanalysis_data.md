---
title: Observational and Re-analysis Datasets
layout: default
nav_order: 1
parent: Datasets
---

# Observational and Re-analysis Datasets

## "Raw" Archives (as downloaded from original source) 	  	  	  	  	  	  	  	  	 

| Archive 	 | Size (1) |	Location |	Access 	| Status 	                                | time period 	 | Variables 	| Temporal Resolution 	| Spatial Resolution 	| more information |
| -----------|----------|----------|----------|-----------------------------------------|----------------|-------------|-----------------------|---------------------|-------------------|
| E-OBS 	   |  660G 	  | IAC 	   | direct 	| different versions, updated irregularly | 1950 - present | TG: mean temperature, TN: minimum temperature, TX: maximum temperature, RR: precipitation sum, PP: mean sea level pressure, FG: mean wind speed, HU: mean relative humidity, QQ: global radiation |	daily |	0.1° and 0.25° |	https://www.ecad.eu/download/ensembles/download.php https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-gridded-observations-europe?tab=overview |
| MERRA2 	   | 15T      |	IAC      | direct   |	updated |	1980 - present |	many, temperature, precipitation, radiation, sea level pressure etc. | hourly, sst monthly | 	0.5 lat x 0.625 lon (~50km) |	https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/ https://climatedataguide.ucar.edu/climate-data/nasas-merra2-reanalysis
| ERAInterim | 5T       | CSCS (2) | direct   |	static |	1979-2019      |	W_SO_REL, T_SO, W_SNOW, FR_LAND, T_SKIN, T_SNOW, FIS, T, U, V, QV, PS, QC, QI, FR_SEA_ICE |	6-hourly |	0.7° x 0.7° (80 km) 	global
| ERA5       | 50T      |	CSCS (3) | direct   | updated |1979 - present  |	FIS, FR_LAND, FR_SEA_ICE, PS, QC, QI, QR, QS, QV, T, T_SKIN, T_SNOW, T_SO, U, V, W_SNOW, W_SO_REL |	hourly |	0.28125° x 0.28125° (31 km) 	List of additional ERA-5 datasets
| ERA5       | 17T      |	IAC (4)  |	direct  |	updated |	1940 - present |	2t, tp, 10si, mn2t, mx2t |	monthly, hourly (variable dependent)| 0.25° x 0.25° |	https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview, https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview, need to delete original data after processing because of size |
| ERA5-Land  | 40T      |	IAC (5)  |	direct  |	updated |	1950 - present |	2t, snom |	hourly (variable dependent) |	0.1° x 0.1° | 	https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form, need to delete original data after processing because of size |
| CERRA      | 16T      |	IAC (6)  |	direct  |	updated |	1985 - present |	2t, t, r, ... | 	3-hourly | 	5x5km |	sub-daily regional reanalysis data for Europe, https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-single-levels?tab=overview Wishlist: https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp, download status: https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0, space constraints prevent us from keeping all the 3-hourly data which have been processed into daily data, see sheet on download process |
| CERRA-Land | 12T      | IAC (7)  | direct   |	updated |	1985 - present |	snom, sro, tp, ... |	3-hourly |	5x5km |	https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview, Wishlist: https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp, download status: https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0, space constraints prevent us from keeping all the 3-hourly data which have been processed into daily data, see sheet on download process |

## Processed Archives (e.g. aggregated or regridded) 	 

| Archive 	 | Size (1) |	Location |	Access | Status  | time period 	 | Variables 	              | Temporal Resolution | Spatial Resolution 	| more information |
| -----------|----------|----------|---------|---------|---------------|--------------------------|---------------------|---------------------|-------------------|
| E-OBS and MCH |	50G 	| IAC (8)  |	direct |	static |	1971-2020    |	tas, tasmax, tasmin, pr |	daily               |	0.11°               |	E-OBS (v23.1e and v26.0e) data with higher resolution MCH data over Switzerland (prepared for CH2025) |
| MCH 	     | 7G       |	IAC (9)  |	direct |	static |	1971-2021 	 | tas, tasmax, tasmin, pr  |	daily               |	~2km                |	gridded observational data from MeteoSwiss over Switzerland |
| MERRA2     |	17G     |	IAC (10) |	direct | updated | 1980-2015 (v0), 1980-2018 (v1) |	tas, tasmax, tasmin, huss, psl, pr, hfss, hfls, rlus, rlds, rsds, rsus, tos |	daily, monthly |	2.5 lat x 2.5 lon (same as cmip6-ng) 	files are consistent with cmip-ng archives, no time period is indicated in filenames |
| CERRA 	   |6T 	      | IAC (11) |	direct | updated | 1985 - 2020 (v1) |	2t, t, r, ...       |	daily, monthly      |	5x5km 	            | sub-daily regional reanalysis data for Europe, https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-single-levels?tab=overview, https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0 |
| CERRA-Land |	1.8T    |	IAC (12) |	direct | updated | 1985 - 2020 (v1) |	snom, sro, tp, ...  |	daily, monthly      |	5x5km 	| https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview, https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0 |
| ERA5 	     | 500G     |	IAC (13) | 	direct | updated | 1940 - present |	2t, tp, mx2t, mn2t |	daily, monthly |	0.25° x 0.25° |	https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview |
| ERA5-Land  |	2.2T    |	IAC (14) |	direct | updated | 1950 - present |	2d, 2t, sd, snom |	daily, monthly |	0.1° x 0.1° |	https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form |

(1) May 2022

(2) /store/c2sm/c2sme/reanalyses_dkrz/ERAInterim

(3) /store/c2sm/c2sme/reanalyses_dkrz/ERA5

(4) /net/atmos/data/era5_cds/original

(5) /net/atmos/data/era5-land_cds/original

(6) /net/atmos/data/cerra/original

(7) /net/atmos/data/cerra-land/original

(8) /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v23.1e/processed/, /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v26.0e/processed/

(9) /net/co2/c2sm-data/ch202X/Obs_Data/MCH/processed/

(10) /net/co2/c2sm-data/rlorenz/MERRA2/

(11) /net/atmos/data/cerra/processed/v1/

(12) /net/atmos/data/cerra-land/processed/v1/

(13) /net/atmos/data/era5_cds/processed/v1/

(14) /net/atmos/data/era5-land_cds/processed/v1/
