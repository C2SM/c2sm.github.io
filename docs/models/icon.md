
# ICON
ICON (Icosahedral Nonhydrostatic Weather and Climate Model) is a global model suitable for climate and weather prediction at regional and global domains.
It is a joint project of [DWD :material-open-in-new:](https://www.dwd.de/DE/Home/home_node.html){:target="_blank"}, [MPI-M :material-open-in-new:](https://mpimet.mpg.de/startseite){:target="_blank"} and [KIT :material-open-in-new:](https://www.kit.edu/){:target="_blank"}.

To stay informed about what is going on in the ICON world and to get to know other ICON users, please attend our [quarterly ICON meeting](../events/icon_meetings/index.md).

## Support status
C2SM facilitates the utilisation of ICON on the [Piz Daint :material-open-in-new:](https://www.cscs.ch/computers/piz-daint){:target="_blank"} and [Euler :material-open-in-new:](https://scicomp.ethz.ch/wiki/Euler){:target="_blank"} computing platforms for the CPU and GPU architectures.

### Supported release
The latest release distributed by C2SM, currently `2024.01`, is continuously being tested on both Piz Daint and Euler and receives patches when necessary.

## Mailing list
If you use ICON, please follow [these instructions](../events/icon_meetings/index.md#c2sm-icon-mailing-list) to subscribe to our mailing list.

## Access
The ICON repository is hosted on the C2SM GitHub organisation. If you do not have access, please follow the instructions under [How to get Access](../index.md#how-to-get-access).

Once you have access, clone the repository from GitHub using the SSH protocol:

  ```bash
  git clone --recurse-submodules git@github.com:C2SM/icon.git
  ```
  If you do not already have an SSH key set up for GitHub, but would like to do so, follow the [instructions :material-open-in-new:](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent){:target="_blank"}.
    
## Configure and compile
The ICON build process is almost identical for Piz Daint and Euler. For both machines, Spack is used to build ICON. Refer to the official spack-c2sm documentation for [installing ICON using Spack :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon){:target="_blank"}.

### Piz Daint
Refer to the official spack-c2sm documentation for [installing ICON using Spack :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon){:target="_blank"}. To [set up a Spack instance :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin){:target="_blank"}, ensure that you clone the repository using the Spack tag provided in the ICON repository at [config/cscs/SPACK_TAG_DAINT :material-open-in-new:](https://github.com/C2SM/icon/blob/main/config/cscs/SPACK_TAG_DAINT){:target="_blank"}.

### Euler
Refer to the official spack-c2sm documentation for [installing ICON using Spack :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#icon){:target="_blank"}. To [set up a Spack instance :material-open-in-new:](https://c2sm.github.io/spack-c2sm/latest/QuickStart.html#at-cscs-daint-tsa-balfrin){:target="_blank"}, ensure that you clone the repository using the Spack tag provided in the ICON repository at [config/ethz/SPACK_TAG_EULER :material-open-in-new:](https://github.com/C2SM/icon/blob/main/config/ethz/SPACK_TAG_EULER){:target="_blank"}.

Euler Support recommends to compile code on compute-nodes. Unfortunately [internet-access on Euler compute-nodes is restricted :material-open-in-new:](https://scicomp.ethz.ch/wiki/Accessing_the_clusters#Internet_Security){:target="_blank"}.
Therefore a two-step install needs to be performed:

```bash
# fetch and install cosmo-eccodes-definitions on login-node
spack install cosmo-eccodes-definitions

# compile ICON on compute-nodes
srun -N 1 -c 12 --mem-per-cpu=20G spack install -v -j 12
```

## Run test case with ICON
In the *run* folder, you find many prepared test cases, which you can convert into run scripts. To generate the runscript of one of the experiment files, e.g. *mch_ch_lowres*, you can use the `make_runscripts` function.

```bash
./make_runscripts mch_ch_lowres
```

To run the created runscript, navigate to the *run* subdirectory and submit the runscript.

```bash
cd run && sbatch ./exp.mch_ch_lowres.run
```
You may need to adjust the account in the runscript to match your permissions. Alternatively, you can include `--account <my_account_id>` in the `sbatch` command.

## Input data
ICON input data are stored at the following locations:

- **Piz Daint (CSCS):** `/users/icontest/pool/data/ICON`
- **Euler:** `/cluster/work/climate/icon_input`


## Toolset
In the [Tools](../tools/index.md) section, you will find relevant tools for working with ICON:

* [**Extpar:**](../tools/extpar.md): External parameters for the ICON grid (preprocessing)
* [**Processing Chain**](../tools/processing_chain.md): Python workflow tool for ICON
* [**SPICE**](../tools/spice.md): Starter package for ICON-CLM experiments
* [**icon-vis**](../tools/icon-vis.md): Python scripts to visualise ICON data

## Projects
Learn more about ongoing projects involving ETHZ in the development of ICON:

  * [EXCLAIM :material-open-in-new:](https://exclaim.ethz.ch/){:target="_blank"} 
  * [ICON-HAMMOZ :material-open-in-new:](https://redmine.hammoz.ethz.ch/projects/icon-hammoz){:target="_blank"}

## Documentation
ICON documentation is available at:

   * [ICON Tutorial (DWD) :material-open-in-new:](https://www.dwd.de/DE/leistungen/nwv_icon_tutorial/nwv_icon_tutorial.html){:target="_blank"}
   * [Getting Started with ICON :material-open-in-new:](https://www.icon-model.org/icon_model/getting_started){:target="_blank"}
   * [MPI-M documentation :material-open-in-new:](https://code.mpimet.mpg.de/projects/iconpublic/wiki/Documentation){:target="_blank"}
     
## External Software
The following external software is useful for working with ICON data:

   * [CDO :material-open-in-new:](https://code.zmaw.de/projects/cdo){:target="_blank"}
