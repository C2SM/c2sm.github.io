!!! construction "Page under construction"

    Information in this page is not yet complete nor final. It will be updated following the progress of

    - the Alps system deployment at CSCS
    - C2SM's adaptation to this new system

# The Alps System

Alps is a distributed HPC infrastructure managed by CSCS. Contrary to traditional HPC, it is composed of several logical units called vClusters (versatile clusters). From the users perspective, they play the role of a traditional HPC machine, each vCluster being tailored to the needs of a specific community. This setup also enables geographical distribution of vClusters which facilitates geo-redundancy. The main physical piece of Alps is hosted at CSCS in Lugano and a detailed description can be found [here :material-open-in-new:](https://www.cscs.ch/computers/alps){:target="_blank"}

## vClusters

The following vClusters are hosted at CSCS

| vCluster | Activity          | Share            |
|----------|-------------------|------------------|
| Daint    | User Lab          | ~ 800 GH nodes   |
| Clariden | Machine Learning  | ~ 800 GH nodes   |
| Santis   | Weather & Climate | ~ 400 GH nodes   |
| Tödi     | Testing           | few GH nodes     |
| Eiger    |                   | multi-core nodes |

## Introductory Workshop Material

As an introduction to the Alps infrastructure, the material of our [C2SM workshop "Switching to Alps"](../blog/posts/2024-07-02_switching_to_Alps.md) is available:

* Recording [:material-download: :material-open-in-new:](https://polybox.ethz.ch/index.php/s/oSxyJgTjyvJKX8B){:target="_blank"}{:target="_blank"}
* Slides presenting Alps, vClusters and Uenvs [:material-download: :material-open-in-new:](https://polybox.ethz.ch/index.php/s/jvtIYkBvHUSGZYD){:target="_blank"}{:target="_blank"}
* Slides for the integration of Uenvs in `spack-c2sm` [:material-download: :material-open-in-new:](https://polybox.ethz.ch/index.php/s/SWbYrOVRIprke60){:target="_blank"}{:target="_blank"}
