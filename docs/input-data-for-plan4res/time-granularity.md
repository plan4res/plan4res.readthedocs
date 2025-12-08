### Time granularity

Figure 6 shows how time is discretised in plan4res. There are 2 levels
of discretization:

-   the SSV timesteps, which are usually weeks (could be months or
    days). They represent the horizon for the management of short term
    storages. During the simulations (in SIM but also conducted while
    solving SSV and CEM), a unit commitment problem will be solved for
    each scenario and each SSV timestep.

-   The timesteps, which are usually 1 hour and are the lowest
    granularity in plan4res. All timeseries should be provided at this
    granularity, but if data are not available, plan4res CREATE and
    FORMAT modules will be able to adapt to higher or lower
    granularities.

![](media/media/image5.jpg){width="6.072490157480315in"
height="2.6875in"}

Figure 6: Time representation

