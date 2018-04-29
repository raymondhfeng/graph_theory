#!/usr/bin/env python
import random
import pylab
from matplotlib.pyplot import pause
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np 
pylab.ion()

graph = nx.Graph()
graph = nx.lollipop_graph(10,10)
pos = nx.spring_layout(graph)
node_number = 0
# graph.add_node(node_number, Position=(random.randrange(0, 100), random.randrange(0, 100)))

def get_fig():
    # global node_number
    # node_number += 1
    # graph.add_node(node_number, Position=(random.randrange(0, 100), random.randrange(0, 100)))
    # graph.add_edge(node_number, random.choice(graph.nodes()))
    # nx.draw(graph, pos=nx.get_node_attributes(graph,'Position'))
    pylab.clf()
    nx.draw(graph, pos, node_color=color, cmap=plt.cm.Blues)

num_plots = 50;
pylab.show()
curr = len(graph.nodes()) - 1
visited = {}
visited[0] = 100
for i in range(len(graph.nodes())):
	if i == curr:
		visited[i] = 1
	else:
		visited[i] = 0

for i in range(1000):
	neighbors = graph.neighbors(curr)
	nextNode = np.random.choice(neighbors)
	# visited[curr] = 0
	curr = nextNode
	visited[nextNode] += 1
	color = [visited[key] for key in sorted(visited.keys(), reverse=False)]
	get_fig()
	pylab.draw()
	pause(0.08)	