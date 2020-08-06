import networkx as nx

G = nx.Graph()

#Nodos = ["Julio", "Natalia"]
G.add_nodes_from(["folates", "asparagus", "liver"]) # Add a list of nodes
G.add_edges_from([("folates", "liver"), ("folates", "asparagus")])

print(G.nodes)


