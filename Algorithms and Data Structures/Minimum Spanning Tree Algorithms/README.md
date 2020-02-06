# Minimum Spanning Tree Algorithms

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

