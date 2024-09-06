!!! construction "Page under construction - last update: 2024-09-06"

    Information in this page is not yet complete nor final. It will be updated following the progress of

    - the Alps system deployment at CSCS
    - C2SM's adaptation to this new system

# The Alps System

Alps is a distributed HPC infrastructure managed by CSCS. Contrary to traditional HPC, it is composed of several logical units called vClusters (versatile clusters). From the users perspective, they play the role of a traditional HPC machine, each vCluster being tailored to the needs of a specific community. This setup also enables geographical distribution of vClusters which facilitates geo-redundancy. The main physical piece of Alps is hosted at CSCS in Lugano and a detailed description can be found at [their website :material-open-in-new:](https://www.cscs.ch/computers/alps){:target="_blank"}.

## vClusters

The following vClusters are hosted at CSCS:

| vCluster | Activity          | Share            |
|----------|-------------------|------------------|
| Daint    | User Lab          | ~ 800 GH nodes   |
| Clariden | Machine Learning  | ~ 800 GH nodes   |
| Santis   | Weather & Climate | ~ 400 GH nodes   |
| Tödi     | Testing           | few GH nodes     |
| Eiger    |                   | multi-core nodes |

*GH = Grace Hopper*

## Early Access

For getting access to the vCluster dedicated to testing ([Tödi](vclusters.md/#tödi){:target="_blank"}), CSCS offers [Preparatory Projects :material-open-in-new:](https://www.cscs.ch/user-lab/allocation-schemes/preparatory-projects){:target="_blank"}. 

## Support by CSCS

To contact CSCS staff directly, users can join their dedicated [Slack channel :material-open-in-new:](https://cscs-users.slack.com){:target="_blank"}.

## File Systems

!!! note "TODO"

    - [ ] `/users`, `/store` and `/scratch`
    - [ ] reserved space per vClsuter vs shared space
    - [ ] ...

## Introductory Workshop Material

As an introduction to the Alps infrastructure, the material of our [C2SM workshop "Switching to Alps"](../blog/posts/2024-07-02_switching_to_Alps.md) from August 12, 2024 is available:

- [Recording :material-download:](https://polybox.ethz.ch/index.php/s/oSxyJgTjyvJKX8B){:target="_blank"}<br>
- [Slides presenting Alps, vClusters and Uenvs :material-download:](https://polybox.ethz.ch/index.php/s/jvtIYkBvHUSGZYD){:target="_blank"}<br>
- [Slides for the integration of Uenvs in `spack-c2sm` :material-download:](https://polybox.ethz.ch/index.php/s/SWbYrOVRIprke60){:target="_blank"} 
