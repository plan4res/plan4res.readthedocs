# Installing plan4res

This section describes how to install plan4res on different systems:

- (recommended) Linux
- Windows
    - (recommended) with WSL
    - (not recommended) with Vagrant
- "Server" mode (on Linux)


## Summary of installation (Linux or Windows WSL)

- **Clone the install repo** in a chose directory, e.g. P4R_DIR:
```bash
git clone https://github.com/plan4res/install
```

- **Move the bash files to P4R_DIR and make them executable:**
```bash
mv P4R_DIR/install/*.sh P4R_DIR/
chmod a+x P4R_DIR/*.sh
```

- **Run the install script:**
```bash
./plan4res_install.sh with -S <SOLVER> -I <installer> -L <LICENCE> 
```

where:
    
    - SOLVER=CPLEX, GUROBI, SCIP or HiGHS; 
    
    - installer= installer file for CPLEX or GUROBI 
    
    - LICENCE=licence file for GUROBI 

     
- **If you wish to run plan4res from a different directory**, e.g P4R_DIR_LOCAL, move the script user_init_plan4res.sh in P4R_DIR_LOCAL and run it as follows:
```bash
mv P4R_DIR/user_init_plan4res.sh P4R_DIR_LOCAL/
./user_init_plan4res.sh -D P4R_DIR -S $SOLVER
```

## Important notice
After proceeding to the install of plan4res, the software is installed in P4R_DIR. The datasets should be stored in the subdirectory data of P4R_DIR_LOCAL. Depending of your choices in the install process, P4R_DIR and P4R_DIR_LOCAL may be identical or different. (in particular if you are installing on a server, the software will be in P4R_DIR, and each user will have his P4R_DIR_LOCAL directory, configured by the user_init_plan4res.sh script)

The installation process is detailed in the following subsections.

```warning
It is recommended to install plan4res with the full environment (p4r-env), which is embedded in a singularity container. This requires at least 3Gb. In case you do not have this available, you may install plan4res without the environment, but it requires installing all the dependencies first, which may sometimes be quite tricky.
```

```warning
Plan4res requires use of external solver, which can be CPLEX, GUROBI, SCIP or HiGHS. If you do have a CPLEX or GUROBI license, it is recommended to use one of these software. If not, it is recommended to use HiGHS. 
```

```warning
If you wish to use CPLEX, you must have a CPLEX linux installer available, such as cplex_studio2211.linux_x86_64.bin, referenced as cplex_studioXXXXXX.bin below.
```

```warning
If you wish to use GUROBI, you must have a GUROBI linux installer, sur as gurobi11.0.1_linux64.tar.gz and a gurobi license file: gurobi.lic.
```

```warning
Before starting the install, create an empty directory (for example P4R_DIR) where you want to install plan4res. **It should not contain special characters or whitespaces!**
```

Once installed, the plan4res environment will appear as described in section 

