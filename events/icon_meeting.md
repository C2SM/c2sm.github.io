---
title: Quarterly Icon Meeting
layout: default
nav_order: 1
parent: Events
---
# 2023

## March 16
<details>
  <summary>Minutes</summary>
  Venue

### Hybrid: ETH Zurich (L 17.1) and via Zoom

### Participants (on-site)
Jonas Jucker (JJ), Annika Lauber (AL), Tamara Bandikowa (TB), Stefan Rüdisühli (SR), Jan Zibell (JZ), Guillaume Bertoli (GB), Athena Nghiem (AN), Andrea Stenke (AS), Doris Folini (DF), Jacobo Canton (JC), Boriana Chtirkova (BC)

### Participants (Zoom)
Michael Jähn (MJ), Tina Schnadt (TS), William Sawyer (WS), Joel Thanwerdas (JT), Dominik Brunner (DB), Nikolai Ponomarev (NP) , Arash Hamzehloo (AH), Lionel Constantin (LC)

_Minutes by Annika Lauber_

### Reports
Michael Jähn, Annika Lauber, Jonas Jucker
MJ welcomes all the participants to the meeting and presents the [news from C2SM about ICON](https://polybox.ethz.ch/index.php/s/i5g1gDDBhx99nxL).

JJ reports that the ECHAM physics support is being dropped and replaced by NWP physics. DB notes that HAM is still coupled to ECHAM. Confirmed by JJ.

WS asks if anyone knows the status of the ICON-Seamless project. The answer is no.

JJ reports on the transition to Spack v0.18.1. WS asks what happens if you source `/project/g110/spack/user/daint/spack/share/spack/setup_env.sh` and there is no global instance anymore. JJ: As long as there is no change on Daint-side the old spack-instance stays functional. After the next upgrade C2SM will remove this instance.

**Boriana Chtirkova**  
BC investigates how changes in the SST affect radiation variables. She plans to complete her PhD in September.

**Jacobo Canton**  
JC has currently returned to COSMO but plans to work with ICON again.

**Doris Folini**  
DF helps BC with her PhD project. They use ICON v2.6.4 because it’s closer to CMIP6, which is being used in BC’s work.

WS asks if it is possible to feed back their work into ICON v2.6.6. DS doesn’t know if this is possible. They are currently focused on BC finishing her PhD. DS suggests discussing offline.

**Andrea Stenke**  
AS plans to use ICON-ART for simulating trace elements such as selenium.

**Athena Nghiem**  
AN is working on implementing the cycling of the trace element arsenic (As) into ICON-ART and specifically now, she is currently working on implementing the atmospheric As chemistry into ART.

**Guillaume Bertoli**  
GB is working with a ML based radiation solver and is currently working on a paper.

**Jan Zibell**  
JZ is starting to use ICON for simulating the aquaplanet with v2.6.5. He looks into the sensitivity and variability of storm tracks.

**Stefan Rüdisühli**  
SR is supervising master’s thesis on time step effects.

**William Sawyer**  
WS has been working on the ICON development for a long time. He supports the port of the dycore to GPU and is happy to see that it’s bascially finished. He also works for EXCLAIM, where his main task is the modularization (or granularization) of ICON, i.e. adapting the interfaces in a way that you can pull out the Fortran version and plug it into the Python version. They are working on different schemes, like the diffusion, advection, dycore and microphysics schemes.

CSCS will transform to new CI system. Everything will have to be compiled and run in a container on the new machine. So they are working on getting ICON-EXCLAIM into a container.

DF asks if the hope is to have a stand-alone Python version of some aspects of ICON. WS confirms but adds that he cannot promise that the community will adopt it.

JJ asks if it is possible to access the compute nodes from inside the container when running the CI system. WS replies that the compute nodes have to be selected before running. JJ asks if this means that compute nodes needed for the run are wasted on the build. WS confirms and offers to talk more about this.

**Dominik Brunner et al.**  
DB shoes overview slide. They are working with ICON-ART and are interested in atmospheric composition related to the transport of tracers.

AH is working on porting ART to GPU. He is working on the OEM (online emission module). They are close to a 3x benchmark speedup.

DB reports on master student Michael Steiner’s work on ICON-ART. They are perturbing a set of prior anthropogenic emission fluxes and optimize them with the Ensemble Kalman Filter.

JT works on designing a tracer release experiment at global scale to try to benchmark chemistry-transport models like ICON-ART. DB is also reports on their work with VPRM where they simulate CO2. They look at the exchange of CO2 with the biosphere using a respiration model. They also simulate photosynthesis and are currently looking for a master student.

WS asks what other contributions to HAMAM are planned. DB reports that they are working with KIT as a project partner. The first task is to port the chemistry part to GPU.

WS asks if Sven Werchner plans to present the plan for next year. DB replied´s that he should contact Sven.

MJ asks when the GPU port of the VPRM model is planned. AH answers that this will be part of the GPU port for OEM. 
</details>

## 12 June
<details>
  <summary>Minutes</summary>

### Venue
Hybrid: ETH Zurich (L 17.1) and via Zoom

### Participants (on-site)
Michael Jähn (MJ), Jonas Jucker (JJ), Matthieu Leclair (ML), Annika Lauber (AL), Tina Schnadt (TS), Sebastian Schemm (SS), Nadja Omanovic (NO), Anurak Dipankar (AD), Stefan Rüdisühli (SR), Jan Zibell (JZ), Guillaume Bertoli (GB), Doris Folini (DF), Jacobo Canton (JC), Boriana Chtirkova (BC)

### Participants (Zoom)
Mikael Stellio (MS), William Sawyer (WS), Nikolai Ponomarev (NP), Marco Arpagaus (MA), Nicoletta Farabulllini (NF)

_Minutes by Annika Lauber_

### Reports
Michael Jähn, Annika Lauber, Jonas Jucker, Matthieu Leclair
MJ welcomes all the participants to the meeting and presents the [news from C2SM about ICON](https://polybox.ethz.ch/index.php/s/LK1JBcQMLenlHtA).

**Discussion about work on seaice port for ICON-CLM:**
AD asks how many static modes there are.

MJ responds that there are 6 static modes.

AD wonders if it would be possible to achieve the desired functionality with just one mode.

MJ agrees to investigate that possibility.

**Discussion about ongoing work on the two-moment microphysics scheme:**
MA asks how the ICON-HAM version of the two-moment microphysics scheme is different.

NO explains that the ICON-HAM version does not include graupel or hail.

MA inquires about when the split occurred.

NO clarifies that the split happened from the beginning, with Ulrike Lohmann and Axel Seifert having their own versions.

WS asks who is planning to use the two-moment microphysics scheme.

AL answers that currently the Atmospheric Physics group is using it but that there are more people interested.

MA expresses the intention to use the two-moment microphysics scheme as soon as it becomes fast enough. MA says that the Lohmann scheme lacks the most important feature, "hail," for the hailcast, which is why they need the version of Seifert.

SS mentions that another important user used to be the Atmospheric Dynamic group. He adds that the scheme is going to be the default option if it is fast enough.

WS brings up the topic of the Hackathon and asks if the restructuring is planned to be done during the Hackathon as that looks like a lot of work.

AL explains that C2SM applied for the CSCS Hackathon to work on the two-moment microphysics scheme and answers that the restructuring is one option they would like to investigate but there is also the option of using the explicit scheme or automatic inlining. They would like to investigate what is feasible during the Hackathon.

AD mentions that Cui Ruoyi is working on restructuring code and could be asked for advice.

**Sebastian Schemm**  
SS expresses gratitude for the support in porting of the aqua planet. He mentions that the original version was running on Daint but not on Euler, and that one compiler was more tolerant than the other. SS emphasizes that running the ensemble is worthwhile.

SS says that Aqua planet includes summer and winter with a new SST distribution, allowing for single and double ITCZ (Inter-Tropical Convergence Zone). They are investigating when the double ITCZ disappears.

**Nadja Omanovic**  
NO uses the two-moment microphysics scheme in LES (Large Eddy Simluation) mode at a 130m resolution, specifically over the Swiss plateau as part of the CLOUDLAB campaign. The goal is to mimic the experiment and improve precipitation forecasts based on the improved understanding.

**Anurak Dipankar**  
AD acknowledges introducing a bug in LES but confirms that it has been resolved.

**Boriana Chtirkova**  
BC is currently engaged global climate modeling, using CMIP6 and SST (Sea Surface Temperature).

**Guillaume Bertoli**  
GB mentions working their current work on machine learning and notes that it is currently extremely slow. They are in the final stages of wrapping up everything for a paper about the offline version.

**Stefan Rüdisühli**  
SR informs about their ongoing master thesis work, which focuses on studying the time-step effect on idealized cases.

**Jan Zibell**  
JZ presents [slides on the aqua planet ensemble](https://polybox.ethz.ch/index.php/s/mNGaggQAjHrAk8O), with the objective of studying storm tracks in response to global warming. They showcase the mean surface pressure over a 10-year period and highlight the distinct responses from the various ensemble members when warming the planet. JZ points out the different asymmetries using GPU and CPU.

AD adds that a longer mean reveals a recurring variability, resembling a cycle. They conducted a two-year run to observe this pattern.

SS notes that previous aqua planet simulations also exhibited asymmetry. The assumption of symmetry was made to provide better statistics. SS suggests that the asymmetry could be caused by the ICON grid.

AD dismisses the grid as the cause.

ML asks about the symmetry of perturbations.

AD explains that as long as turbulence is not triggered, the perturbations remain symmetric. However, once turbulence is triggered, they become asymmetric.

DF inquires if the CPU version also exhibits the same flip.

AD states that they are currently conducting tests to investigate that.

SS mentions that low-resolution aqua planets appeared symmetric, but small perturbations seemed to shift their symmetry.

MA suggests that obtaining an asymmetric result could be possible if they always start on the same date.

JZ explains that the start date is set to equinox, which positions is right above the equator.

**Mikael Stellio**  
MS provides an update on ICON-22, where he specifically focuses on the optimization of the ICON-HAM port for GPUs. MS presents [plots showcasing the results of a 6-hour simulation](https://polybox.ethz.ch/index.php/s/IzvePUPyrNImSMN). The main effort took place in the wet deposition part. The improvements made there have propagated to other schemes. Currently, MS is working on the two-moment microphysics scheme (Lohmann), which involves many calls of very small subroutines that are not efficient on GPUs.

**Marco Arpagaus**  
MA gives an update on ICON-22, mentioning the ongoing challenges they face. The machine they are working with has been causing difficulties, particularly with the restoration process, which leads to delays. As a result, the start of the pre-operational phase has been shifted to the beginning of October.

On the physics side, MA notes that they are currently running on Balfrin and admits to have being less careful with initialization. They discovered that the temperature of the soil was taken over from ICON-EU, resulting in heating in the lower soil. The orographies did not match, leading to elevated terrain that was too high, causing a bias of approximately 1K. But they hope that has been resolved now. MA expresses gratitude to JJ for their assistance in fixing the issue.

**William Sawyer**  
WS is trying to keep an overview. He starts with the [ICON port to LUMI](https://polybox.ethz.ch/index.php/s/IzvePUPyrNImSMN), which is being done by the Max Planck institute, CSC, and others. This endeavor turned into a significant project, and although they have something running, they face challenges as they rely on the Cray compiler, which has significant bugs. On a positive note, progress has been made, and they have a 1.25km test running. WS emphasizes the hope that HPE can fix the compiler bugs soon, preferably before LUMI gets decommissioned. However, there is still a lot of work to be done. To assist with the project, Cray has provided an entire person to help out.

MA asks about the client for this implementation.

WS responds that the first client is a Swedish team, although the name escaped him. Other users are interested in performing high-resolution runs.

MA inquires about the timeline.

WS admits that there is a bit of frustration and they had hoped to complete it during the acceptance phase. They acknowledge that relying on the Cray compiler was a big mistake.

MA asks if the Swedish team is part of the Climate Twins project.

WS clarifies that they are not.

WS then discusses the ICON consolidation project, which aims to refactor ICON, as it is currently a mess. The plan is to incrementally refactor it, which is challenging because every change has to pass all the buildbot. Thus it is a lot of work to integrate it.

WS mentions that they received the first Grace-Hopper node, which serves as the basis for ALPS. They have been working on benchmarking it to determine the energy usage of certain runs, such as ICON-CPU on Grace and ICON-GPU on Hopper. They are also considering DSL (Domain Specific Language) usage.

JJ asks for a date when the machines will be available to test workflows.

WS explains that the node they have now will not be accessible, but they will have access to an ALPS subset. They cannot provide an exact date at the moment but hope to have something available for the hackathon. Their best estimate is November or December, but they make no promises.

MA questions if the port to Grace-Hopper will be as challenging as the port to LUMI.

WS believes it should not be as challenging since they are working with a reliable (NVIDIA) compiler. However, the CPU side may present more difficulties. They promise to provide an update within two weeks.

**Nicoletta Farabulllini**  
NB mentions their efforts to complete the Python version and expresses hope that they can finish everything during this cycle.

**Nikolai Ponomarev**  
NP informs about their work on CO2 simulations in ICON-ART over Zurich. 
</details>