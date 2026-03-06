# Marketing Analytics Project

This project presents a complete mini analytical pipeline that integrates marketing data from three sources:

Facebook Ads
Google Ads
CRM (revenue data)

The goals of the project are:

merging all sources into one unified dataset
calculating core marketing metrics (CTR, CPC, CPA, ROI)
exporting results to:
a CSV file
a SQL Server database
performing additional analysis in Power BI and Jupyter Notebook

# 1. Project Structure


stock-analysis/
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
└── src/
    ├── data_loader.py
    ├── data_transformation.py
    ├── export_to_files.py
    ├── export_csv.py
    ├── export_sql.py
    └── metrics.py

# 2. How to Run the Project

## 2.1. Create environment

## 2.2. Installation

pip install -r requirements.txt

## 2.3. Configure .env

Create a .env file and provide database connection details:

DB_SERVER=YOUR_SERVER
DB_NAME=MarketingData

## 2.4. Running the Project

python main.py

The script will:

load and merge data from all sources
calculate marketing performance metrics
export processed data to a CSV file inside the output/ directory
insert new records into SQL Server

# 3. Marketing Metrics Calculated
CTR = clicks / impressions
CPC = cost / clicks
CPA = cost / conversions
Conversion Rate = conversions / clicks
ROI = (revenue – cost) / cost

# 4. SQL – Database Structure

The project includes a SQL script that creates:

the CampaignData table
two analytical views:
v_ChannelPerformance
v_TopCampaigns
These views help analyze performance per channel and per campaign.

# 5. Analytical Notebook

In the notebooks/ directory, you will find:

marketing_analysis.ipynb

It contains:

exploratory data analysis (EDA)
charts showing performance metrics
correlation analysis
a foundation for building Power BI dashboards

# 6. License

MIT