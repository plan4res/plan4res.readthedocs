# The plan4res environment

The plan4res environment is a container[How to explain containers in plain English | The Enterprisers Project](https://enterprisersproject.com/article/2018/8/how-explain-containers-plain-english). The plan4res container, p4r-envsee [CERL / Plan4Res / p4r-env · GitLab](https://gitlab.com/cerl/plan4res/p4r-env), can be installed in various environments (Linux, Windows, MacOS, CRAY). It provides a complete Linux environment with all dependencies already installed, allowing to run all plan4res modules. Once the environment is installed, the functional behavior will be the same on all kinds of systems. Computation time will depend on the computer's performance.

p4r-env is a singularity container, which means that it requires singularity to be installed.

Note that all components of plan4res can also run without this environment but it requires to install all dependencies manually, which can prove time-consuming and tricky.

The main softwares installed in p4r-env are:

- **StOpt **(see [Stochastic Control / StOpt · GitLab](https://gitlab.com/stochastic-control/StOpt)): a stochastic optimization library used for solving the Seasonal Storage Valuation (SSV) problem.

- **SMS++** (see [SMS++ / The SMS✛✛ Project · GitLab](https://gitlab.com/smspp/smspp-project)): modelling and optimization library including the 3 main solvers of plan4res in the OM4A toolbox.

- **A preprocessing tool** p4r-env/scripts/python/plan4res-scripts/ CreateInputPlan4res.py: this tool allows to create plan4res dataset out of long-term pluriannual energy system scenarios (e.g. from GENeSYS-MOD).

- **A formatting tool**, p4r-env/scripts/python/plan4res-scripts/ format.py,  (mandatory apart if you are creating the NetCDF input data files in the format required by SMS++ on your own); this tool creates input data file with the format required by SMS++ taking as inputs user friendly CSV and XLSX files.

- A **Postprocessing tool** p4r-env/scripts/python/plan4res-scripts/ PostTreatPlan4res.py: this tool transforms the files created by the solver (SMS++) into more user-friendly files and creates some synthetic results.

- **IAMC format transformation tools**: this tool, included in PostTreatPlan4res.py transforms the results from the postprocessing tool into files within the standardized IAMC format.

- A **Visualization tool**: creates graphs.

It is not necessary to launch the p4r-env environment to use plan4res (as launching it is embedded in the plan4res running scripts), but it may be useful in some cases. To launch the plan4res environment, go in the p4r-env repository and type bin/p4r (on Windows, use Git Bash to do so). This will start a shell in the plan4res containerized environment such as:

[P4R-ENV] /…/P4R_DIR/p4r-env >

You then have a Linux installation, based on Debian. Basic softwares and utilities are already installed and ready to use, in particular all the dependencies which are necessary for plan4res, in particular python3 and the packages used by the plan4res python scripts.