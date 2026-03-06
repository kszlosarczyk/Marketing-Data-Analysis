# Marketing Analytics

# 1. Project Overview

This project demonstrates a complete marketing analytics pipeline in Python that integrates data from multiple marketing platforms and a CRM system.

The pipeline performs data extraction, transformation, metric calculation, and exports results for further analysis in SQL Server, Power BI, and Jupyter Notebook.

The project follows a simplified ETL workflow:

Extract → Transform → Analyze → Export

# 2. Project Goals

The project aims to:
- Integrate marketing data from multiple sources
- Create a unified dataset combining advertising and revenue data
- Calculate core marketing performance metrics
- Export processed data to analytical formats
- Enable further analysis in SQL Server, Power BI, and Jupyter Notebook

# 3. Data Sources

The project integrates data from three sources:

- Facebook Ads
    - impressions
    - clicks
    - cost

- Google Ads
    - impressions
    - clicks
    - cost

- CRM System
    - conversions
    - revenue

All sources are merged into a single analytical dataset.

# 4. Marketing Metrics Calculated

The following performance metrics are computed:

CTR = clicks / impressions
CPC = cost / clicks
CPA = cost / conversions
Conversion Rate = conversions / clicks
ROI = (revenue − cost) / cost

These metrics allow evaluation of campaign efficiency and channel performance.

# 5. Project Structure

marketing-analytics/
├── .env
├── config.py
├── main.py
├── requirements.txt
│
├── data/
│   ├── ads_facebook.csv
│   ├── ads_google.csv
│   └── crm_sales.csv
│
├── output/
│
├── powerbi/
│   ├── dashboards.pdf
│
├── sql/
│   ├── create DB.sql
│   ├── create views.sql
│
├── src/
│   ├── data_loader.py
│   ├── data_transformation.py
│   ├── metrics.py
│   ├── export_csv.py
│   ├── export_sql.py
│   └── export_to_files.py
│
└── notebooks/
    └── marketing_analysis.ipynb

# 6. How to Run the Project

## 6.1 Create Environment
python -m venv venv
Activate the environment.

## 6.2 Install Dependencies
pip install -r requirements.txt

## 6.3 Configure Environment Variables
Create a .env file with database connection details:

DB_SERVER=YOUR_SERVER
DB_NAME=MarketingData

## 6.4 Create db and views in SQL Server

In sql/ folder you can find two scripts:

-- Create db and tables
sql/create DB.sql

-- Create views
sql/create views.sql

## 6.5 Run the Pipeline
python main.py

The script will:
- load marketing data from CSV files
- merge datasets
- calculate marketing metrics
- export results to CSV
- insert records into SQL Server

# 7. Analytical Notebook

The directory contains:
marketing_analysis.ipynb

The notebook includes:
- exploratory data analysis (EDA)
- marketing performance visualizations
- correlation analysis
- preparation for Power BI dashboards

# 8. Technology Stack

Python
pandas
numpy
SQL Server
matplotlib
seaborn
python-dotenv
Jupyter Notebook

# 9. License
MIT License