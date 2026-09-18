# Data Handling

## C2SM data management guidelines
[C2SM Data Management Recommendations 2020 :material-open-in-new:](https://polybox.ethz.ch/index.php/s/pyZRPF4FfJJ47g1){:target="_blank"}

## Data compression
Compression of data can considerably reduce disk space usage and the time for data transfer. Compressing data can be a lossless or lossy process. Lossless compression enables the restoration of a file to its original state, without the loss of a single bit of data. Lossy compression permanently eliminates bits of data that are redundant, unimportant or imperceptible. Lossy compression is useful for graphics, audio, video and images, where the removal of some data bits has little or no discernible effect on the representation of the content. Depending on the use case, lossy compression can also be applied to measured or simulated data.

Compression and decompression use CPU and memory resources and can have a negative impact on read and write performance. Ideally, data that is not accessed much should be compressed. It is highly recommended for data that is stored in an archive.

Compressed files, like *.gz, *.zip, *.bz files normally need to be uncompressed before they can be used again. But there are alternatives. Linux commands, like zless, zcat, zdiff, zgrep, etc. can handle compressed files on the fly. The same is true for file access from scripting languages like R, python, Matlab or IDL.

   # Standard lossless methods
   * netcdf4 library and all the tools compiled with netcdf4 support seamlessly integrate compression
   * We recommend lossless compressed netcdf4 files for many cases
      - Lossless compression in netcdf4 is based on the zlib library. The level of compression can be adjusted between 1 (least aggressive) and 9 (most aggressive compression). The minimum compression requires moderate CPU and memory resources and is sufficient for most purposes. Higher levels should usually result in smaller compressed files, but come with larger processing costs when packing/unpacking. For fine tuning netcdf compression, it is possible to set the size of data chunks on which the compression operates. These chunks should match typical data blocks that have to be accessed at the same time. Furthermore, the shuffling option is often a possibility to further reduce data size. Finally, it is advantageous to remove unneeded unlimited dimensions from a netcdf file as they may reduce the efficiency of compression.
   * On IAC systems the script nczip is installed. The nczip script is a wrapper around ncks and can be used to compress and decompress a netcdf file or a bunch of netcdf files in a folder. The command ncks is part of NCO.
   * Good results can also be obtained with the nccopy command which is part of every netcdf4 installation. nccopy allows setting the compression level, shuffling option, and even chunk sizes.
   * Another alternative to nczip is nccompress
   * Climate Data Operators (cdo) can compress netCDF, but offers limited chunking options compared to NCO
   * Compression details can also directly be set in source code when creating netcdf variables (e.g., FORTRAN, R, python interfaces)

   # Lossy algorithms
   * This is still an area where people experiment. We cannott make recommendations at this point
   * ncks also supports three lossy compression algorithms. More information can be found in the NCO User Guide
   * Python users should have a look at netcdf4-python or xarray which support lossless and lossy compression. The latter is supported by defining a least significant digit. The least significant digit is the power of ten of the smallest decimal place in the data that is a reliable value. All information below this threshold is cropped from the data before saving and cannot be restored.
   * Check the dedicated dc-toolkit that helps exploring data compression techniques on your data
   * One always needs to be aware of what might be lost. In general, lossy compression should result in smaller files than lossless compression.

## ETH Links
   * [Research Data at ETH Zurich :material-open-in-new:](https://ethz.ch/staffnet/en/service/a-to-z/research-data.html){:target="_blank"}
   * [New Guidelines for Research Data Management :material-open-in-new:](https://ethz.ch/staffnet/en/news-and-events/internal-news/archive/2022/10/new-guidelines-for-research-data-management.html){:target="_blank"} -> [PDF :material-open-in-new:](https://rechtssammlung.sp.ethz.ch/Dokumente/414.2en.pdf){:target="_blank"}
   * [Forschungsdatenmanagement und Datenerhalt :material-open-in-new:](https://documentation.library.ethz.ch/display/DD/Forschungsdatenmanagement+und+Datenerhalt){:target="_blank"}
   * [ETH Guidelines for Research Integrity :material-open-in-new:](https://doi.org/10.3929/ethz-b-000179298){:target="_blank"}
   * [ETH Research Collection :material-open-in-new:](https://www.research-collection.ethz.ch){:target="_blank"}
   * [Add your ORCID ID to your ETH account :material-open-in-new:](https://unlimited.ethz.ch/spaces/RC/pages/194119877/Author+profil+and+assign+ORCID+iD){:target="_blank"}
   * [ETH Guidelines for data management plans :material-open-in-new:](https://unlimited.ethz.ch/pages/viewpage.action?pageId=194127962){:target="_blank"}

## ETH Contacts
   * Data management plans: Digital Curation Office, ETH Library, ETH Zurich, [ETH Digital Curation Webpage :material-open-in-new:](https://library.ethz.ch/en/collections-and-archives/archiving/digital-long-term-preservation/digital-curation-services.html){:target="_blank"}
   * Research Collection: Barbara Hirschmann, ETH Research Collection, ETH Library, ETH Zurich, [ETH Research Collection Webpage :material-open-in-new:](https://library.ethz.ch/en/researching-and-publishing/publishing-research/publishing-in-the-research-collection.html){:target="_blank"}
   * openBIS software: Dr. Caterina Barillari, ETH SIS, [ETH Personal Page :material-open-in-new:](https://www.ethz.ch/en/the-eth-zurich/organisation/departments/informatikdienste/personen/person-detail.html?persid=185758){:target="_blank"}

## Data repositories
   * [C2SM datasets](../datasets/index.md)
   * [Directory of data repositories :material-open-in-new:](https://www.re3data.org){:target="_blank"}
   * [ETH research collection :material-open-in-new:](https://www.research-collection.ethz.ch){:target="_blank"}
   * [Zenodo :material-open-in-new:](https://zenodo.org){:target="_blank"}
   * [IAC data pool :material-open-in-new:](http://data.iac.ethz.ch/atmos/){:target="_blank"}
   * [IAC gitlab :material-open-in-new:](https://git.iac.ethz.ch){:target="_blank"}

## Open access journals
   * [Directory of open access journals :material-open-in-new:](https://www.doaj.org){:target="_blank"}
   * [Check specific journal access policy :material-open-in-new:](https://openpolicyfinder.jisc.ac.uk/){:target="_blank"}

## Funding agencies open access policies
   * [Open research data @SNSF :material-open-in-new:](https://www.snf.ch/en/dMILj9t4LNk8NwyR/topic/open-research-data){:target="_blank"}
   * [Check specific funder archiving mandates :material-open-in-new:](https://openpolicyfinder.jisc.ac.uk/){:target="_blank"}

## Licensing
   * [Advices on how to license research data :material-open-in-new:](http://www.dcc.ac.uk/resources/how-guides/license-research-data){:target="_blank"}
   * [Creative commons licenses :material-open-in-new:](https://creativecommons.org){:target="_blank"}
   * [Open data commons licenses :material-open-in-new:](https://opendatacommons.org){:target="_blank"}
   * [GNU licenses :material-open-in-new:](https://www.gnu.org/licenses/gpl.html){:target="_blank"}
   * [Open definition for data :material-open-in-new:](https://opendefinition.org){:target="_blank"}
   * [Creative commons and open science :material-open-in-new:](https://zenodo.org/record/840652#.XHm1Vi17TOQ){:target="_blank"}
   * [Copyleft definition :material-open-in-new:](https://en.wikipedia.org/wiki/Copyleft){:target="_blank"}
   * [Why avoiding non-commercial licenses? :material-open-in-new:](https://freedomdefined.org/Licenses/NC){:target="_blank"}
   * [Advices on how to cite datasets :material-open-in-new:](http://www.dcc.ac.uk/resources/how-guides/cite-datasets){:target="_blank"}
   * [SPDX (standard for easy sofware licensing) :material-open-in-new:](https://spdx.org/ids){:target="_blank"}

## Help on improving NetCDF metadata
   * [IAC internal documentation on NetCDF in general :material-open-in-new:](https://wiki.iac.ethz.ch/IT/LinuxNetCDF){:target="_blank"} (!with IAC login only)
   * [Climate and Forecast (CF) conventions :material-open-in-new:](https://cf-convention.github.io/){:target="_blank"}
   * [Python CF checker :material-open-in-new:](https://github.com/cedadev/cf-checker){:target="_blank"}
   * [Controlled Vocabularies (CVs) for use in CMIP6 :material-open-in-new:](https://wcrp-cmip.github.io/CMIP6_CVs/){:target="_blank"}


