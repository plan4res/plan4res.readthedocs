### Results of SSV 

The SSV runs a Stochastic Dynamic Dual Programming (SDDP) algorithm to
compute Bellman values for all the seasonal storages.

**Note**: Bellman values represent the *cost-to-go functions* = the
expected economic value associated to the various levels of the seasonal
storages at each time stages. They are usually represented as sets of
hyperplanes called *cuts*.

The results are:

-   [When the convergence criteria of the SDDP algorithm is
    met]{.underline}[^34]: \*

    -   BellmanValuesOUT.csv: redundant cuts have been pruned out.

    -   BellmanValuesAllOUT.csv: contains all the cuts found by the
        algorithm.

-   [In any case, ie even without convergence]{.underline}: cuts.txt,
    which contains all the cuts already found by the SDDP algorithm.
    This is useful to help reach convergence since it is possible to
    launch the SSV again using the cuts from a previous run stored in
    cuts.txt as a hot start.

The format of this file is, as shown in Table 13, aiming to represent a
polyhedral function at each SSV timestep. The first column (Timestep)
gives the index of the SSV Timestep. There are a number of rows for each
timestep, representing the different 'cuts' of the function at this
timestep. The function at timestep \$i is:
$\max_{cuts}\left( \sum_{j = 0}^{R}{a\_ j} + b \right)$, where a_j and b
are the values in the corresponding columns, and R is the number of
reservoirs (the number of columns a_j).

Table 13: BellmanValuesOUT.csv

  -------------------------------------------------------------------------
  **Timestep**   **a_0**         **a_1**      **a_2**        **b**
  -------------- --------------- ------------ -------------- --------------
  0              0               0            0              3.9825E+10

  0              -113.40944      -10000       -10000         7.4137E+10

  0              -113.40944      -10000       -81.517916     1.2033E+11

  0              -81.786066      -3           -150.94929     5.6955E+10

  0              -0.036          -3.816       -8             5.3972E+10

  0              -8              -3           -113.20533     5.5282E+10

  0              -0.03249        -0.03249     -8             5.4175E+10

  0              -0.036          -10000       -81.517916     1.1965E+11

  0              -0.036          -8           -81.517916     5.5241E+10

  1              0               0            0              3.9637E+10

  1              -113.40944      -10000       -10000         1.3613E+11
  -------------------------------------------------------------------------

