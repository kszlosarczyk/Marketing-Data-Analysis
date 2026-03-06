# Marketing Analysis

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

marketing-analysis/
├── .env
├── main.py
├── requirements.txt
├── marketing_analysis.ipynb
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
│   ├── __init__.py
│   ├── data_loader.py
│   ├── export_csv.py
│   ├── export_sql.py
│   ├── metrics.py

# 6. Power BI Dashboard

A Power BI dashboard has been created to visualize marketing performance data.

The dashboard is based on the exported data and SQL views (v_ChannelPerformance, v_TopCampaigns).

It provides interactive charts and tables for:

- Campaign performance per channel
- ROI, CTR, CPC, CPA metrics
- Top performing campaigns

Note: The .pbix file is not included in this repository. Use the exported CSV files or SQL views to explore the dashboard in Power BI Desktop.

This allows stakeholders to interactively analyze marketing campaigns without including the raw Power BI project file.

# 7. How to Run the Project

## 7.1 Create Environment
python -m venv venv
Activate the environment.

## 7.2 Install Dependencies
pip install -r requirements.txt

## 7.3 Configure Environment Variables
Create a .env file with database connection details:

DB_SERVER=YOUR_SERVER
DB_NAME=MarketingData

## 7.4 Create db and views in SQL Server

In sql/ folder you can find two scripts:

Create db and tables:
sql/create DB.sql

Create views:
sql/create views.sql

## 7.5 Run the Pipeline
python main.py

The script will:
- load marketing data from CSV files
- merge datasets
- calculate marketing metrics
- export results to CSV
- insert records into SQL Server

# 8. Analytical Notebook

The directory contains:
marketing_analysis.ipynb

The notebook includes:
- exploratory data analysis (EDA)
- marketing performance visualizations
- correlation analysis
- preparation for Power BI dashboards

# 9. Technology Stack

Power BI
Python
pandas
numpy
SQL Server
matplotlib
seaborn
python-dotenv
Jupyter Notebook

# 10. License
MIT License