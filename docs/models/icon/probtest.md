# Run Probtest

## Säntis
To run Probtest for ICON on Säntis, it is the easiest to run Probtest in a container, which is available on Docker Hub (see [Probtest Container :material-open-in-new:](https://github.com/MeteoSwiss/probtest?tab=readme-ov-file#probtest-container){:target="_blank"}). In ICON, there is a [probtest_container_wrapper.py :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/scripts/cscs_ci/probtest_container_wrapper.py?ref_type=heads){:target="_blank"} script you can make use of. If you are using an ICON version, which does not include the wrapper yet, please add it under `icon/scripts/cscs_ci/probtest_container_wrapper.py` as well as the corresponding [PROBTEST_TAG :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/run/tolerance/PROBTEST_TAG?ref_type=heads) under `icon/run/tolerance/PROBTEST_TAG`.

### Setup Probtest Container and Requirements
Navigate to your ICON build folder to do the following.

Import the containter:
```console
PROBTEST_TAG=$(cat run/tolerance/PROBTEST_TAG)
enroot import docker://c2sm/probtest:${PROBTEST_TAG}
```

Add a toml file to your build folder and export the current path as the EDF path:
```console
echo "image = \"$(pwd)/c2sm+probtest+${PROBTEST_TAG}.sqsh\"" > probtest.toml
echo "mounts = [ \"$(pwd)\" ]" >> probtest.toml
echo "workdir = \"$(pwd)\"" >> probtest.toml
echo "writable = true" >> probtest.toml
export EDF_PATH=$(pwd)
```

Create and source Python environment:
```console
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/cscs_ci/requirements.txt
```

If the container and Python environment are already set up, you can just run the following instead of the above:
```console
export EDF_PATH=$(pwd`
source .venv/bin/activate
```

Export the experiment you are going to work with, e.g.:
```console
export EXPERIMENT=c2sm_clm_r13b03_seaice
```

Export relevant environmental variables:
```console
export BB_NAME=santis_cpu_nvhpc
export UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
```