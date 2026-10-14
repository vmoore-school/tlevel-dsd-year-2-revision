"""Analyse Task 3a-style survey feedback with pandas and matplotlib (lesson 03.02).

Run from the repository root:  python curriculum/03-sources-and-feedback/02-gathering-feedback-data/resources/analyse_feedback.py
Needs: pip install pandas matplotlib
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "sample-data" / "feedback-responses.csv"
KPI_EASE_TARGET = 4.0          # example KPI: average ease-of-booking rating of at least 4/5
KPI_COMPLETION_TARGET = 0.9    # example KPI: 90% of users complete all tasks

df = pd.read_csv(DATA)

print(f"Responses: {len(df)}  (technical: {(df.audience == 'Technical').sum()})\n")

# 1. Quantitative: averages by device
by_device = df.groupby("device")[["ease_of_booking_1to5", "layout_clarity_1to5"]].mean().round(2)
print("Average ratings by device:\n", by_device, "\n")

# 2. KPIs
ease = df["ease_of_booking_1to5"].mean()
completion = (df["completed_all_tasks"] == "Yes").mean()
print(f"KPI ease of booking: {ease:.2f} (target {KPI_EASE_TARGET}) -> {'MET' if ease >= KPI_EASE_TARGET else 'NOT MET'}")
print(f"KPI task completion: {completion:.0%} (target {KPI_COMPLETION_TARGET:.0%}) -> "
      f"{'MET' if completion >= KPI_COMPLETION_TARGET else 'NOT MET'}\n")

# 3. Qualitative: most common improvement suggestions
print("Top improvement suggestions:\n", df["improvement_suggestion"].value_counts().head(5), "\n")

# 4. Technical feedback
print("Technical comments:")
for comment in df.loc[df.audience == "Technical", "technical_comment"].dropna():
    print(" -", comment)

# 5. Chart
ax = by_device.plot(kind="bar", rot=0, title="Average rating by device (1-5)")
ax.set_xlabel("Device")
ax.set_ylabel("Average rating")
ax.axhline(KPI_EASE_TARGET, linestyle="--", color="grey", label="KPI target")
ax.legend()
plt.tight_layout()
out = Path(__file__).with_name("ratings_by_device.png")
plt.savefig(out)
print(f"\nChart saved to {out}")
