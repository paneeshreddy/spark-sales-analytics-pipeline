# spark-sales-analytics-pipeline

## 🚀 Spark Sales ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/PySpark-3.5.0-orange)](https://spark.apache.org/)

---

## 💡 Project Overview

This project is a **Batch ETL pipeline** built with **PySpark** to process raw sales data, calculate analytics, and save processed outputs.  

It demonstrates skills in:  
- Data extraction, transformation, and loading (ETL)  
- Analytics using Spark DataFrames and SQL  
- Handling large datasets efficiently with PySpark  
- Generating meaningful business insights from raw sales data  

---

## 🛠 Tech Stack

- Python 3.x  
- PySpark 3.5.0  
- Pandas (optional, for validation or additional analytics)  
- CSV files for input and output  

---

## 📁 Project Structure

spark-sales-analytics-pipeline/
│
├─ data/
│ ├─ raw/ # Raw input CSV (sales.csv)
│ └─ processed/ # Processed outputs (ignored in Git)
│
├─ spark_etl/
│ ├─ extract.py # Extracts data from CSV
│ ├─ transform.py # Aggregates and computes analytics
│ ├─ load.py # Saves processed data
│ └─ run_pipeline.py # Orchestrates the ETL pipeline
│
├─ scripts/
│ └─ create_spark_session.py # Spark session setup
│
├─ requirements.txt # Project dependencies
└─ README.md # Project documentation




## ⚡ How to Run the Pipeline

1. Install dependencies:

```bash
pip install -r requirements.txt


2. Run the ETL pipeline:

PYTHONPATH=. python3 spark_etl/run_pipeline.py
Processed output files will be saved in data/processed/.

📊 Outputs

| File / Folder        | Description                    |
| -------------------- | ------------------------------ |
| `sales_transformed/` | Full transformed sales dataset |
| `total_revenue/`     | Total revenue by country       |
| `total_quantity/`    | Total quantity sold by country |
| `top_products/`      | Top 5 products by revenue      |
| `daily_revenue/`     | Revenue trends by date         |
