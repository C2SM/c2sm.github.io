# "Raw" CMIP archives (as downloaded from ESGF)

| Archive   | Size (#Files) (3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CMIP2     |	0.01 TB (500)       |	IAC            |	direct / rsync | frozen (2010-10) |	           | native (1) |
| CMIP3     |	6 TB (40’000)       |	IAC            |	direct / rsync | frozen (2016-12) |	           | native |
| CMIP5     | 130 TB (700’000)    | IAC            |  direct / rsync | monthly updated  |	           | native |
| CMIP6     |	520 TB (5’500’000)  | IAC, Euler (4) |  direct / rsync | weekly updated   |	           | native |

# CMIP next generation (checked, standardized, regridded to common grid)

| Archive   | Size (#Files) (3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CMIP3-ng (2) | 0.5 TB (5’000)   |	IAC 	         | direct / rsync  | frozen (2019-03) | 	  	     | native and 2.5°x2.5° |
| CMIP5-ng (2) | 33 TB (100’000)  | IAC            | direct / rsync  | frozen (2019-09) |  	         | native and 2.5°x2.5° |
| CMIP6-ng (2) | 175 TB (500’000) | IAC, Euler (4) | direct / rsync  | ongoing          |	monthly: co2mass, hfls, mrro, npp, rlds, rsdscs, rtmt, tasmin, tsl, evspsbl, hfss, mrros, pr, rldscs, rsdt, sftlf, tauu, zg500, evspsblsoi, hurs, mrso prw, rlus, rsus, siconc, tauv, evspsblveg, huss, mrsol, psl, rlut, rsuscs, ta, tos, areacella, gpp, lai, mrsos, ra, rlutcs, rsut, tas, tran, clt, hfds, nbp, rh, rsds, rsutcs, tasmax, treeFrac, zos, daily: pr, tas, tasmin, tasmax, zg500, mrro |	native and 2.5°x2.5° |

# "Raw" CORDEX (as downloaded)

| Archive   | Size (#Files) (3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CORDEX    |	370 TB (800’000) 	  | IAC, Euler (4), CSCS (5) | direct / rsync | monthly updated | | 0.44° and 0.11° |
| CORDEX-ReKliEs | 23 TB (100’000) | IAC, Euler (4)          | direct         |	monthly updated |	|  	0.11° |

# CORDEX data for climate scenarios (checked, regridded to identical grids if necessary)

| Archive   | Size (#Files) (3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CORDEX.ch2018 |	11 TB (1’800) |	IAC, CSCS (5) |	direct |	frozen (2019-04) |	daily: hurs, huss, pr, rsds, sfcWind, sfcWindmax, snw, tas, tasmax, tasmin |	0.44° and 0.11° |
| CORDEX.ch2025 |	46 TB (3’500) |	IAC (6) |	direct 	| ongoing |	daily: pr, tas, tasmax, tasmin, zg500 |	0.44° and 0.11° |
| CORDEX-FPSCONV |	30T (22'949) |	CSCS (7) |	direct |	ongoing |	1hr: pr, tas, daily: pr, tas, tasmax, tasmin |	2-3km  |

(1) native means every model on their native grid they were run on

(2) CMIP-ng: Next Generation archives were maintained by Reto's group (Jan Sedlacek/Lukas Brunner)
Ruth Lorenz / C2SM took over cmip6-ng in 2022. contact: cmip6-archive@env.ethz.ch, documentation: https://doi.org/10.5281/zenodo.3734128

(3) Stand June 2021

(4) cd /nfs/atmos/c2sm

(5) cd /store/c2sm/c2sme

(6) cd /net/ch4/data/cordex.ch2025/

(7) cd /store/c2sm/c2sme/CH202X/CORDEX-FPSCONV/ALP-3/ 
