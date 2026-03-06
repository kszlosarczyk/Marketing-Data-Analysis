import pandas as pd


def safe(series):
    """
    Replace zeros with NA to avoid division-by-zero errors.
    """
    return series.replace({0: pd.NA})


def calculate_marketing_metrics(df):
    """
    Calculate CTR, CPC, CPA, Conversion Rate and ROI.
    """
    df["CTR"] = df["clicks"] / safe(df["impressions"])
    df["CPC"] = df["cost"] / safe(df["clicks"])
    df["CPA"] = df["cost"] / safe(df["conversions"])
    df["Conversion_Rate"] = df["conversions"] / safe(df["clicks"])
    df["ROI"] = (df["revenue"] - df["cost"]) / safe(df["cost"])

    return df
