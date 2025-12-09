## Installation of the full plan4res environment on Windows

Requirements: at least 3G available.

### Installing on Windows using WSL

Follow the procedure ‘Installing on Linux’

### Installing on Windows, using Vagrant

The procedure is available at
[**https://gitlab.com/cerl/plan4res/p4r-env#windows**](https://gitlab.com/cerl/plan4res/p4r-env#windows).
It is reproduced below with some more information.

Installation requires Windows 7 Pro 64bit SP1 or higher and
[PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-windows-powershell?view=powershell-6)
3.0 or higher. Furthermore, the CPU must support [hardware
virtualization](https://www.virtualbox.org/manual/ch10.html#hwvirt). On
many systems, the hardware virtualization features first need to be
enabled in the BIOS.

#### Required packages Installation (execute once)

-   Install Git for Windows (use default settings)
    <https://git-for-windows.github.io/>

-   Install VirtualBox and [Extension Pack]{.underline}
    <https://www.virtualbox.org/wiki/Downloads>

-   Install Vagrant <https://www.vagrantup.com/downloads.html>

-   (Optional) Install Vagrant Manager
    <http://vagrantmanager.com/downloads/>

The goal of Vagrant and VirtualBox is to emulate a UNIX system on the
Windows computer. Vagrant Manager provides a GUI to facilitate the
management of the VM.

#### Installation

Run Git Bash.

If working behind a proxy, define the following environment variables:

export http_proxy = \<proxy address\>:\<port\>

export https_proxy = \${http_proxy}

Move to your installation directory:

cd P4R_DIR

Then enter the following commands:

> git clone <https://github.com/plan4res/install>
>
> mv ./install/\* .
>
> chmod a+x \*.sh
>
> ./plan4res_install.sh \[-S \<SOLVER\>\] \[-I \<installer\>\] \[-L
> \<license\>\] \[-v \<version\>\] -M MPICH -V \<memory\>
>
> Where:

-   SOLVER is the chosen solver among CPLEX, GUROBI, SCIP, HiGHS. If
    this option is not provided, HiGHS is chosen

-   Installer is the installer file for CPLEX of Gurobi, the -I option
    must only be provided when CPLEX or GUROBI are chosen

-   License is the license file, only for GUROBI

-   Version is the solver version, only for SCIP

**Examples:**

./plan4res_install.sh -M MPICH -V 8192

-   Installs plan4res with HiGHS

./plan4res_install.sh -M MPICH -V 8192 -S CPLEX -I
cplex_studio2211.linux_x86_64.bin

-   Installs plan4res with CPLEX, using ths installer
    cplex_studio2211.linux_x86_64.bin available in P4R_DIR

./plan4res_install.sh -M MPICH -V 8192 -S GUROBI -I
gurobi11.0.1_linux64.tar.gz -L gurobi.lic

-   Installs plan4res with GUROBI using the gurobi installer and licence
    available in P4R_DIR

./plan4res_install.sh -M MPICH -V 8192 -S SCIP -v 9.1.1

-   Installs plan4res with SCIP, choses the version 9.1.1 from SCIP

#### Vagrant settings

To avoid issues with memory fragmentation while using Vagrant, we advise
to allocate at least 8 Gb of RAM if the computer can afford it. This can
be done via the -V option of the installation command (see above), but
you can also edit the file *Vagrantfile* located in *P4R_DIR/p4r-env*,
edit parameter vb.memory (in Mb):

![](media/media/image1.png){width="4.141515748031496in"
height="1.1358005249343832in"}

You may also increase the number of CPUs allocated to the VM if
possible, on your machine. In above example, it is set to 6.


