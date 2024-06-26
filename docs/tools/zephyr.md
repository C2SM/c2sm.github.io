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

Zephyr efficiently extracts both regional and global climate datasets, with options to retrieve data at individual nearest grid points or within a user-defined rectangular area. Once a request has been successfully submitted and processed, a download link will be posted to the GitHub issue thread where the request was submitted. The download link will be available for up to seven days.

## Code

* [Zephyr](https://github.com/C2SM/zephyr/tree/main)

## Access

* Zephyr website to create requests: [Zephyr Website](https://zephyr.ethz.ch)
* Submitting Zephyr data requests: [Zephyr-request](https://github.com/C2SM/zephyr-request/issues/new/choose)

## Local Processing at IAC

If you have access to IAC servers, you can use Zephyr directly without submitting your request via the [Zephyr data request template](https://github.com/C2SM/zephyr-request/issues/new/choose). To do this, clone and install the tool in your workspace by following the instructions in the [Zephyr README](https://github.com/C2SM/zephyr/tree/main). Once installed, you can process requests created via the Zephyr website using the following command:

```shell
python launch_zephyr.py --json_path=/path/to/your/request --output_directory=/path/to/your/output/directory
```
