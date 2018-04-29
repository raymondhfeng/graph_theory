import numpy as np
import matplotlib.colors as mcolors
import networkx as nx
import matplotlib.pyplot as plt
n = 10000  # Number of nodes
m = 3  # Number of initial links
seed = 500
G = nx.barabasi_albert_graph(n, m, seed)

ncols = 100
pos = {i : (i % ncols, (n-i-1)//ncols) for i in G.nodes()}

fig, ax = plt.subplots()
degrees = G.degree() #Dict with Node ID, Degree
nodes = G.nodes()
n_color = np.asarray([degrees[n] for n in nodes])
sc = nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=n_color, cmap='viridis',
                            with_labels=False, ax=ax, node_size=n_color)
# use a log-norm, do not see how to pass this through nx API
# just set it after-the-fact
sc.set_norm(mcolors.LogNorm())
fig.colorbar(sc)
fig.show()
plt.pause(10)