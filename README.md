# CSV Data Quality Checker (Bash + Python)

This is a simple, modular data quality pipeline built using **Bash** and **Python**.  
It automates the process of downloading a dataset, preparing it, and analyzing it for basic data quality issues such as missing values and outliers.

---

## 🔧 What It Does

1. **Checks if the dataset exists locally** — if not, downloads it.
2. **Copies** the dataset to a processing directory.
3. **Analyzes** the dataset using Python:
   - Record count
   - Missing values per column
   - Outliers in numeric columns
4. **Outputs** a text report
5. **Logs** all actions

---

## 📁 Project Structure

csv-quality-checker/
├── input/ # Original dataset (downloaded once)
├── processing/ # Working copy for analysis
├── reports/ # Text reports (per file)
├── logs/ # Execution logs
├── run_pipeline.sh # Main Bash script
├── analyze_csv.py # Python script for analysis
└── README.md # Documentation

 
## 🚀 How to Run

### 1. Clone the project
`bash
git clone https://github.com/YOUR_USERNAME/csv-quality-checker.git
cd csv-quality-checker
2. Create and activate virtual environment (for Python libraries)
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy
3. Make the Bash script executable
chmod +x run_pipeline.sh
4. Run the pipeline
./run_pipeline.sh
📄 Output Files
input/diabetes.csv – Raw dataset

processing/diabetes.csv – Working copy

reports/report_diabetes.txt – Text report (record count, missing values, outliers)

logs/run.log – Execution logs

📊 Dataset Source
Diabetes Dataset (by Plotly)


✅ Sample Report Output

File: processing/diabetes.csv
Total Records: 768

Missing Values Per Column:
Pregnancies        0
Glucose            0
BloodPressure      0
SkinThickness      0
Insulin            0
BMI                0
DiabetesPedigree   0
Age                0
Outcome            0

Outliers Per Numeric Column:
Pregnancies: 79 outliers
Glucose: 27 outliers
BloodPressure: 35 outliers
...


👤 Author
Abdullah Gaballah
