# The plan4res commands: p4r and sp4r

p4r and sp4r are available for using them after installing and configuring plan4res. They allow to run all modules of plan4res (installed in P4R_DIR) from any directory of the user account configured by user_init_plan4res. Independently of the directory in which you are located when running p4r or sp4r, both commands will consider that the datasets are in P4R_DIR_LOCAL/data and the results will also be written in this directory.

The p4r command allows to run all modules of plan4res, without using parallelization.

**Usage**:

p4r <runtype> <dataset> -M <option1> -m <option2> -o <Dir> -H [save] -S [NumberIterationsFirstStep] [CheckConvEachXIter] -E [epsilon] -L [NumberOfCemIterations] [MaxNumberOfLoops] -D [distance] -U <configfile>"

where:

- **runtype** can be: CLEAN, CREATE, FORMAT, SSV, SIM, CEM, SSVandSIM, SSVandCEM, POSTTREAT:

  - CLEAN: remove all results and revert to initial csv files if necessary (ie if CEM -L was launched)

  - CONFIG: read config file in settings/plan4res_settings.yml and print to screen

  - CREATE: creates a plan4res dataset (csv files) from a IAMC dataset, including data for capacity expansion (with -M invest) or not (with -M simul)

  - FORMAT: creates netcdf files for SMS++, for further run of SSV (with -M optim) based on a dataset with capacity expansion (with -m invest) or not (with -m simul), or for further run of SIM (with -M simul) or for further run of CEM (with -M invest) or for further run of SSV in the case when CEM was already launched (with -M postinvest)

  - SSV: runs the sddp_solver for computing bellman values. With -M $option, the results of SSV will be in results_$option ; if not they will be in results_optim

  - SIM: run simulations using BellmanValues in results_simul, outputs results to results_simul

  - CEM: runs capacity expansion and simulation; outputs results in results_invest; without the option -L, CEM will use BellmanValues in results_invest; with the option -L, BellmanValues will be computed at each iteration of the loop.

  - POSTTREAT: runs posttreatment of results in results_simul with option -M simul, or in results_invest with option -M invest

  - SSVandSIM: runs in sequence SSV then SIM, outputs results in results_simul. Handles creation of NetCDF if used with option -F, and creation of csv files if used with option -C; runs the POSTTREAT in the end.

  - SSVandCEM: runs in sequence SSV then CEM, outputs results in results_invest. Handles creation of NetCDF if used with option -F, and creation of csv files if used with option -C; runs the POSTTREAT in the end.

- **dataset** is the Name of the dataset (also the name of the dataset directory in data/)

- **-o [Dir] (or --out [Dir])** is optionnal ; Dir is the name of a subdir of data/dataset where results will be written; -o is usable for SSV, CEM, SIM, SSVandSIM, SSVandCEM, POSTTREAT

- **-C or --create** is optional: in that case the dataset (csv files) will be created; -C is usable for FORMAT, SSV, SIM, CEM, SSVandCEM, SSVandSIM, CEMloopSSV

- **-F or --format** is optional: in that case the NetCDF[Unidata | NetCDF](https://www.unidata.ucar.edu/software/netcdf/) dataset for SMS++ will be created; -F is usable for SSV, SIM, CEM (without option -L), (for SSVandCEM, SSVandSIM, CEM -L, creation of netcdf files is mandatory)

- **-H or --hotstart** is optional: in that case a first SSV or CEM run must have been performed; The current run will restart from the results of the previous run ; -H is usable for SSV, CEM ; **-H save** is only used with CEM, meaning that not only the previous solution will be used but also the previous state

- **-S or --steps** is optional: in that case SSV will be ran in 2 steps (first step with convergence checks every 10 iterations, second with checks every iteration); -S is usable for SSV, CEM; The arguments **NumberIterationsFirstStep** (max number of iterations of the first step) and **CheckConvEachXIter** (convergence is checked after CheckConvEachXIter SSV iterations) can be provided either in the command line (-S NumberIterationsFirstStep CheckConvEachXIter**)** or in the plan4res_settings.yml config file (an example of this file is available in toyDataset/settings/plan4res_settings.yml). If the parameters are available in both plan4res_settings.yml and as arguments of the p4r command, the arguments of the command line will be used.

- **-L or --loopssv** is optional: in that case CEM will be launched using a loop of SSV/CEM until convergence; -L is usable for CEM; The arguments **NumberOfCemIterations** (max number of iterations in each run of CEM) and **MaxNumberOfLoops** (max number of iterations SSV/CEM) can be provided either in the command line (-L NumberOfCemIterations MaxNumberOfLoops) or in the plan4res_settings.yml config file (an example of this file is available in toyDataset/settings/plan4res_settings.yml). If the parameters are available in both plan4res_settings.yml and as arguments of the p4r command, the arguments of the command line will be used.

- **-E or --epsilon** is optional: it is the convergence criteria for CEM -L (default 0.01) ; -E is usable for CEM; The argument **epsilon** (convergence criteria of CEM) can be provided either in the command line (-E epsilon) or in the plan4res_settings.yml config file (an example of this file is available in toyDataset/settings/plan4res_settings.yml). If the parameters are available in both plan4res_settings.yml and as arguments of the p4r command, the arguments of the command line will be used.

- **-D or --distance** is optional: it allows to choose which convergence test is used when running CEM with option -L; -D is usable for CEM -L; The argument **distance** (kind of one of the convergence tests) can be provided either in the command line (-E epsilon) or in the plan4res_settings.yml config file (an example of this file is available in toyDataset/settings/plan4res_settings.yml). If the parameters are available in both plan4res_settings.yml and as arguments of the p4r command, the arguments of the command line will be used; distance can be 2 (distance between initial capacity and invested capacity is used for checking convergence) or 3 (distance between cost of investment solution at last 2 iterations is used for checking convergence); if not provided, distance 2 is used.

- **-U or –scenarios** is optional: it allows to run CEM in sequence on different lists of scenarios; -U is usable for CEM; The lists of scenarios must be in the file **configfile** , which must be a text file, and must be provided in the command line (-U configfile). An Example is available in the toyDataset/settings/list_scenarios.txt

- **-M or –mode1** is optional. The chosen option must be provided in command line (-M option1). If not provided, it will behave as if -M simul was provided. -M is useable for CREATE, FORMAT, SSV and POSTTREAT. For CREATE, option1 can be simul or invest (with simul, CREATE will compute a dataset for a simulation run, with invest, CREATE will compute a dataset for a capacity expansion run). For FORMAT, option1 can be optim (for creating NetCDF files for SSV), simul (for creating NetCDF files for SIM), invest (for creating NetCDF files for CEM) or postinvest (for creating NetCDF files for SSV and updating csv files after a CEM run)

- **-m or –mode2** is optional. The chosen option must be provided in command line (-m option2). If not provided, it will behave as if -m simul was provided. -m is useable for FORMAT in the case where option1 is optim: option2 can be invest (for creating NetCDF files for SSV based on the csv files in csv_invest) or simul (for creating NetCDF files for SSV based on the csv files in csv_simul

p4r -h or --help display some help

sp4r has the same “usage” as p4r apart from a mandatory additional argument: **-n or –nodes** followed by the number of nodes on which to run plan4res.

It will create the file this_sbatch_p4r.sh and run it with sbatch.

Note that the plan4res scripts will manage the configuration of the arguments requested by sbatch such as the number of tasks, …… depending on the module which is ran. Within a workflow of different modules, these parameters are adapted, and each module is launched with srun.