import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sankey_assignment.csv")

sources = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
intermediates = df['LABEL'].unique().tolist()
targets = ['Reg', 'Aca', 'Oth']

nodes = sources + intermediates + targets
node_indices = {name: i for i, name in enumerate(nodes)}

node_colors = {
    "PS": "#008080", "OMP": "#FF8C00", "CNP": "#FF4500", "NRP": "#8A2BE2",
    "NMCCC": "#FFD700", "PEC": "#DC143C", "NCDM": "#32CD32", "RGS": "#1E90FF",
    "Reg": "#87CEEB", "Aca": "#4682B4", "Oth": "#20B2AA"
}

for i, intermediate in enumerate(intermediates):
    node_colors[intermediate] = ["#4682B4", "#A9A9A9", "#2F4F4F", "#5F9EA0", "#708090"][i % 5]

links = []
colors_links = []
for _, row in df.iterrows():
    intermediate = row['LABEL']
    for source in sources:
        value = row[source]
        if value > 0:
            links.append((source, intermediate, value))
            colors_links.append(node_colors[source])
    for target in targets:
        value = row[target]
        if value > 0:
            links.append((intermediate, target, value))
            colors_links.append(node_colors[intermediate])

source_indices = [node_indices[link[0]] for link in links]
target_indices = [node_indices[link[1]] for link in links]
values = [link[2] for link in links]

sankey_figure = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes,
        color=[node_colors[node] for node in nodes]
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=values,
        color=colors_links
    )
))

sankey_figure.update_layout(
    title_text="Sankey Diagram - Adjusted Layout & Colors",
    font_size=10
)

sankey_figure.show()
