## Quick Install

-   Clone the install repo in a chose directory, e.g. P4R_DIR:
  '''
         git clone <https://github.com/plan4res/install>
  '''

-   Move the files \*.sh from in P4R_DIR, make them executable:
  '''
          chmod a+x \*.sh
  '''
-   Run the install script:
  '''
          ./plan4res_install.sh -S \$SOLVER -I \$installer -L \$LICENCE
   (-S \$SOLVER with \$SOLVER=CPLEX, GUROBI, SCIP ; else it will use
    HiGHS ; -I \$installer if \$SOLVER is CPLEX or GUROBI; -L \$LICENCE if \$SOLVER is GUROBI; other options are possible, see detailed documentation)
  '''

If you wish to run plan4res from a different directory, e.g
P4R_DIR_LOCAL, move the script user_init_plan4res.sh in P4R_DIR_LOCAL
and run it as follows: 
  '''
     ./user_init_plan4res.sh -D P4R_DIR -S \$SOLVER
  '''

