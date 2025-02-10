import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

file_path = "networks_assignment.to_csv"
df = pd.read_csv(file_path, index_col=0)

pentagram_nodes = ['D', 'F', 'I', 'N', 'S']
green_nodes = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA']
yellow_nodes = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'ASU']
all_nodes = pentagram_nodes + green_nodes + yellow_nodes

G = nx.DiGraph()

for source in df.index:
    for target in df.columns:
        if df.loc[source, target] > 0:
            G.add_edge(source, target, weight=df.loc[source, target])

pos = {}

pentagram_angles = np.linspace(0, 2 * np.pi, 6)[:-1]
pentagram_radius = 1.5
for i, node in enumerate(pentagram_nodes):
    pos[node] = (pentagram_radius * np.cos(pentagram_angles[i]), pentagram_radius * np.sin(pentagram_angles[i]))

np.random.seed(42)
outer_radius = 3
angle_step = 2 * np.pi / (len(green_nodes) + len(yellow_nodes))

angle = 0
for node in green_nodes + yellow_nodes:
    distance = np.random.uniform(outer_radius, outer_radius + 1)
    pos[node] = (distance * np.cos(angle), distance * np.sin(angle))
    angle += angle_step

node_colors = {}
for node in pentagram_nodes:
    node_colors[node] = 'blue'
for node in green_nodes:
    node_colors[node] = 'green'
for node in yellow_nodes:
    node_colors[node] = 'yellow'

node_color_values = [node_colors[node] for node in G.nodes()]

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=800, font_size=8, node_color=node_color_values, edge_color="gray", linewidths=0.5, font_weight="bold")

plt.title("Network Graph")
plt.show()
