# Minimum Cost Spanning Tree Algorithms (MCST)

The Python script uses the same kind of Partition ADT (union-find data	structure) and the minimum
spanning tree algorithms.

## Context

Electricity grids can be designed using a 'minimum cost spanning tree' algorithm,	by taking into
account the minimal cost of installing transmission links and structures, rather than simply using	the
shortest distance from	a	node to the power station. To achieve this,	one can start by assigning each
node in the network its own partition and calculate the distances between all pairs of nodes.	Nodes
with the lowest cost edges can	be connected first in	the	grid,	forming spanning trees.	These trees can	
then	be	successively merged in a forest (partial spanning trees) until we obtain a full single spanning
tree.	In other words,	we are successively joining clusters of connected	data points or nodes until there
is only a single big cluster.

Sometimes, the electricity	providers prefer	splitting	the	electricity	network	into	fragments or	microgrids	(also	known	as	‘Islands’).	This	helps	improve	the	self-healing,	reliability,	and	resiliency	of	the	
electrical	system	of	remote	towns	or	communities. It	also	reduces	overloading	of	the	micro-grid	and
helps	save the	cost of installing	and	maintaining lengthy	and	expensive	high	voltage	transmission	links	
over	fragmented	communities.	

A particularly	simple	approach to	achieve	the	above	form	of	spanning	tree	using clustering	is by using
the Kruskal’s algorithm we	have	studied earlier	in	the	course.	In	Kruskal’s	algorithm,	we	successively	
merge	trees	in	a	forest	(partial	spanning	trees)	until	we	obtain	a	full	single	spanning	tree.	This	type	of	
clustering	is	referred	to	as	single-link	clustering	and	is	a	specific	type	of	hierarchical	clustering. 

In	 this	 task, we	 start	 by	 assigning	 each	 data	 point (representing	 location	 of	 customers) its	 own	
partition and	successively	join	clusters	of	data	points or	customer	nodes until	we	end	up	with	a	single	
big	cluster.	To	do	so	we	can	use	the	Partition	ADT	(union-find	data	structure).

## Steps:
1. Using the ADT class for points in 2-dimensional Euclidean space from before,	implement a
function to generate a test set of n random nodes/points,	 where n is a user-definable
parameter.	

2. Implement an ADT class for Partition (union-find).	 It supports the operations for
generating a new partition (i.e.	a set of sets),	for generating a new set within the partition,	for
merging two sets (union)	and for finding a set to which an element belongs (find).	This step
uses the tree-based implementation.

3. Using the Partition ADT and test data function that wrote for the first two tasks,	
implement the clustering procedure described above.	

4. Extend forest-based Partition ADT class from above with path compression.	

5. Ultimately,	we are aiming to find k-clusters i.e.	we want to the	electricity	providers	to	see	
the	structure	of	the	micro-grid	if	they	decide	to	commission k micro-grids such	that	all	the	
nodes	are	covered	in	the	vicinity	of	these	sub-stations. I Extend my implementation that
it stops when k clusters have been achieved and return those clusters,	where k is a userdefinable parameter.

6. Implement functions/methods to let the user query whether two given points (nodes) belong
to the same cluster (micro-grid).

7. Define a function to compute the Dunn index,	a measure for the quality of the clustering.

8. Compare the forest that have generated for the k-clustering to the full minimum cost
spanning tree. 

9. Use Matplotlib and Bokeh to visualize how
the algorithm works and let the user interactively (graphically)	enter a point set.
