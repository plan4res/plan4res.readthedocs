### The sp4r command

sp4r has the same "usage" as p4r apart from a mandatory additional
argument: **-n or --nodes** followed by the number of nodes on which to
run plan4res.

It will create the file this_sbatch_p4r.sh and run it with sbatch.

Note that the plan4res scripts will manage the configuration of the
arguments requested by sbatch such as the number of tasks, ......
depending on the module which is ran. Within a workflow of different
modules, these parameters are adapted, and each module is launched with
srun.

