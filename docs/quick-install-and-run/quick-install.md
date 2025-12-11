## Quick Install

-   Clone the install repo in a chose directory, e.g. P4R_DIR:
 
 ```bash
   git clone <https://github.com/plan4res/install>   
   ```

-   Move the files \*.sh from in P4R_DIR, make them executable:

 ```bash
  chmod a+x \*.sh
   ```

-   Run the install script:

 ```bash
  ./plan4res_install.sh -S \$SOLVER -I \$installer -L \$LICENCE
   ```

 (\$SOLVER=CPLEX, GUROBI, SCIP or HiGHS ; \$installer is the installer file, only for CPLEX or GUROBI; \$LICENCE is the licence file, only for GUROBI; other options are possible, see detailed documentation)

If you wish to run plan4res from a different directory, e.g
P4R_DIR_LOCAL, move the script user_init_plan4res.sh in P4R_DIR_LOCAL
and run it as follows: 

 ```bash
   ./user_init_plan4res.sh -D P4R_DIR -S \$SOLVER
 ```
