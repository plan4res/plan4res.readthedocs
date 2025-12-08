### Filling the settingPostTreatPlan4res_XXX.yml configuration file

The configuration files settingsPostTreatPlan4res_simul.yml (for
posttreating results of SIM) or settingsPostTreatPlan4res_invest.yml
(for posttreating results of CEM) define how the results will be
post-treated by POSTTREAT.

You may edit this file with any text editor. Change the following
parameters:

-   **BeginTreatData**: optional , use only if you want to posttreat on
    a subset of the time horizon

-   **EndTreatData**: optional , use only if you want to posttreat on a
    subset of the time horizon

-   (do not change) **Resultsdir**: sub-repository where all results are
    (in practice results_simul or results_invest)

-   (do not change) **ScenarioIdentifier**: postfix of the output files
    of SIM and CEM as defined in SMS++

-   **map**: yes if you wish to output graphs on maps

-   **geopandas**: if you are not using the p4r-env environment, you may
    not have installed the python package geopandas (which is quite
    tricky to install) in that case choose no

-   **private_map**: CSV file defining the boarders of the map, contains
    gdp data. It must include the countries you are working on.

-   **PostTreat**:

    -   **DrawMean**: True if you wish to include the average in the
        stochastic graphs

    -   The following subsections: **Volume**, **Flows**, **Power**,
        **MarginalCost**, **MarginalCostFlows**, **Demand**,
        **InstalledCapacity** and **SpecifiedPeriods** are used to
        specify which treatment should be done for each category. The
        list of possible treatments is given for each category and you
        must write yes for allowing the treatment, or no.

        -   **read**: read results and creates the posttreated csv files

        -   **draw**: create graphs

        -   **latex**: create latex report

        -   **iamc**: converts results to IAMC format

        -   (do not change) **Dir**: name of sub dir in results_invest
            or results_simul

    -   SpecifiedPeriods allows the user to choose a list of scenarios
        and subperiods which will be analysed in details. It includes
        additional parameters:

        -   **Scenarios**: subset of scenarios on which to perform
            detailed analysis

        -   A subsection for each period to analyse, with a name chosen
            by the user. For each period, you need to fill **begin**
            with the first timestep of the period and **end** with the
            last timestep

```{=html}
<!-- -->
```
-   **Graphs**: this section allows to specify the dimensions of the
    graphics. It include one subsection for each of the following
    categories: **Volume**, **Power**, **MarginalCost**,
    **MarginalCostFlows** and **Demand.** For each category, the
    following parameters are required:

    -   **nbcols**: number of columns in the graph which will be
        composed of subgraphs per regions or interconnections

    -   **nblines**: number of rows in the graph which will be composed
        of subgraphs per regions or interconnections

    -   **SizeCol**: size of the column in the aforementioned graph

    -   **SizeRow**: size of the row in the aforementioned graph

    -   **TitleSize**: size of the title in the aforementioned graph

    -   **LabelSize**: size of the labels (columns and rows) in the
        aforementioned graph

    -   (only for Power) **treat**: list of aggregated technologies to
        be included in the generation graphs

    -   (only for Power) **ChloroGraph**: parameters for the graph
        composed of one map per aggregated technology, with shade
        varying depending on the intensity of this technology in each
        region:

        -   **nbcols**: number of columns

        -   **nblines**: number of rows

        -   **dpi**: the default dpi produces very big jpeg files.
            Lowering it lowers the quality of the graph but also its
            size.

-   **scenario**: name of Scenario to be used in Scenario column of the
    IAMC files containing outputs of plan4res (should be the name of the
    scenario used in CreateInputPlan4res followed by '\|' and an
    additional identifier if necessary)

-   **model**: name of Model to be used in Scenario column of the IAMC
    files containing outputs of plan4res (should be plan4res 2.0)

-   **namereport**: name of the latex file which can be created

-   **titlereport**: title of the latex report

-   **usevu**: if yes, the cost of water used will be computed using the
    Bellman values computed by SSV

-   **timestepvusms**: index of the SSV timestep to use for computation
    of the value of the water at the end of the period analysed by
    POSTTREAT

-   **arrondi**: 1 if you wish to round all figures, else 0

-   **marginalcostlimits**: allows to limit the graphs of marginal costs
    to a certain limit. You must provide a maximum (**max**) and a
    minimum (**min**)

-   **pielimit**: POSTTREAT create graphs with pies. For very small
    quantities, the share of the pie will not be visible. This allows to
    not include shares of less than X in the graphs

-   **Technos**: this section gives a color identifier for each
    technologies. All technologies in settingsCreatePlan4res_XXX.yml
    must be present, but this section can include additional
    technologies. For each techno X that has pumping capacity, an
    additional techno X_PUMP must be added.

-   **technosAggr**: this section allows to define aggregates for the
    technologies (e.g. gas or WindPower). These aggregates are used for
    creating additional graphs as well as synthetic outputs. This
    section must list the different aggregates and provide the following
    for each aggregate:

    -   **technos**: list of the technologies included in this aggregate

    -   **color**: color used in e.g. bargraphs

    -   **colors**: code of a color range to use in the chloromaps

-   **pumping**: provides the list of all technologies with storage and
    pumping capacity

-   **nopumping**: provides the list of all technologies with storage
    but WITHOUT pumping capacity

-   **graphVolumes**: parameters for creation of the graphs related to
    storage for the 'SpecificPeriods'. It includes one subsection per
    category (**Reservoir**, **PumpedStorage**, **Battery**), and for
    each category:

    -   **Name**: title of the graph

    -   **Technos**: list of technos to include

