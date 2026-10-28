"""Figure 1: firms on the Disclosure (x) and Disclaimer (y) axes; marker size = Absolution; colour = cluster.
All firms in the dataset (one pooled roster), filled by cluster. Light jitter.
Run from the project root after analysis/taxonomy_v2.py: python analysis/figure1_taxonomy.py"""
import csv, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

rows = list(csv.DictReader(open("analysis/taxonomy-v2-firms.csv", encoding="utf-8")))
COL = {"Fortified": "#1b6ca8", "Agentic-shift": "#7b3fa0", "Warned": "#2a9d6f", "Peripheral": "#e09f2d", "Exposed": "#c4483e"}
random.seed(7)
j = lambda: random.uniform(-0.22, 0.22)
fig, ax = plt.subplots(figsize=(6.4, 4.6), dpi=300)
for r in rows:
    x, y, s = int(r["disclosure"]) + j(), int(r["disclaimer"]) + j(), 18 + 28 * int(r["absolution"])
    ax.scatter(x, y, s=s, color=COL[r["cluster"]], alpha=0.85, edgecolors="white", linewidths=0.5, zorder=3)
ax.set_xticks(range(4)); ax.set_yticks(range(4))
ax.set_xticklabels(["0\nnone", "1\noutside\ncontract", "2\ncategory /\nAI-specific", "3\nby brand"], fontsize=7)
ax.set_yticklabels(["0 none", "1 generic only", "2 one AI-specific", "3 two or more\nAI-specific"], fontsize=7)
ax.set_xlabel("Disclosure: does the firm tell the customer an AI is involved?", fontsize=8)
ax.set_ylabel("Disclaimer: AI-specific accuracy, reliance,\nliability clauses in the binding contract", fontsize=8)
ax.set_xlim(-0.5, 3.5); ax.set_ylim(-0.5, 3.5)
ax.grid(True, color="#e6e6e6", linewidth=0.6, zorder=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c, markersize=7, label=k) for k, c in COL.items()]
handles += [Line2D([0], [0], marker="o", color="w", markerfacecolor="#bbbbbb", markersize=ms, label=f"Absolution {lv}")
            for lv, ms in ((0, 4), (3, 10))]
ax.legend(handles=handles, fontsize=6.5, frameon=False, loc="upper left", bbox_to_anchor=(1.0, 1.0))
fig.tight_layout()
fig.savefig("analysis/figure1-taxonomy.png", bbox_inches="tight")
print(f"plotted {len(rows)} firms")
print("saved analysis/figure1-taxonomy.png")
