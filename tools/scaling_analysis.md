---
title: Scaling Analysis Tool
layout: default
parent: Tools
---

# Scaling Analysis Tool

The Scaling Analysis Tool automates the creation of multiple ICON run scripts
for a given experiment, varying the number of nodes to assess strong scaling
efficiency. Strong scaling efficiency measures how effectively the task's
performance improves with more nodes. It then analyses the experiment runs,
extracts timing data from log files, and generates summary plots that show
efficiency, node hours, and wallclock time in relation to the number of nodes used.

The tool comes in handy when applying for a
[production project at CSCS](https://www.cscs.ch/user-lab/allocation-schemes/production-projects),
as a technical report is required that must include the following information:

- Representative benchmarks and scaling
- Resource justification (annual node hours and disk space)

The plots created by the Scaling Analysis Tool can be used directly for the 
proposal.

## Code and Documentation

* [Scaling Analysis Tool](https://github.com/C2SM/scaling_analysis)
