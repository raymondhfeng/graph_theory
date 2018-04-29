import networkx as nx 
from matplotlib import pyplot as mpl 
# G = nx.circular_ladder_graph(10)
# G = nx.barbell_graph(10)

# G = nx.dorogovtsev_goltsev_mendes_graph(5)
# print("hoopla!")
# print(G)
# print(list(G.edges()))
# nx.draw(G)
# mpl.savefig("simple_path.png") # save as png
# mpl.show() # display

G = nx.lollipop_graph(10,10)
pos = nx.spring_layout(G)
print(G.nodes())
nx.draw(G, pos)
mpl.show()