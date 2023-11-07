---
title: Scaling Analysis Tool
layout: default
parent: Tools
---

# Scaling Analysis Tool

The Scaling Analysis Tool automatically creates and launches several ICON run
scripts based on a given experiment with different numbers of nodes to
analyze the strong scaling. Once the experiment runs are complete,
the tool reads the timings from the log files and produces summary plots of 
efficiency, node hours and wallclock against the number of nodes.

The tool comes in handy when applying for a
[production project at CSCS](https://www.cscs.ch/user-lab/allocation-schemes/production-projects),
as a technical report is required that must include the following information:

- Representative benchmarks and scaling
- Resource justification (annual node hours and disk space)

The plots created by the Scaling Analysis Tool can be used directly for the 
proposal.

## Code and Documentation

* [Scaling Analysis Tool](https://github.com/C2SM/scaling_analysis)
