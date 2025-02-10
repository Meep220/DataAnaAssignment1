import pandas as pd
import matplotlib.pyplot as plt

file_path = "./bar_assignment.csv"
df = pd.read_csv(file_path)

df["COUNT"] = df["COUNT"].map({1: "Yes", 0: "No"})

pivot_df = df.groupby(["LABEL", "COUNT"]).size().unstack(fill_value=0)

colors = {"No": "red", "Yes": "blue"}

fig, ax = plt.subplots(figsize=(8, 5))
bars = pivot_df.plot(kind="barh", stacked=True, color=[colors["No"], colors["Yes"]], ax=ax)

for container, response_type in zip(bars.containers, pivot_df.columns):
    for rect in container:
        width = rect.get_width()
        if width > 0:
            x_pos = rect.get_x() + width / 2
            ax.text(x_pos, rect.get_y() + rect.get_height() / 2, str(int(width)), 
                    ha='center', va='center', fontsize=12, color='white', fontweight='bold')

plt.xlabel("LABELS", fontsize=12, fontweight="bold")
plt.ylabel("COUNT", fontsize=12, fontweight="bold")
plt.title("Horizontal Stacked Bar Chart", fontsize=14, fontweight="bold")

legend = plt.legend(title="LEGEND HERE", loc="upper left", fontsize=12, title_fontsize=12)
for text in legend.get_texts():
    text.set_fontweight("bold")

plt.show()
