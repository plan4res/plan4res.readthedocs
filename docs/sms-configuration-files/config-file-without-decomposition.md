### Config file without decomposition

BlockSolverConfig \# The name of the configuration

1 \# The BlockSolverConfig is \"differential\"

1 \# The number of Solvers

\# Now all the names of the Solvers

CPXMILPSolver

1 \# The number of ComputeConfigs

\# Now all the ComputeConfigs

\# 1st
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ComputeConfig \# Type of the object

1 \# differential

2 \# Number of integer parameters

intLogVerb 0

intRelaxIntVars 1 \# 1 =relax integer constraints

0 \# Number of double parameters

\# dblMaxTime 3600

3 \# Number of string parameters

strOutputFile uc.lp

CPXPARAM_CPUmask auto

CPXPARAM_WorkDir .

