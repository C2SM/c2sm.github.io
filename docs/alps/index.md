# The Alps System

Alps is a distributed HPC infrastructure managed by CSCS. Contrary to traditional HPC, it is composed of several logical units called vClusters (versatile clusters). From the users perspective, they play the role of a traditional HPC machine, each vCluster being tailored to the needs of a specific community. This setup also enables geographical distribution of vClusters which facilitates geo-redundancy. The main physical piece of Alps is hosted at CSCS in Lugano and a detailed description can be found at [their documenation :material-open-in-new:](https://docs.cscs.ch/alps/){:target="_blank"}.

## vClusters

The following table shows current clusters distribution on Alps at CSCS (only C2SM relevant clusters are shown).

| vCluster | Activity          | Share            |
|----------|-------------------|------------------|
| Santis   | Weather & Climate | ~ 500 GH nodes   |
| Daint    | User Lab          | ~ 600 GH nodes   |
| Clariden | Machine Learning  | ~ 800 GH nodes   |
| Eiger    |                   | multi-core nodes |

*GH = Grace Hopper*

More information about clusters on Alps is available on the [official CSCS documentation :material-open-in-new:](https://docs.cscs.ch/alps/clusters/#alps-clusters){:target="_blank"}.

## Support by CSCS

General information about access, file systems, vClusters, user environments and much more can be found at the [CSCS documentation :material-open-in-new:](https://docs.cscs.ch/){:target="_blank"}.

To contact CSCS staff directly, users can join their dedicated [Slack workspace :material-open-in-new:](https://cscs-users.slack.com){:target="_blank"}, with dedicated channels for each vCluster. 


## Introductory Workshop Material

As an introduction to the Alps infrastructure, the material of our [C2SM workshop "Switching to Alps"](../posts/2024-07-02_switching_to_Alps.md) from August 12, 2024 is available:

- [Recording :material-download:](https://polybox.ethz.ch/index.php/s/oSxyJgTjyvJKX8B){:target="_blank"}<br>
- [Slides presenting Alps, vClusters and Uenvs :material-download:](https://polybox.ethz.ch/index.php/s/jvtIYkBvHUSGZYD){:target="_blank"}<br>
- [Slides for the integration of Uenvs in `spack-c2sm` :material-download:](https://polybox.ethz.ch/index.php/s/SWbYrOVRIprke60){:target="_blank"} 
