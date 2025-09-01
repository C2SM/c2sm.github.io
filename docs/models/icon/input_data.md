# Input data

There are two types in input data sets available for ICON:

- General input data for use cases / production runs
- Testing input data for CI

## Santis 

On Säntis, all ICON input data is collected in the project `cws01`.

```shell
/capstor/store/cscs/userlab/cws01/
```

### Directory Tree

```
/capstor/store/cscs/userlab/cws01/
│
├── ci/                              # CI and testing-related data
│   └── input/                       # git lfs repo "testing-input-data" lives here
│
├── input/                           # All input data needed for ICON runs
│   ├── icon-clm/                    # ICON-CLM specific input
│   │   ├── aerosols                 # ICON-CLM aerosol input datasets
│   │   ├── gcm                      # Global climate model boundary data
│   │   ├── rcm                      # Regional climate model boundary data
│   │   ├── ERA5                     # ERA5 reanalysis forcing data
│   │   └── ERAInterim               # ERA-Interim reanalysis forcing data
│   │
│   ├── grids/                       # ICON global grids at different resolutions
│   │   ├── R02B04/
│   │   │   ├── icon_grid_0013_R02B04_G.nc
│   │   │   └── index.txt
│   │   │
│   │   ├── R02B05/
│   │   │   ├── icon_grid_0019_R02B05_G.nc
│   │   │   ├── aerosol_kinne/       # Aerosol climatologies
│   │   │   ├── external_parameter/  # Surface and land-sea mask data
│   │   │   ├── initial_conditions/  # Initial state for atmosphere/ocean
│   │   │   ├── ozone/               # Ozone datasets
│   │   │   ├── ozone_old/           # Legacy ozone datasets
│   │   │   └── sst_and_seaice/      # SST & sea-ice boundary conditions
│   │   │
│   │   └── ...                      # Other grids (R02B06, R02B07, ...)
│   │
│   └── misc/                        # Other input data not tied to specific grids
│
└── validation/                      # Validation/reference datasets
    ├── observations/                # Ground-based or in-situ observations
    ├── reanalysis/                  # Reanalysis datasets (e.g. ERA5, JRA-55)
    ├── satellite/                   # Satellite observations for validation
    └── model_comparisons/           # Reference data from other models
```


## Input data pools

=== "Santis"
    ```shell
    /capstor/store/cscs/userlab/cws01/pool/data/ICON
    ```  
=== "Balfrin"
    ```shell
    /scratch/mch/jenkins/icon/pool/data/ICON
    ```
=== "Euler"
    ```shell
    /cluster/work/climate/icon_input
    ```    

## Testing input data pool

The input data for standard ICON tests are stored in a [Git-lfs repository :material-open-in-new:](https://gitlab.dkrz.de/icon/testing-input-data){:target="_blank"}.

=== "Santis"
    ```shell
     /capstor/store/cscs/userlab/d126/testing-input-data
    ```  
=== "Balfrin"
    ```shell
    /scratch/mch/icontest/testing-input-data
    ```
=== "Euler"
    ```shell
    /cluster/work/climate/icon_testing_input
    ```
