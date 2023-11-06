---
title: Scaling Analysis Tool
layout: default
parent: Tools
---

# Scaling Analysis Tool

When applying to CSCS for a production project, a technical report is required.
This report must include the following information:

- Representative benchmarks and scaling
- Resource justification (annual node hours and disk space)

The Scaling Analysis Tool automatically creates and launches various running scripts based on a given ICON experiment with different numbers of nodes to analyse the scaling. Once the experiment runs are complete, the tool reads the timings from the log files and produces summary plots of efficiency, node hours and wallclock against the number of nodes. These plots can then be used directly for the proposal.

## Code and Documentation

* [Scaling Analysis Tool](https://github.com/C2SM/scaling_analysis)
