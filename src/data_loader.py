import pandas as pd
from pathlib import Path


def validate_columns(df, required_cols, source_name):
    """
    Validate that required columns exist in the DataFrame.
    """
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in {source_name}: {missing}")


def load_data():
    """
    Load Facebook, Google Ads, and CRM data.
    Merge them into a single DataFrame.
    """
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data"

    required_ads_cols = [
        "date", "campaign_id", "impressions", "clicks", "cost", "conversions"
    ]
    required_crm_cols = ["date", "campaign_id", "revenue"]

    df_fb = pd.read_csv(data_dir / "ads_facebook.csv", dtype={"campaign_id": "string"})
    df_ads = pd.read_csv(data_dir / "ads_google.csv", dtype={"campaign_id": "string"})
    df_crm = pd.read_csv(data_dir / "crm_sales.csv", dtype={"campaign_id": "string"})

    validate_columns(df_fb, required_ads_cols, "Facebook Ads")
    validate_columns(df_ads, required_ads_cols, "Google Ads")
    validate_columns(df_crm, required_crm_cols, "CRM Sales")

    df = pd.concat([df_ads, df_fb], ignore_index=True)

    df["date"] = pd.to_datetime(df["date"])
    df_crm["date"] = pd.to_datetime(df_crm["date"])

    df = df.merge(df_crm, on=["campaign_id", "date"], how="left")

    return df
