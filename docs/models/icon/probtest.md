# Run Probtest on Säntis

Use Probtest to verify whether your test case produces consistent results on GPU. It compares a GPU test run to a CPU ensemble with perturbed input conditions.

## 1. Compile ICON
Compile ICON on CPU and on GPU as [out-of-source builds](compile_and_run.md#building-out-of-source) in sub-directories of ICON.

!!! note
    The probtest container uses the ICON root directory as its working directory and can therefore only access data within the ICON root directory. This is why the out-of-source builds need to be subdirectories of ICON.

## 2. Set Up the Probtest Container and Environment on Säntis
To run Probtest for ICON on Säntis, use the prebuilt container available on Docker Hub ([Probtest Container :material-open-in-new:](https://github.com/MeteoSwiss/probtest?tab=readme-ov-file#probtest-container){:target="_blank"}). ICON provides the wrapper script [`probtest_container_wrapper.py` :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/master/scripts/cscs_ci/probtest_container_wrapper.py?ref_type=heads){:target="_blank"}.

!!! note
    If your ICON version doesn’t include this script, add it to `scripts/cscs_ci/probtest_container_wrapper.py`, along with the appropriate [PROBTEST_TAG :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/master/run/tolerance/PROBTEST_TAG?ref_type=heads){:target="_blank"} under `run/tolerance/PROBTEST_TAG` and [yaml_experiment_test_processor.py :material-open-in-new:](https://gitlab.dkrz.de/icon/icon-nwp/-/blob/master/scripts/experiments/yaml_experiment_test_processor.py?ref_type=heads){:target="_blank"} under `scripts/experiments/yaml_experiment_test_processor.py` (replace if already available).


### When Setting Up ICON from Scratch
Add a TOML configuration to run the probtest container in your ICON root directory (this requires setting the `EDF_PATH` to your *current directory* = *ICON root directory*):
```console
PROBTEST_TAG=$(cat run/tolerance/PROBTEST_TAG)
echo "image = 'c2sm/probtest:${PROBTEST_TAG}'" > probtest.toml
echo "mounts = [ \"$(pwd)\" ]" >> probtest.toml
echo "workdir = \"$(pwd)\"" >> probtest.toml
echo "writable = true" >> probtest.toml
```

### Every Time You Reconnect to the Server
If the `probtest.toml` file already exists in your ICON root directory, run the following command from within that directory:
```console
# Set the path to the probtest.toml file
export EDF_PATH=$(pwd)

# Set the builder name
export BB_NAME=santis_cpu_nvhpc

# Set the uenv version
export UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)

# Point the Python image and create empty folder to mount to
export SQFS_PATH=/capstor/store/cscs/userlab/cws01/ci/ci-python-image/py_icon_ci.squashfs
mkdir -p .venv
```

Set experiment name, e.g.:
```console
export EXP=c2sm_clm_r13b03_seaice
```

## 3. Run perturbed ensemble on CPU
To run a perturbed ensemble, please allocate compute nodes interactively to *not* use your login nodes. Therefore, run the following:
```console
salloc -p normal --time=01:00:00
```

Then navigate to your CPU build directory and generate and run a 10-member ensemble (this may take time):
```console
cd nvhpc_cpu
./make_runscripts $EXP
uenv run ${UENV_VERSION},${SQFS_PATH}:${EDF_PATH}/.venv --view modules,default -- bash -c 'source ${EDF_PATH}/.venv/bin/activate && module load nvhpc cdo && python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXP --build-dir $(pwd) --member-ids $(seq -s, 1 10)'
```

This generates:

- `stats_${EXP}_<member_id>.csv`
- `${EXP}_reference.csv`

## 4. Generate Tolerance from Ensemble

Create reference and tolerance files using the 10 ensemble members:
```console
uenv run ${UENV_VERSION},${SQFS_PATH}:${EDF_PATH}/.venv -- bash -c 'source ${EDF_PATH}/.venv/bin/activate && python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXP --build-dir $(pwd) --member-ids $(seq -s, 1 10)'
```

This generates:

- `${EXP}_tolerance.csv`

## 5. Run the test case on GPU and collect statistics
Navigate to your GPU build folder and run the same test case, e.g.:
```console
cd ../nvhpc_gpu
./make_runscripts $EXP
cd run && uenv run $UENV_VERSION --view modules,default -- bash -c 'module load nvhpc cdo && ./exp.$EXP.run 2>&1 | tee LOG.exp.$EXP.run.o' && cd ..
```

Navigate back to ICON root folder and collect the GPU statistics:
```console
cd ..
uenv run ${UENV_VERSION},${SQFS_PATH}:${EDF_PATH}/.venv -- bash -c 'source ${EDF_PATH}/.venv/bin/activate && python3 scripts/cscs_ci/probtest_container_wrapper.py stats $EXP --stats-file-path stats_gpu.csv --build-dir nvhpc_gpu'
```

This saves the GPU stats as `stats_gpu.csv` in your ICON root directory.

## 6. Check GPU Statistics Against Reference and Tolerance

From your ICON root directory, run the check using the generated reference and tolerance:
```console
uenv run ${UENV_VERSION},${SQFS_PATH}:${EDF_PATH}/.venv -- bash -c 'source ${EDF_PATH}/.venv/bin/activate && python3 scripts/cscs_ci/probtest_container_wrapper.py check $EXP --input-file-cur stats_gpu.csv --input-file-ref nvhpc_cpu/${EXP}_reference.csv --tolerance-file-name nvhpc_cpu/${EXP}_tolerance.csv --build-dir $(pwd)'
```

## 7. Increase Ensemble Size if Validation Fails
Again, if not done already, allocate compute nodes interactively to *not* use your login nodes:
```console
salloc -p normal --time=01:20:00
```

A 10-member ensemble may not capture the full variability, causing false negatives. Increase to 49 members for better coverage from your CPU build directory:

Run additional members (11–49):
```console
cd nvhpc_cpu
./make_runscripts $EXP
uenv run ${UENV_VERSION},${SQFS_PATH}:${EDF_PATH}/.venv --view modules,default -- bash -c 'source ${EDF_PATH}/.venv/bin/activate && module load nvhpc cdo && python3 scripts/cscs_ci/probtest_container_wrapper.py ensemble $EXP --build-dir $(pwd) --member-ids $(seq -s, 11 49)'
```

Regenerate reference and tolerance using all 49 members:
```console
uenv run ${UENV_VERSION},${SQFS_PATH}:${EDF_PATH}/.venv -- bash -c 'source ${EDF_PATH}/.venv/bin/activate && python3 scripts/cscs_ci/probtest_container_wrapper.py tolerance $EXP --build-dir $(pwd) --member-ids $(seq -s, 1 49)'
```

*If the test still fails, the GPU result is likely incorrect.*