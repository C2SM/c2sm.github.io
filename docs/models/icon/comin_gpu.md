# ComIn on GPU

This guide shows how to compile ICON on **Säntis** with GPU support and the
[ICON Community Interface (ComIn) :material-open-in-new:](https://gitlab.dkrz.de/icon-comin/comin){:target="_blank"},
including its Python adapter, and how to run a small test case with a Python plugin on the GPU.

It is based on the public ICON release `release-2026.10-public`, which bundles
[ComIn v1.0.0 :material-open-in-new:](https://www.icon-model.org/news/news-1/icon-comin-v1-0-0-release-announcement){:target="_blank"},
the first stable release of ComIn. Only the official uenv and the configure wrapper of the release are needed.

!!! warning "Migrating plugins from ComIn 0.x"

    ComIn v1.0 is not compatible with earlier versions. Every plugin has to be recompiled, and the namelist
    has changed: the single `comin_nml` group with `plugin_list(i)%` entries is replaced by one
    `comin_plugin_nml` group per plugin (see [step 6](#6-use-comin-in-your-own-experiment)).
    For all changes, see the
    [migration guide :material-open-in-new:](https://icon-comin.gitlab-pages.dkrz.de/comin/){:target="_blank"}
    of ComIn.

## 1. Clone ICON

```bash
git clone -b release-2026.10-public --recurse-submodules https://git.gitlab.dkrz.de/icon/icon-model.git
cd icon-model
```

All following commands are run from the ICON root folder unless stated otherwise.

## 2. Enable ComIn and Its Python Adapter

Add the `comin` variant to the Spack spec of the Säntis GPU build. The Python adapter, which is required for
Python plugins, is enabled with the configure option `--enable-bundled-python=comin`:

```bash
sed -i 's/+mpi-gpu +realloc-buf/+mpi-gpu +realloc-buf +comin extra-config-args=--enable-bundled-python=comin/' \
    config/cscs/spack/santis_gpu_double/spack.yaml
```

ComIn v1.0.0 contains a bug that can skip the device-to-host copy of a variable the first time a CPU plugin reads it,
so the plugin sees outdated data. It is fixed in ComIn
[c14abf4 :material-open-in-new:](https://gitlab.dkrz.de/icon-comin/comin/-/commit/c14abf4){:target="_blank"},
which is not part of the ICON release. Apply the fix with:

```bash
sed -i 's/^  bool accessed;/  bool accessed = false;/' externals/comin/src/core/comin_state.hpp
```

## 3. Compile ICON

Compile ICON out-of-source in the folder `gpu`, as described in [Compile](compile.md#building-out-of-source):

```bash
UENV_VERSION=$(cat config/cscs/SANTIS_ENV_TAG)
mkdir gpu && cd gpu
uenv run ${UENV_VERSION} --view default -- ./../config/cscs/santis.gpu.nvhpc
```

The compilation takes about one hour. Besides the ICON binary `bin/icon`, it produces the Python adapter
`externals/comin/build/_icon/plugins/python_adapter/libpython_adapter.so`.

## 4. Create a Python Environment for the Plugins

The Python adapter embeds the Python interpreter of the uenv (Python 3.13).
Create a virtual environment from this interpreter inside the folder `gpu` and install the packages
your plugins need. For plugins running on the GPU, install [CuPy :material-open-in-new:](https://cupy.dev){:target="_blank"}
for CUDA 13, which is the CUDA version of the uenv:

```bash
uenv run ${UENV_VERSION} --view default -- bash -c \
    'python -m venv venv-comin && ./venv-comin/bin/pip install numpy "cupy-cuda13x[ctk]"'
```

!!! info "CuPy needs the CUDA headers"

    The `[ctk]` extra installs the CUDA headers that CuPy needs to compile its kernels at runtime.
    Without it, the plugin fails with `RuntimeError: Failed to find CUDA headers`.

## 5. Run a Test Case

The ICON release contains the test case `atm_tracer_Hadley_comin_portability`, a pure tracer advection
experiment on a coarse global grid. It attaches the Python plugin `gpu_test.py`, which uses CuPy to write
ICON variables on the GPU and checks the data transfers between CPU and GPU.

Copy the experiment into the `run` folder, set the path to the grid file on Säntis and create the run script:

```bash
EXP=atm_tracer_Hadley_comin_portability
cp run/checksuite.infrastructure/comin/exp.${EXP} run/
sed -i 's|^grids_folder=.*|grids_folder=/capstor/store/cscs/userlab/cws01/ci/testing-input-data/c2sm/tracer_Hadley|' \
    run/exp.${EXP}
./make_runscripts ${EXP}
```

Tell the Python adapter to use the virtual environment and submit the job:

```bash
export COMIN_PYTHON_EXECUTABLE=${PWD}/venv-comin/bin/python
cd run && sbatch --uenv ${UENV_VERSION} --account=<my_account_id> ./exp.${EXP}.run
```

The job runs on one node with four GPUs and takes about 15 minutes. The log file
`LOG.exp.atm_tracer_Hadley_comin_portability.run.<job_id>.o` contains the messages of the plugin, e.g.:

```console
 INFO(cuda_test): glob.device_name='NVIDIA GH200 120GB'
 INFO(cuda_test): Using cupy!
```

and ends with `Script run successfully:  OK`.

## 6. Use ComIn in Your Own Experiment

Add one `comin_plugin_nml` group per plugin to the atmosphere namelist of your experiment.
For a Python plugin, `plugin_library` is the Python adapter and `options` is the path to your plugin script:

```fortran
&comin_plugin_nml
  name           = "my_plugin"
  plugin_library = "<icon_root>/gpu/externals/comin/build/_icon/plugins/python_adapter/libpython_adapter.so"
  options        = "<path_to_my_plugin>.py"
/
```

Export `COMIN_PYTHON_EXECUTABLE` as in [step 5](#5-run-a-test-case) before submitting the job, or set it in the
run script.

## Further Reading

- [ComIn documentation :material-open-in-new:](https://icon-comin.gitlab-pages.dkrz.de/comin/){:target="_blank"}
  with the Python API, the section on using GPUs and the migration guide
- Example plugins in `externals/comin/plugins` of the ICON source code, e.g.,
  `python_adapter/examples/simple_python_plugin.py`
