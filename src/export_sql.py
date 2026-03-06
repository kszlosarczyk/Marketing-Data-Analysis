import os
import urllib
import pandas as pd
from sqlalchemy import create_engine


def export_to_sql(df):
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")

    params = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    conn_str = "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(params)
    engine = create_engine(conn_str)

    key_query = """
        SELECT campaign_id, date
        FROM dbo.CampaignData
    """

    with engine.connect() as conn:
        keys_sql = pd.read_sql(key_query, conn)

    keys_sql["date"] = pd.to_datetime(keys_sql["date"])

    merged = df.merge(
        keys_sql,
        on=["campaign_id", "date"],
        how="left",
        indicator=True
    )

    df_to_export = merged[merged["_merge"] == "left_only"].copy()
    df_to_export = df_to_export.drop(columns="_merge")

    if df_to_export.empty:
        print("No new rows to insert (all keys already exist).")
        return

    print(f"Preparing to insert {len(df_to_export)} rows into SQL...")

    with engine.begin() as conn:
        df_to_export.to_sql(
            name="CampaignData",
            con=conn,
            schema="dbo",
            if_exists="append",
            index=False
        )

    print(f"Inserted {len(df_to_export)} new rows successfully.")
