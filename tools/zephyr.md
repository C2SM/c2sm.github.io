---
title: Zephyr
layout: default
parent: Tools
---

# <img src="https://polybox.ethz.ch/index.php/s/Na2CeLPTzhtmh1T/download" width="110" valign="middle" alt="Zephyr"/>  Climate Data Extraction Tool

Zephyr is the climate data extraction tool developed by C2SM, serving as the backend processing engine for the [Zephyr website](https://zephyr.ethz.ch).

## Support status

The `main` branch is tested daily and for incoming changes via GitHub pull requests.

Scans of the datasets listed below are performed daily, generating file trees in JSON format. This ensures that the data information for the [Zephyr website](https://zephyr.ethz.ch) is kept up to date.

## Features

Requests are made via the [Zephyr website](https://zephyr.ethz.ch) and submitted using the [Zephyr data request template](https://github.com/C2SM/zephyr-request/issues/new/choose). Zephyr supports a range of climate models and reanalysis datasets, including:

- CMIP5
- CMIP6
- CORDEX
- CORDEX ReKliEs
- ERA5
- ERA5 land
- CERRA
- CERRA land

Zephyr efficiently extracts both regional and global climate datasets, offering options for data retrieval at single nearest gridpoints or within a user-defined rectangular area. After successful submission and processing, a download link to the processed data is sent via email and is also displayed in the GitHub issue where the request was submitted, which remains available for up to seven days.

## Code

* [Zephyr](https://github.com/C2SM/zephyr/tree/main)

## Access

* Zephyr website to create requests: [Zephyr Website](https://zephyr.ethz.ch)
* Submitting Zephyr data requests: [Zephyr-request]([https://github.com/C2SM/zephyr-request](https://github.com/C2SM/zephyr-request/issues/new?assignees=&labels=data+request&projects=&template=data-request.md)

## Local Processing at IAC

If you have access to IAC servers, you can use Zephyr directly without submitting your request via the [Zephyr data request template](https://github.com/C2SM/zephyr-request/issues/new/choose). To do this, clone and install the tool in your workspace by following the instructions in the [Zephyr README](https://github.com/C2SM/zephyr/tree/main). Once installed, you can process requests created via the Zephyr website using the following command:

```shell
python launch_zephyr.py --json_path=/path/to/your/request --output_directory=/path/to/your/output/directory
```
