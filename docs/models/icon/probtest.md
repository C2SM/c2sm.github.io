# Run Probtest on Säntis

Use probtest to check if your test case is working on GPU. Therefore, the GPU run is being compared to the statistics of a CPU ensemble with perturbed input conditions.

## 1. Setup Probtest Container and Requirements on Säntis
To run Probtest for ICON on Säntis, it is the easiest to run Probtest in a container, which is available on Docker Hub (see [Probtest Container :material-open-in-new:](https://github.com/MeteoSwiss/probtest?tab=readme-ov-file#probtest-container){:target="_blank"}). In ICON, there is a [probtest_container_wrapper.py :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/scripts/cscs_ci/probtest_container_wrapper.py?ref_type=heads){:target="_blank"} script you can make use of. If you are using an ICON version, which does not include the wrapper yet, please add it under `icon/scripts/cscs_ci/probtest_container_wrapper.py` as well as the corresponding [PROBTEST_TAG :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/run/tolerance/PROBTEST_TAG?ref_type=heads) under `icon/run/tolerance/PROBTEST_TAG`.

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

## 2. Run perturbed ensemble on CPU.
Run ensemble with 10 members (this will take a while, as there is currently no parallel job execution enabled):
```console
./make_runscripts $EXPERIMENT
uenv run ${UENV_VERSION} -- python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```

## 3. Generate a reference and tolerance from the ensemble.

Create reference and tolerance from ensemble:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```

The reference and tolerance file will be saved as `${EXPERIMENT}_reference.csv` and `${EXPERIMENT}_tolerance.csv` respectively.


## 4. Run the test case on GPU and collect statistics.
Navigate to your GPU build folder and run the same test case, e.g.:
```console
cd <path-to-GPU-build>
./make_runscripts $EXPERIMENT
cd run && sbatch --uenv ${UENV_VERSION} ./exp.c2sm_clm_r13b03_seaice.run
```

Navigate back to the CPU build and collect the GPU statistics:
```console
cd <path-to-CPU-build>
python3 scripts/cscs_ci/probtest_container_wrapper.py stats $EXPERIMENT --stats-file-path stats_gpu.csv --build-dir $(pwd)
```

This will save the GPU statistics into `stats_gpu.csv`.

## 5. Check if the GPU statistics validate with the given reference and tolerance.

Run the tolerance check against `${EXPERIMENT}_reference.csv` and `${EXPERIMENT}_tolerance.csv`.
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py check $EXPERIMENT --input-file-cur stats_gpu.csv --input-file-ref ${ref_path}/${EXPERIMENT}_reference.csv --tolerance-file-name ${ref_path}/${EXPERIMENT}_tolerance.csv
```

## 6. Use larger ensemble in case probtest does not validate.
An ensemble with 10 members may not cover the whole spread and it can happen that probtest fails, even though the GPU run is correct. To make sure this is not the case, you can increase the ensemble (50 members should be enough).

Run additional ensemble with members 11 to 49:
```console
./make_runscripts $EXPERIMENT
uenv run ${UENV_VERSION} -- python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 11 49)
```

Generate reference and tolerance from 49 members and the reference run:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 49)
```

Now check again if the GPU run validates. IF it still doesn't, there seems to be an error on the GPU.