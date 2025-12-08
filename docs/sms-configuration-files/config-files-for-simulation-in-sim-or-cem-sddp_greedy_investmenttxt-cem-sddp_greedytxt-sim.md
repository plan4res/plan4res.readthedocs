## Config files for simulation in SIM or CEM: sddp_greedy_investment.txt (CEM) / sddp_greedy.txt (SIM)

BlockSolverConfig \# exact type of the Configuration object

1 \# the BlockSolverConfig is a \"differential\" one

1 \# number of (the names of) Solver in this BlockSolverConfig

\# now all the names of the
Solver - - - - - - - - - - - - - - - - - - - - -

SDDPGreedySolver \# name of 1st Solver

1 \# number of ComputeConfig in this BlockSolverConfig

\# now all the ComputeConfig

\# 1st
ComputeConfig- - - - - - - - - - - - - - - - - - - - - - - - - - - -

\# ComputeConfig of the SDDPGreedySolver; it basically is the

\# ComputeConfig of the inner Solver, which is a BundleSolver

ComputeConfig \# exact type of the ComputeConfig object

1 \# f_diff == 0 ==\> all non-provided parameters are set to the default
value

\# f_diff == 1 ==\> all non-provided parameters are not changed

2 \# number of integer parameters

\# now all the integer parameters

intLogVerb 1 \# log verbosity

intUnregisterSolver 1 \# unregister the Solver of the inner Block after
solving it

0 \# number of double parameters

\# now all the double parameters

1 \# number of string parameters

\# now all the string parameters

strInnerBSC uc_solverconfig.txt \# BlockSolverConfig for the UCBlock 

