# Rubik's Cube Solver

## Abstract:
In this study, two methods were used to solve scrambled rubik's cube. It was done using Iterative Depth First Search (IDFS) or Iterative Deepening Search (IDS) and Iterative Deepening A* (IDA*). Two heuristics were used for IDA*. One of them uses pattern database. All methods were able to unscramble cube. However, time to unscramble cube increased exponentially with steps to solve the cube. IDA* with pattern database unscrambled cube the quickest.

## Algorithms:
Two search algorithms were used to solve Rubik's cube.
* Iterative Depth First Search (IDFS) or Iterative Deepening Search (IDS).
* Iterative Deepening A* (IDA*)

## Heuristics:
Two heuristics were used for IDA*.
* First is **corner_idge_sum_max**. It takes the maximum of the sum of manhattan distance of cube corners and sum of manhattan distance of edges.
* Second is **corner_pattern_database**. It uses depth of corners configuration of cube as heuristic. Depth is assumed to be saved in **Pattern Database**

## Creating Pattern Database:
In this problem, pattern database only uses depth of specific corners configuration. It can extend for depth of edges configuration. In that case, maximum of both will be used.
Depth of corners configuration can be calculated by performing every possible move on every possible cube state. Root configuration will be configuration of solved cube with depth is equal to zero. Depth of further configurations will be equal to the configuration of the configuration it was derived from plus 1.

## Results:
Both algorithms were able to solve the cube. IDFS time increased rapidly with depth of solution. IDA* performd quite faster as compared to IDFS. IDA* worked even faster with pattern database. Detailed results can found in [Report](../master/Report-Format-1.docx).

## Conclusion:
To conclude, both IDFS and IDA* can be used to unscramble 


## Contact
You can get in touch with me on my LinkedIn Profile: [Farhan Shoukat](https://www.linkedin.com/in/farhan-shoukat/)


## License
[MIT](../master/LICENSE)
Copyright (c) 2018 Farhan Shoukat

