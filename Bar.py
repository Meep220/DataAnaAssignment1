import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "./bar_assignment.csv"
df = pd.read_csv(file_path)

# Transform 1 -> "Yes" and 0 -> "No"
df["COUNT"] = df["COUNT"].map({1: "Yes", 0: "No"})

# Count occurrences of "Yes" and "No" for each category
pivot_df = df.groupby(["LABEL", "COUNT"]).size().unstack(fill_value=0)

# Define colors based on the provided example
colors = {"No": "red", "Yes": "blue"}

# Plot horizontal stacked bar chart with annotations
fig, ax = plt.subplots(figsize=(8, 5))
bars = pivot_df.plot(kind="barh", stacked=True, color=[colors["No"], colors["Yes"]], ax=ax)

# Add labels inside bars
for container, response_type in zip(bars.containers, pivot_df.columns):
    for rect in container:
        width = rect.get_width()
        if width > 0:  # Avoid placing labels on zero values
            x_pos = rect.get_x() + width / 2  # Center position
            ax.text(x_pos, rect.get_y() + rect.get_height() / 2, str(int(width)), 
                    ha='center', va='center', fontsize=12, color='white', fontweight='bold')

# Customizing the plot to match the reference image
plt.xlabel("LABELS", fontsize=12, fontweight="bold")
plt.ylabel("COUNT", fontsize=12, fontweight="bold")
plt.title("Horizontal Stacked Bar Chart", fontsize=14, fontweight="bold")

# Adjust legend to match placement and format
legend = plt.legend(title="LEGEND HERE", loc="upper left", fontsize=12, title_fontsize=12)
for text in legend.get_texts():
    text.set_fontweight("bold")

# Show the improved plot
plt.show()
