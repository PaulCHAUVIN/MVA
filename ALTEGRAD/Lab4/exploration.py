"""
Graph Mining - ALTEGRAD - Nov 2022
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

############## Task 1

G = nx.read_edgelist(path='/Users/paulchauvin/PycharmProjects/ALTEGRAD_Lab4/ca-HepTh.txt',
                     comments='#',
                     delimiter='\t',
                     data=True)
print(G)

############## Task 2

def connected_components(G):
    cc_list = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    largest_cc = max(nx.connected_components(G), key=len)
    G_largest_cc = G.subgraph(largest_cc)
    nb_edges_largest_cc = G_largest_cc.number_of_edges()
    nb_nodes_largest_cc = G_largest_cc.number_of_nodes()
    nb_edges_total = G.number_of_edges()
    nb_nodes_total = G.number_of_nodes()
    return "There are " + str(len(cc_list)) + " connected components in the graph. The largest connected components has "+ str(nb_nodes_largest_cc) + " nodes ("+str(int(100*(nb_nodes_largest_cc/G.number_of_nodes())))+"% of total) and " + str(nb_edges_largest_cc) + " edges ("+str(int(100*(nb_edges_largest_cc/G.number_of_edges()))) +"% of total)."

connected_components(G)

############## Task 3
# Degree
degree_sequence = [G.degree(node) for node in G.nodes()]
print("The maximum degree of the nodes in the graph is ", "%.2f" %max([elem for elem in degree_sequence]))
print("The minimum degree of the nodes in the graph is ", "%.2f" %min([elem for elem in degree_sequence]))
print("The mean degree of the nodes in the graph is ", "%.2f" %np.mean([elem for elem in degree_sequence]))


############## Task 4
plt.close()

fig,(ax0, ax1) = plt.subplots(nrows=1, ncols=2)

ax0.hist(nx.degree_histogram(G), density=True, histtype='bar')
ax0.set_title('Degree histogram')

ax1.hist(nx.degree_histogram(G), density=True, histtype='bar')
ax1.set_title('Degree histogram in log axis')
ax1.set_xscale('log')
ax1.set_yscale('log')

fig.tight_layout()
plt.show()


############## Task 5
print('The global clustering coefficient is ',"%.2f" %nx.transitivity(G))

