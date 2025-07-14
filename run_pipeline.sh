#!/bin/bash

log_file="./logs/run.log"
input_dir="./input"
processing_dir="./processing"
report_dir="./reports"

echo "[$(date)] Pipeline started." >> "$log_file"

# Step 1: Download if not exists
dataset_url="https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
dataset_file="$input_dir/diabetes.csv"

if [[ ! -f "$dataset_file" ]]; then
    echo "[$(date)] Downloading dataset from $dataset_url" >> "$log_file"
    wget -O "$dataset_file" "$dataset_url"
    if [[ $? -eq 0 ]]; then
        echo "[$(date)] Dataset downloaded successfully." >> "$log_file"
    else
        echo "[$(date)] Dataset download failed!" >> "$log_file"
        exit 1
    fi
else
    echo "[$(date)] Dataset already exists. Skipping download." >> "$log_file"
fi

# Step 2: Copy to processing directory
filename=$(basename "$dataset_file")
processing_path="$processing_dir/$filename"
cp "$dataset_file" "$processing_path"
echo "[$(date)] Copied $filename to processing directory." >> "$log_file"

# Step 3: Run analysis
python3 analyze_csv.py "$processing_path" "$report_dir"
if [ $? -eq 0 ]; then
    echo "[$(date)] Analysis completed successfully." >> "$log_file"
else
    echo "[$(date)] Analysis failed!" >> "$log_file"
    exit 1
fi
