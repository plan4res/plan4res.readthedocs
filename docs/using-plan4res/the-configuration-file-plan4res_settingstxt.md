### The configuration file plan4res_settings.txt

This configuration file contains parameters for the plan4res modules SSV
and CEM. Some of those parameters can be passed as options of the p4r
command (in this case the value passed in option will always be used).

This file contains the following parameters:

-   **SSV parameters**

```{=html}
<!-- -->
```
-   **NumberSSVIterationsFirstStep**: maximum number of iterations of
    the first step, when using option -S

-   **NumberSSVIterations**: maximum number of iterations when not using
    option -S, or maximum number of iterations in the final step when
    using option -S

-   **CheckConvEachXIterInFirstStep**: convergence is checked after X
    iterations of the sddp algorithm in the first step, when ran with
    option -S

-   **CheckConvEachXIter**: convergence is checked after X iterations of
    the sddp algorithm in the unique SSV step when ran without option
    -S, and in final SSV step when ran with option -S

-   **EpsilonSSV**: convergence criteria of SSV

```{=html}
<!-- -->
```
-   **CEM parameters**

```{=html}
<!-- -->
```
-   **NumberOfCemIterationsInLoopCEM**: maximum number of iterations in
    each run of CEM when CEM is launched with option -L

-   **NumberOfCemIterations**: maximum number of iterations in each run
    of CEM when CEM is launched without option -L or in the last CEM run
    when launched with -L

-   **MaxNumberOfLoops**: maximum number of iterations SSV/CEM when CEM
    is launched with option -L

-   **EpsilonCEM**: convergence criteria for CEM when launched with
    option -L

-   **Distance**: choice of the distance computation for CEM when
    launched with option -L. distance can be 2 or 3 -default 2- 2 means
    that the distance between the initial capacity and the invested
    capacity is used for checking convergence; 3 means that the distance
    between the cost of the investment solution at the last 2 iterations
    is used for checking convergence

-   **ScenariosLists**: name of the configuration file for running CEM
    with option -U

