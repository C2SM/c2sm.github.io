# ![](https://polybox.ethz.ch/index.php/s/P1sc5n7TLhmUcld/download#only-light){:style="vertical-align: top"} ![](https://polybox.ethz.ch/index.php/s/7FVqpqKOPQw9xew/download#only-dark){:style="vertical-align: top"} Climate Data Extraction Tool


Zephyr is the climate data extraction tool developed by C2SM, serving as the backend processing engine for the [Zephyr website :material-open-in-new:](https://zephyr.ethz.ch){:target="_blank"}.

## Support status

The `main` branch is tested daily and for incoming changes via GitHub pull requests.

Scans of the datasets listed below are performed daily, generating file trees in JSON format. This ensures that the data information for the [Zephyr website :material-open-in-new:](https://zephyr.ethz.ch){:target="_blank"} is kept up to date.

## Features

Requests are made via the [Zephyr website :material-open-in-new:](https://zephyr.ethz.ch){:target="_blank"} and submitted using the [Zephyr data request template :material-open-in-new:](https://github.com/C2SM/zephyr-request/issues/new/choose){:target="_blank"}. Zephyr supports a range of [climate models and reanalysis datasets](../datasets/index.md), including:

- [CMIP5](../datasets/climate_model_data.md#cmip5)
- [CMIP6](../datasets/climate_model_data.md#cmip6)
- [CORDEX](../datasets/climate_model_data.md#cordex)
- [CORDEX ReKliEs](../datasets/climate_model_data.md#cordex-reklies)
- [ERA5](../datasets/obs_reanalysis_data.md#era5_1)
- [ERA5 land](../datasets/obs_reanalysis_data.md#era5-land_1)
- [CERRA](../datasets/obs_reanalysis_data.md#cerra_1)
- [CERRA land](../datasets/obs_reanalysis_data.md#cerra-land_1)

Zephyr efficiently extracts both regional and global climate datasets, with options to retrieve data at individual nearest grid points or within a user-defined rectangular area. Once a request has been successfully submitted and processed, a download link will be posted to the GitHub issue thread where the request was submitted. The download link will be available for up to seven days.

## Code

* [Zephyr :material-open-in-new:](https://github.com/C2SM/zephyr/tree/main){:target="_blank"} on GitHub

## Local Processing at IAC

If you have access to IAC servers, you can use Zephyr directly without submitting your request via the [Zephyr data request template :material-open-in-new:](https://github.com/C2SM/zephyr-request/issues/new/choose){:target="_blank"}. To do this, clone and install the tool in your workspace by following the instructions in the [Zephyr README :material-open-in-new:](https://github.com/C2SM/zephyr/tree/main){:target="_blank"}. Once installed, you can process requests created via the Zephyr website using the following command:

```shell
python launch_zephyr.py --json_path=/path/to/your/request --output_directory=/path/to/your/output/directory
```
