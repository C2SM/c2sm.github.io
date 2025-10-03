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

!!! warning "Work in Progress"

    The directory tree below is a rough outline of the planned structure. It is subject
    to change and non-exhaustive. If you find data that is in the wrong place, or if you
    want to have your data added to the project, please contact
    [Michael Jähn :material-open-in-new:](https://c2sm.ethz.ch/the-center/people/person-detail.html?persid=286091){:target="_blank"}. 

```
/capstor/store/cscs/userlab/cws01/
│
├── ci/                                      # CI 
│   ├── testing-input-data/                  # Input data for CI (git lfs repo)
│   └── buildbot_data/                       # Buildbot data
│       ├── nwp/                             # nwp test case data
│       └── ref/                             # Reference data (hashed)
│
├── input/                                   # All input data
│   ├── icon/                                # ICON-specific input
│   │   ├── clm/                             # ICON-CLM input
│   │   │   ├── independent/                 # Input independent of case/domain
│   │   │   │   ├── aerosols/                # ICON-CLM aerosol input datasets
│   │   │   │   ├── gcm/                     # Global climate model boundary data
│   │   │   │   └── rcm/                     # Regional climate model boundary data
│   │   │   │
│   │   │   └── europe11/                    # EURO-CORDEX 0.11° domain-specific input
│   │   │       ├── aerosols/
│   │   │       ├── gcm/
│   │   │       └── rcm/
│   │   │
│   │   ├── global/                          # ICON global model input
│   │   │   ├── grids/                       # ICON global grids at different resolutions
│   │   │   │   ├── R02B04/
│   │   │   │   │   ├── icon_grid_0013_R02B04_G.nc
│   │   │   │   │   └── index.txt
│   │   │   │   ├── R02B05/
│   │   │   │   │   ├── icon_grid_0019_R02B05_G.nc
│   │   │   │   │   ├── aerosol_kinne/       # Aerosol climatologies
│   │   │   │   │   ├── external_parameter/  # Surface and land-sea mask data
│   │   │   │   │   ├── initial_conditions/  # Initial state for atmosphere/ocean
│   │   │   │   │   ├── ozone/               # Ozone datasets
│   │   │   │   │   ├── ozone_old/           # Legacy ozone datasets
│   │   │   │   │   └── sst_and_seaice/      # SST & sea-ice boundary conditions
│   │   │   │   └── ...                      # Other grids (R02B06, R02B07, ...)
│   │   │   │
│   │   │   └── misc/                        # Other ICON global input data
│   │   │
│   │   ├── public/                          # Public data
│   │   │   └── grids/                       # Public grids from MPI-M and DWD
│   │   │       ├── edzw
│   │   │       └── mpim
│   │   └── regional/                        # ICON regional model input
│   │
│   └── misc/                                # Non-ICON input (placeholder for future)
│
└── reference/                               # Reference datasets
    ├── observations/                        # Ground-based or in-situ observations
    |   └── eObs/                            # E-OBS daily gridded meteorological data for Europe
    |       ├── eObs28.0/
    |       ├── eObs29.0/
    |       ├── eObs30.0/
    |       └── eObs31.0/
    ├── reanalysis/                          # Reanalysis datasets (e.g. ERA5)
    |   ├── ERA5/
    |   └── dkrz/                            # Synced from DKRZ, ready-to-use for SPICE (CLM runs)
    |       ├── ERA5/                        # ERA5 (updated as soon as new data is available)
    |       └── ERAInterim/                  # ERAInterim (static)
    ├── satellite/                           # Satellite observations for validation
    └── model_comparisons/                   # Reference data from other models
```


## Input data pools

=== "Santis"
    ```shell
    /capstor/store/cscs/userlab/cws01/input/icon
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
     /capstor/store/cscs/userlab/cws01/ci/testing-input-data
    ```  
=== "Balfrin"
    ```shell
    /scratch/mch/icontest/testing-input-data
    ```
=== "Euler"
    ```shell
    /cluster/work/climate/icon_testing_input
    ```
