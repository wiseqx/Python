# Divide and Conquer
Divide and Conquer algorithm can be used to find the closest pair of points in a set of points
in 2-dimensional Euclidean space. 

We now want to solve the same problem using *Manhattan Distance* (this is simply the distance that  
walk on a grid where you can’t take diagonal shortcuts as opposed to the Euclidean
distance which measures the shortest straight line.). This task is to adapt and implement the Divide
and Conquer algorithm and to evaluate it empirically. We

1. Use the ADT class for points in 2-dimensional Euclidean space discussed in the lecture in Week 1
(see lecture notes), and extend the class this with a distance function for pairwise Manhattan
distance.

2. Based on this point class, implement an ADT class that models a point set. It will need a
constructor as well as functions to insert and delete points in the set.

3. Extend the point set class with a method to find the closest pair of points. Our method
returns the coordinates of the two points that have the smallest pairwise distance in the set as well
as this distance. And there is a brief discussion and justify in the algorithm that to accomodate Manhattan distance. 
Implement two different versions as methods in the point set class:
  * a. Implement the naive O(n2) brute-force algorithm.
  * b. Implement the divide-and-conquer algorithm.


4. Perform an empirical runtime evaluation for both algorithms using the Python timeit library.
Plot runtime graphs for both algorithms for a reasonable rage of input sizes. 

5. Define the runtime recurrence relation that would arise and sort the lists explicitly on each level of the recursion.

6. Use packages to visualize
how the algorithm searches (i.e. visualize the point sets, the splitlines, and ultimately the results)
and even to let the user interactively (graphically) enter a point set (the latter is easier in
Matplotlib than in Bokeh). 
