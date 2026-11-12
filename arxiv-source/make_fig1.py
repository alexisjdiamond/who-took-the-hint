"""Figure 1 of the long-form paper: the floor and the influence rate against the base rate,
at take-up pi = 0.6 (the half-blind monitor of Section 3.1), equal baselines.

    python make_fig1.py        # writes fig1.png beside this file (needs matplotlib)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

PI = 0.6
p0 = [i / 1000 for i in range(0, 801)]
p1 = [PI + (1 - PI) * x for x in p0]
influence = [PI / y for y in p1]
floor = [PI * (1 - x) / y for x, y in zip(p0, p1)]

fig, ax = plt.subplots(figsize=(6.2, 4.1), dpi=200)
ax.fill_between(p0, floor, influence, color="#d9d9d9", linewidth=0)
ax.plot(p0, influence, color="black", linewidth=2)
ax.plot(p0, floor, color="black", linewidth=2, linestyle=(0, (4, 2)))
for x, label in [(0.07, "toy MC\n(wrong hint)"), (0.5, "Scruples"), (0.7, "Health\n(patient opinion)")]:
    ax.axvline(x, color="gray", linewidth=0.8, linestyle=":")
    ax.text(x, 0.03, label, ha="center", va="bottom", fontsize=7.5, color="#444444")
# The half-blind monitor of Section 3.1: p0 = 0.5, floor 0.375, influence rate 0.75.
ax.plot([0.5, 0.5], [0.375, 0.75], marker="o", color="black", markersize=4, linestyle="none")
ax.annotate("case (1): floor 0.375,\ninfluence rate 0.75", xy=(0.5, 0.56), xytext=(0.535, 0.60),
            fontsize=7.5, color="#222222")
ax.set_xlim(0, 0.8)
ax.set_ylim(0, 1.02)
ax.set_xlabel("Base rate p₀ = Pr(cue-concordant output | no cue)")
ax.set_ylabel("Share of encouraged cue-concordant draws\n(Z = 1, Y = 1)")
ax.set_title("Floor and influence rate at π = 0.6 (equal baselines)", fontsize=10.5)
ax.spines[["top", "right"]].set_visible(False)
handles = [Line2D([0], [0], color="black", linewidth=2, label="Influence rate π/p₁: what the monitor is asked to detect"),
           Line2D([0], [0], color="black", linewidth=2, linestyle=(0, (4, 2)), label="Floor R_effect = TE/p₁: what the monitor is scored against"),
           Patch(color="#d9d9d9", label="Gap: cue-reliant draws whose output would not have changed")]
fig.legend(handles=handles, loc="lower center", ncol=1, frameon=False, fontsize=7.5, bbox_to_anchor=(0.5, -0.01))
fig.tight_layout(rect=(0, 0.14, 1, 1))
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig1.png"))
