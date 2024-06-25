---
title: Zephyr
layout: default
parent: Tools
---

# <img src="https://polybox.ethz.ch/index.php/s/Na2CeLPTzhtmh1T/download" width="110" valign="middle" alt="Zephyr"/>  Climate Data Extraction Tool

Zephyr is the climate data extraction tool developed by C2SM, serving as the backend processing engine for the [zephyr-frontend](https://github.com/C2SM/zephyr-frontend), which can be accessed through the [zephyr-website](https://zephyr.ethz.ch).


## Support status

The `main` branch is being tested upon creating a PR.

## Features

Requests are made via the [zephyr-frontend](https://github.com/C2SM/zephyr-frontend) and submitted using the [zephyr-request Data Request template](https://github.com/C2SM/zephyr-request/issues/new/choose). Zephyr supports a range of climate models and reanalysis datasets, including:

- CMIP5
- CMIP6
- CORDEX
- CORDEX ReKliEs
- ERA5
- ERA5 land
- CERRA
- CERRA land

Zephyr efficiently extracts both regional and global climate datasets, offering options for data retrieval at single nearest gridpoints or within a user-defined rectangular area.Upon successful submission and processing, users will receive an email notification containing a download link to the processed data, which will be available for up to seven days.

## Code

* [zephyr (backend engine)](https://github.com/C2SM/zephyr/tree/main)
* [zephyr-frontend](https://github.com/C2SM/zephyr-frontend)
* [zephyr-request](https://github.com/C2SM/zephyr-request)

## Access

Zephyr website to create requests: [zephyr Website](https://zephyr.ethz.ch)

## Local Processing at IAC

If you have access to IAC servers, you can use zephyr directly without submitting your request via the [zephyr-request Data Request template](https://github.com/C2SM/zephyr-request/issues/new/choose). To do this, clone and install the tool in your workspace by following the instructions in the [zephyr README](https://github.com/C2SM/zephyr/tree/main). Once installed, you can process requests created via the zephyr website using the following command:

```shell
python launch_zephyr.py --json_path=/path/to/your/request --output_directory=/path/to/your/output/directory
```