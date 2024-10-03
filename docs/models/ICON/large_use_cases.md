# Large Use Cases

ICON is a complex piece of software and even more so is ICON-exclaim that builds on top of it. Troubleshooting large scale configurations can therefore be tedious, which is why we developed a procedure to build large production ICON configurations in the most robust way possible.

The overall philosophy is to build a series of gradually increasing complexity setups from a small scale ICON test case to the full production configuration. Even if it could feel like an overhead when starting the whole process, C2SM's core team is there to assist you in this journey and it will pay off in the end!

## 1. Small Scale Test Case
Set up an ICON test case (either ICON-c2sm or ICON-nwp) integrated in the ICON testing infrastructure with a low number of grid points and a few time steps. The idea here is to test the code path of the final setup and identify potential issues coming from upstream source code.

### Test case setup

### Local testing

## 2. Activate Test in a CI Pipeline

## 3. Intermediate Scale Tests
The purpose here is to, still with a *standard* ICON, catch issues that could arise when increasing space and time scales. Because we still would like to be able to debug without waiting hours in the queue, it could be wise to come up with setups using few nodes and testing either/or: 

- approaching the memory limits of the nodes
- long simulations

## 4. Full scale test with *standard ICON*

## 5. Switch to ICON-exclaim

