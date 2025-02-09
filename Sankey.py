import pandas as pd
import plotly.graph_objects as go

# Load the CSV file
df = pd.read_csv("./sankey_assignment.csv")

# Define source and target categories
sources = ['PS', 'OMP', 'CNP', 'NRP', 'NMCCC', 'PEC', 'NCDM', 'RGS']
targets = ['Reg', 'Aca', 'Oth']

# Flatten the data into a source-target-value format
links = []
for source in sources:
    for target in targets:
        value = df[source].sum()  # Sum all values in the column
        if value > 0:
            links.append((source, target, value))

# Map node names to indices
nodes = sources + targets
node_indices = {name: i for i, name in enumerate(nodes)}

# Create Sankey diagram data
sankey_data = dict(
    type='sankey',
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes
    ),
    link=dict(
        source=[node_indices[link[0]] for link in links],
        target=[node_indices[link[1]] for link in links],
        value=[link[2] for link in links]
    )
)

# Create and show figure
fig = go.Figure(go.Sankey(**sankey_data))
fig.update_layout(title_text="Sankey Diagram", font_size=10)
fig.show()
