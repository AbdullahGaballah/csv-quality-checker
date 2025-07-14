#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import os

# Check args
if len(sys.argv) != 3:
    print("Usage: analyze_csv.py <input_csv> <output_dir>")
    sys.exit(1)

# Paths
csv_path = sys.argv[1]
output_dir = sys.argv[2]
filename = os.path.basename(csv_path).replace(".csv", "")
report_path = os.path.join(output_dir, f"report_{filename}.txt")

# Load
try:
    df = pd.read_csv(csv_path)
except Exception as e:
    print(f"[ERROR] Failed to read CSV: {e}")
    sys.exit(1)

# Report
report_lines = []
report_lines.append(f"File: {csv_path}")
report_lines.append(f"Total Records: {len(df)}")

report_lines.append("\nMissing Values Per Column:")
report_lines.append(str(df.isnull().sum()))

report_lines.append("\nOutliers Per Numeric Column:")
numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    report_lines.append(f"{col}: {len(outliers)} outliers")

# Save
try:
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))
    print(f"[INFO] Report saved to {report_path}")
except Exception as e:
    print(f"[ERROR] Failed to write report: {e}")
    sys.exit(1)
