import os
from datetime import datetime


def save_csv(df, output_dir="output"):
    """
    Save final dataset to a timestamped CSV file.
    """
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.today().strftime("%Y-%m-%d")

    file_path = f"{output_dir}/analysis_{today}.csv"
    df.to_csv(file_path, index=False, encoding="utf-8")

    print(f"File saved as {file_path}")
    return file_path
