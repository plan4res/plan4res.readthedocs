# Installation without p4r-env

It is possible to install plan4res without the p4r-env environment. This requires installing all the dependencies first. It is possible to install on Linux (Ubuntu or Debian), MacOS or Windows

Python3 must be the default version of python

The following python packages must be installed (e.g. with pip-install):

*setuptools, openpyxl, scipy, pandas, pyyaml, matplotlib, geopandas, fiona, descartes, shapely, pillow, mapclassify, numpy, requests, requests-toolbelt, rtree, pygeos, wheel, netCDF4, pyam-iamc*

The requirements for installing SMS++ are described in the SMS++ gitlab repo[https://gitlab.com/smspp/smspp-project/-/wikis/Installing-SMS++#requirements](https://gitlab.com/smspp/smspp-project/-/wikis/Installing-SMS++#requirements). Their installation may be included in the installation script of SMS++, but, in particular in the case of a Linux installation, the version which would be installed depend on which linux OS is installed (and which version), and thus may be too old. (This in particular happens on linux Debian::bullseye). In that case you should install manually a more recent version.

For each SOFTWARE install, on linux, PATH and LD_LIBRARY_PATH must be updated to include $SOFTWARE_PATH/mpi and $SOFTWARE_PATH/mpi/lib. For BOOST, the variable $BOOST_PATH must also be set.

- **Boost**[https://www.boost.org/more/getting_started/unix-variants.html](https://www.boost.org/more/getting_started/unix-variants.html) **(minimum version 1.87).**

- **OpenMPI**[Open MPI: Open Source High Performance Computing](https://www.open-mpi.org/) **(minimum version 3.1.4) OR MPICH**[MPICH | High-Performance Portable MPI](https://www.mpich.org/) **(minimum version 3.3.2)**

- **NETCDF**[netCDF Downloads](https://downloads.unidata.ucar.edu/netcdf/) **(minimum version 4.9.2) and NETCDFCXX (minimum version: 4.3.1).**

- **Eigen**[libeigen / eigen · GitLab](https://gitlab.com/libeigen/eigen) **(minimum version 3.3.7)**

- **Cmake**[Kitware/CMake: Mirror of CMake upstream repository](https://github.com/Kitware/CMake) **(minimum version 3.28.1)**

Mkdir P4R_DIR (can be any directory name)cd P4R_DIRgit clone [https://github.com/plan4res/install](https://github.com/plan4res/install)chmod a+x *.sh./plan4res_install.sh -X -S <SOLVER> [-D <solverpath>] [-I <installer>] [-L <license>] [-v <version>] [-M <mpi>]Where:

- SOLVER is the chosen solver among CPLEX, GUROBI, SCIP, HiGHS. If this option is not provided, HiGHS is chosen

- solverpath is to be provided if the solver is already installed in your system. In that case you need to provide the path where it is installed

  - for CPLEX: solverpath is where you find e.g. cplex/bin and cplex/lib

  - for GUROBI: solverpath is where you find e.g. gurobi1101/linux64 and gurobi1101/gurobi.lic is version 11.01 is installed

  - for HiGHS: solverpath is where you find bin, include and lib

- Installer is the installer file for CPLEX of Gurobi, the -I option must only be provided when CPLEX or GUROBI are chosen

- License is the license file, only for GUROBI

- Version is the solver version, only for SCIP

- mpi is the chosen MPI version among MPICH and OpenMPI. If this option is not provided, OpenMPI is chosen.

Create a P4R directory somewhere. Create a sub directory BUILD in P4R. Once everything has been installed you can delete P4R/BUILD as this directory will be used for compiling everything.

Python3 must be the default version of python

The following python packages must be installed:

*setuptools, openpyxl, scipy, pandas, pyyaml, matplotlib, geopandas, fiona, descartes, shapely, pillow, mapclassify, numpy, requests, requests-toolbelt, rtree, pygeos, wheel, netCDF4, pyam-iamc*

**Install Visual Studio 2022** (or later) from  [https://visualstudio.microsoft.com/fr/downloads/](https://visualstudio.microsoft.com/fr/downloads/)  ; you will only need the command line tools, so when requested you may choose to install only the last version of the MS build tools for the command line.

Depending on the solver you may want to use, install it following the solver’s own install procedure for windows.

Using the command line of VS (Visual Studio):

- move to a chosen empty directory (YOURDIR)

- git clone [https://github.com/Microsoft/vcpkg.git](https://github.com/Microsoft/vcpkg.git)

Open the VS Developer command prompt:

- move to YOURDIR/vcpkg/

- bootstrap-vcpkg.bat

- ./vcpkg.exe integrate install

From the directory where vcpkg has been installed:

- vcpkg.exe install zlib bzip2 blas lapack eigen3 glpk netcdf-cxx4 pthreads getopt boost --triplet x64-windows (beware, this may last 4 to 5 hours)

If you have a CPLEX licence:

- vcpkg.exe edit coin-or-osi (this will open portfile.cmake in your favourite text editor ; you may also move to ports/coin-or-osi and edit portfile.cmake) , and proceed to the following changes in order to allow for cplex: (go to line 24, adapt to you cplex version and to where it is installed)  
–with-cplex  
–with-cplex-lib=C:\/IBM\/ILOG\/CPLEX_Studio221\/cplex\/lib\/x64_windows_msvc14\/stat_mda\/cplex2210.lib  
–with-cplex-incdir=C:\/IBM\/ILOG\/CPLEX_Studio221\/cplex\/include\/ilcplex  
–with-cplex-cflags=-IC:\/IBM\/ILOG\/CPLEX_Studio221\/cplex\/include\/ilcplex  
–with-cplex-lflags=C:\/IBM\/ILOG\/CPLEX_Studio221\/cplex\/lib\/x64_windows_msvc14\/stat_mda\/cplex2210.lib

/!\ : it may be needed to not have any white spaces in the paths for this to work properly; Also the \/ for windows path specification are not optional !

- vcpkg.exe install coin-or-osi --triplet x64-windows (this may last 30 min)

Check if your vcpkg/installed/x64-windows/lib directory has OsiCpx.lib

- vcpkg.exe install coin-or-clp coinutils pybind11 --triplet x64-windows (this may last 1 or 2 hours)

- vcpkg.exe install boost-mpi --triplet x64-windows

In case of failure execute vcpkg\downloads\msmpisetup-10.1.12498.exe (or in fact the executable vcpkg tells you to install)Then try again : vcpkg.exe install boost-mpi --triplet x64-windows

- git clone [https://gitlab.com/stochastic-control/vcpkg-registry](https://gitlab.com/stochastic-control/vcpkg-registry)

- vcpkg.exe install stopt --overlay-ports=C:\LocalDriveD\Tools\ExtLibsVS\vcpkg\vcpkg-registry\ports\stopt --triplet x64-windows

Create a directory called SMSpp, and move into this directory

- git clone --recurse-submodules [https://gitlab.com/smspp/smspp-project](https://gitlab.com/smspp/smspp-project) -b develop

Go to the SMSpp directory, make a buildVS directory

Edit the extlib/makefile-default-paths-windows  to set all paths properly. The path to set up in the file « extlib/makefile-default-paths-windows » corresponds to the parent folder where the .dll are stored in the vcpkg manager. For example it could be:

BOOST_ROOT = YOURPATH/vcpkg/installed/x64-windows  
Eigen3_ROOT = YOURPATH/vcpkg/installed/x64-windows  
netCDF_ROOT = YOURPATH/vcpkg/installed/x64-windows  
netCDFCxx_ROOT = YOURPATH/vcpkg/installed/x64-windows  
StOpt_ROOT = YOURPATH/vcpkg/installed/x64-windows  
CPLEX_ROOT = « C:/IBM/ILOG/CPLEX_Studio1210 »  
SCIP_ROOT = « C:/Program Files/SCIPOptSuite x.y.z »  
GUROBI_ROOT = C:/gurobi1003  
HiGHS_ROOT = C:/HiGHS  
CoinUtils_ROOT = YOURPATH/vcpkg/installed/x64-windows  
Osi_ROOT = YOURPATH/vcpkg/installed/x64-windows  
Clp_ROOT = YOURPATH/vcpkg/installed/x64-windows

Go in the buildVS directory:

- cmake …/. -DCMAKE_BUILD_TYPE=Debug -DCMAKE_TOOLCHAIN_FILE=C:/LocalDriveD/Tools/ExtLibsVS/vcpkg/scripts/buildsystems/vcpkg.cmake -Wno-dev -DMILPSolver_USE_GUROBI=OFF

- msbuild "The SMS++ Project.sln"

git clone [https://github.com/plan4res/plan4res-scripts](https://github.com/plan4res/plan4res-scripts)

git clone [https://github.com/plan4res/toyDataset](https://github.com/plan4res/toyDataset)

It is possible to get the plan4res running scripts with git clone [https://github.com/plan4res/include](https://github.com/plan4res/include) but some adaptations will need to be made in order to make those scripts functional without the p4r-env environment. This has not been done yet.

Git bash should allow launching the scripts.