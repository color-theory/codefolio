# 01 - Introduction

## Correctness vs. Efficiency
This is the real world we're talking about. While we engineers tend to strive for the most precise answers possible, sometimes it is only required that we find an acceptable one. Fuzzy inputs, resource constraints, and timelines can affect the amount of precision we'll be able to provide in many aspects of our jobs, and algorithms are no different.

Added `Size` and `Complexity` often leads to more required `Resources`.

## Math is Unavoidable. Adapt the strategy to the problem.
There are strategies that can be utilized to decrease the cost of workign with algorithms. Mathmeticians use tricks to get more output from less computing. IE: If it's been proven that x always equals y + some constant z, but you have an algorithm that finds x by doing a series of complex calculations solely on y, you can save yourself a lot of time and effort by using the constant z. Furthermore, if you have a single large algo defined to solve a problem, it can sometimes be more efficient to run a bevy of smaller, simpler algos in parallel that combined lead to the answer you want.

- Bayes' theorem reads the same in any language. https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem
```
P(B|E) = P(E|B)*P(B)/P(E)
```

## Structuring Data to Obtain a Solution
Because computers have a strict understanding about the data we provide, it makes sense that by arranging the data in different ways can affect the way the computer can work with it. For a simple example, converting all text to lowercase prevents the computer from having to compare a single character to two different values in order to determine if it is the letter A(or a)

# 02 - Algorithm Design
We stand on the sho(u)lders of giants. When starting to solve a problem, it's important to recognize the following:
- How other people hav created new problem solutions.
- Know what resources you have available.
- Determine which solutions have worked for similar problems in the past.
- Consider which solutions have not produced a desirable result.

A real world problem sometimes involve:
- Noise
- Unintuitive results
- Extremely large data sets
- Multiple problems

## Greediness
Greed isn't necessarily a bad thing when it comes to algorithms. It means that the most optimal decision is made each step of the way. While this is useful a lot of the time, it's also important to realize that greed isn't always the most effective way to solve a problem. 

#### Example: Change Machine
One example of where greed isn't always best would be a change machine that tries to always use the largest coins available to provide the least coins possible. If the change is 50 cents, a 50-cent piece would be the optimal solution. But what if there are no half-dollars available? Then two quarters would suffice. This is greed working. What if the change required is 40 cents? Well then, you'd get a quarter, then a dime, and then a nickel. But what if there were no nickels? Then you'd get a quarter, then a dime, and then five pennies. By using greed for each step, it made sense to start with the quarter, but in the end, with no nickels, it makes more sense to use four dimes.

## Heuristics
Relies on self-discovery and providing good-enough results. Can be considered as an algorithm making an educated guess and then trying again if it fails.

## Brute Force
Slow, but reliable. Should only be used with small data-sets. Some common brute force searching algorithms:
- Breadth-first
- Depth-first
- Bi-directional

## Problem Spaces
A _problem space_ is an environment in which a search for a solution takes place.
Consider the sliding tile puzzle, in a 3x3 grid. The _problem instance_ is the particular start state, the tiles themselves, and the goal state.  The minimum number of moves to solve the problem is the _problem depth_. Some more important terms:
- _problem space graph_: A graph in which each node represents a single state (all eight tiles in some order).
- _space complexity_: The number of nodes in memory necessary to solve the problem.
- _time complexity_: The amount of time required to solve the problem.
- _branching factor_: The average number of nodes needing to be created at each step in the problem space graph to solve a problem.
It's important to define the problem space you are working with to gain insight into what approaches can be eliminated from the start and possibly which ones might work better. For example, if you know your problem involves a very large data-set, you can pretty much assume that brute-force approaches will not be efficient enough for your needs.

## Evaluating Algorithms
It is important not to simply try algorithms until you find one that works. We must learn to evaluate algorithms abstractly, as trying many algorithms could be a futile waste of time. 

#### RAM Computers
Random Access Machines are not real physical computers. They are theoretical in nature, but help to conceive of the individual steps that would be performed in an algorithm. When testing an algo in a RAM, 
- Count each simple operation as a time step.
- Break complex operations into simple operations and count time steps as above.
- Count every data access from memory as a time step.

This can be done in pseudocode and will help to analyse the time complexity of an algorithm. This mental simulation is different from a _benchmark_ which is testing the algorithm on a specific real-life machine in a real environment. Benchmarks are useful when you know what resources you have available, but lack generality. (something that benchmarks slow on a computer without a math-coprocessor could be very speedy on another that has one.)

#### Resource concerns:
When analyzing algorithms, it is important to consider:
- Running time
- Memory requirements
- Hard-disk usage
- Power-consumption
- Data-transmition speed of the network.

#### Big-O notation
You know Big-O. Big-O represents the theoretical standard worst case in complexity of which we compare our actual algorithm performance. 
- Constant O(1): Does not change as input grows
- Logarithmic O(log n): Grows at a slower rate than the input
- Linear O(n): Grows at same rate as input
- Linearithmic O(n log n): Grows slightly fast than input
- Quadratic O(n^2): Grows as the square of the number of inputs
- Cubic O(n^3): Grows as the cube.
- Exponential O(2^n): Grows twice the number of operations for every input added.
- Factorial O(n!): Let's just say it's big.



