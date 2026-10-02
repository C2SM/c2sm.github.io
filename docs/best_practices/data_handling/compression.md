# Data Compression

Compression of data can considerably reduce disk space usage and the time for data transfer. Compressing data can be a lossless or lossy process. Lossless compression enables the restoration of a file to its original state, without the loss of a single bit of data. Lossy compression permanently eliminates bits of data that are redundant, unimportant or imperceptible. Lossy compression is useful for graphics, audio, video and images, where the removal of some data bits has little or no discernible effect on the representation of the content. Depending on the use case, lossy compression can also be applied to measured or simulated data.

Compression and decompression use CPU and memory resources and can have a negative impact on read and write performance. Ideally, data that is not accessed much should be compressed. It is highly recommended for data that is stored in an archive.

Compressed files, like *.gz, *.zip, *.bz files normally need to be uncompressed before they can be used again. But there are alternatives. Linux commands, like zless, zcat, zdiff, zgrep, etc. can handle compressed files on the fly. The same is true for file access from scripting languages like R, python, Matlab or IDL.

## Standard lossless methods
   * netcdf4 library and all the tools compiled with netcdf4 support seamlessly integrate compression
   * We recommend lossless compressed netcdf4 files for many cases
      * Lossless compression in netcdf4 is based on the zlib library. The level of compression can be adjusted between 1 (least aggressive) and 9 (most aggressive compression). The minimum compression requires moderate CPU and memory resources and is sufficient for most purposes. Higher levels should usually result in smaller compressed files, but come with larger processing costs when packing/unpacking. For fine tuning netcdf compression, it is possible to set the size of data chunks on which the compression operates. These chunks should match typical data blocks that have to be accessed at the same time. Furthermore, the shuffling option is often a possibility to further reduce data size. Finally, it is advantageous to remove unneeded unlimited dimensions from a netcdf file as they may reduce the efficiency of compression.
   * On IAC systems the script nczip is installed. The nczip script is a wrapper around ncks and can be used to compress and decompress a netcdf file or a bunch of netcdf files in a folder. The command ncks is part of NCO.
   * Good results can also be obtained with the nccopy command which is part of every netcdf4 installation. nccopy allows setting the compression level, shuffling option, and even chunk sizes.
   * Another alternative to nczip is nccompress
   * Climate Data Operators (cdo) can compress netCDF, but offers limited chunking options compared to NCO
   * Compression details can also directly be set in source code when creating netcdf variables (e.g., FORTRAN, R, python interfaces)

## Lossy algorithms
   * This is still an area where people experiment. We cannot make recommendations at this point
   * ncks also supports three lossy compression algorithms. More information can be found in the NCO User Guide
   * Python users should have a look at netcdf4-python or xarray which support lossless and lossy compression. The latter is supported by defining a least significant digit. The least significant digit is the power of ten of the smallest decimal place in the data that is a reliable value. All information below this threshold is cropped from the data before saving and cannot be restored.
   * Check the dedicated dc-toolkit that helps exploring data compression techniques on your data
   * One always needs to be aware of what might be lost. In general, lossy compression should result in smaller files than lossless compression.
