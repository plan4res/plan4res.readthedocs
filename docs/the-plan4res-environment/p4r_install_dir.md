### P4R_INSTALL_DIR

This directory is structured as follows:

-   Documentation: contains the plan4res documentation, downloaded from
    [plan4res/documentation: plan4res
    documentation](https://github.com/plan4res/documentation)

-   p4r-env : contains the plan4res environment (container) as well as
    all the modules of plan4res.

    -   .cache_dir: plan4res container image (.SIF). In some cases it is
        necessary for the user to move the SIF files in another location
        as some systems specify mandatory locations for SIF images. In
        that case, it is necessary to update the p4r-env environment
        variable SINGULARITY_BIND with the location of the SIF file.

    -   bin: contains the main p4r-env executables (bin to run the
        container and the executables used to update or rebuild the
        container)

    -   config: contains the configuration file of p4r-env

    -   executors: contains the definitions files of the container

    -   scripts: contains all the plan4res modules

        -   include: contains all plan4res bash scripts which are used
            to run the different modules

        -   python:

            -   plan4res-scripts: contains the python scripts for the
                CREATE, FORMAT and POSTTREAT modules

            -   openentrance: contains the definition of the IAMC
                nomenclature such as developed in the open ENTRANCE[^10]
                project ( [openENTRANCE/openentrance: Definitions of
                common terms (variables, regions, etc.) for the
                openENTRANCE
                project](https://github.com/openENTRANCE/openentrance) )

        -   add-ons: contains the solving modules of plan4res: SSV, SIM
            and CEM, which are based on the SMS++[^11] library.

            -   Install: installation dir for sms++ and the solvers used
                within sms++

            -   .build: directory where the source code is downloaded
                and compiled

-   data: optional directory. Created only when the user wishes to run
    plan4res in the same location where it is installed. The structure
    of data is described in section 3.2.2.

