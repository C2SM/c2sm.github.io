# ECMWF Data Cube

!!! warning
    The following information is new and work in progress, thus not everything might be up to data at all times.

The ECMWF Data Cube is currently set up on AlpsB,
which is a storage system at the ECMWF Data Center in Bologna.

## Technical Details

- Storage-focused system
- data hypercube
- 0.5 PB of fast SSD storage
- 2 PB of “slow” storage
- Build via work package of SwissTwins project
- Physically installed at ECMWF Bologna with a direct connection to Alps Lugano [ALPS](../hpc/index.md)
- Part of the multi-site distributed infrastructure (Lugano, Lausanne, Bologna)

## Usage

- Using [polytope :material-open-in-new:](https://polytope-client.readthedocs.io/en/latest/index.html){:target="_blank"}
  web service it will be possible to query ECMWF MARS (Meteorological Archival and Retrieval System)
- Polytope is set up on AlpsB
- An [initial ERA5 dataset :material-open-in-new:](https://docs.google.com/spreadsheets/d/1oKjhWkcIRSb-vsmQz5OxGSe6SgSO4-Zttg8OMj8qyvU/edit?usp=sharing){:target="_blank"} has been copied to AlpsB and can be queried using polytope
- [Repo with examples :material-open-in-new:](https://github.com/C2SM/polytope-ecmwf){:target="_blank"}
