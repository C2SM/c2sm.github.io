# Run Probtest on Säntis

Use Probtest to verify whether your test case produces consistent results on GPU. It compares a GPU test run to a CPU ensemble with perturbed input conditions.

## 1. Set Up the Probtest Container and Environment on Säntis
To run Probtest for ICON on Säntis, use the prebuilt container available on Docker Hub ([Probtest Container :material-open-in-new:](https://github.com/MeteoSwiss/probtest?tab=readme-ov-file#probtest-container){:target="_blank"}).

ICON provides the wrapper script [probtest_container_wrapper.py :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/scripts/cscs_ci/probtest_container_wrapper.py?ref_type=heads){:target="_blank"}.
If your ICON version doesn’t include this script, add it to `icon/scripts/cscs_ci/probtest_container_wrapper.py`, along with the appropriate [PROBTEST_TAG :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/ci_probtest/run/tolerance/PROBTEST_TAG?ref_type=heads){:target="_blank"} under `icon/run/tolerance/PROBTEST_TAG`.


### When Setting Up a New Build Directory
In your ICON build directory, run:

Import the containter:
```console
PROBTEST_TAG=$(cat run/tolerance/PROBTEST_TAG)
enroot import docker://c2sm/probtest:${PROBTEST_TAG}
```

Add a TOML configuration and export EDF path (being used when running the container):
```console
echo "image = \"$(pwd)/c2sm+probtest+${PROBTEST_TAG}.sqsh\"" > probtest.toml
echo "mounts = [ \"$(pwd)\" ]" >> probtest.toml
echo "workdir = \"$(pwd)\"" >> probtest.toml
echo "writable = true" >> probtest.toml
export EDF_PATH=$(pwd)
```

Create and activate Python environment:
```console
python3 -m venv .venv
source .venv/bin/activate
pip install pyyaml pandas click toml
```

### Every Time You Reconnect to the Server
If the container and environment are already set up, simply re-run:
```console
export EDF_PATH=$(pwd)
source .venv/bin/activate
```

Set experiment name, e.g.:
```console
export EXPERIMENT=c2sm_clm_r13b03_seaice
```

Export required environment variables:
```console
export BB_NAME=santis_cpu_nvhpc
export UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
```

## 2. Run perturbed ensemble on CPU.
Generate and run a 10-member ensemble on the CPU (this may take time):
```console
./make_runscripts $EXPERIMENT
uenv run ${UENV_VERSION} -- python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```

## 3. Generate Reference and Tolerance from Ensemble

Create reference and tolerance files using the 10 ensemble members:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 10)
```

This generates:

- `${EXPERIMENT}_reference.csv`
- `${EXPERIMENT}_tolerance.csv`

## 4. Run the test case on GPU and collect statistics.
Navigate to your GPU build folder and run the same test case, e.g.:
```console
cd <path-to-GPU-build>
./make_runscripts $EXPERIMENT
cd run && sbatch --uenv ${UENV_VERSION} ./exp.c2sm_clm_r13b03_seaice.run
```

Navigate back to the CPU build and collect the GPU statistics (replace <path-to-GPU-build>):
```console
cd <path-to-CPU-build>
python3 scripts/cscs_ci/probtest_container_wrapper.py stats $EXPERIMENT --stats-file-path stats_gpu.csv --build-dir $(pwd) --model-output-dir <path-to-GPU-build>/experiments/$EXPERIMENT
```

This saves the GPU stats as `stats_gpu.csv`.

## 5. Check GPU Statistics Against Reference and Tolerance

Run the check using the generated reference and tolerance:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py check $EXPERIMENT --input-file-cur stats_gpu.csv --input-file-ref ${ref_path}/${EXPERIMENT}_reference.csv --tolerance-file-name ${ref_path}/${EXPERIMENT}_tolerance.csv
```

## 6. Increase Ensemble Size if Validation Fails
A 10-member ensemble may not capture the full variability, causing false negatives. Increase to 49 members for better coverage:

Run additional members (11–49):
```console
./make_runscripts $EXPERIMENT
uenv run ${UENV_VERSION} -- python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 11 49)
```

Regenerate reference and tolerance using all 49 members:
```console
python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXPERIMENT --build-dir $(pwd) --member-ids $(seq -s, 1 49)
```

*If the test still fails, the GPU result is likely incorrect.*