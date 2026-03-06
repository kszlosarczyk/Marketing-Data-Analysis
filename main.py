from dotenv import load_dotenv

from src.data_loader import load_data
from src.metrics import calculate_marketing_metrics
from src.export_csv import save_csv
from src.export_sql import export_to_sql


def main():
    """
    Main ETL execution function.
    """
    load_dotenv()

    df = load_data()
    df = calculate_marketing_metrics(df)

    save_csv(df)
    export_to_sql(df)


if __name__ == "__main__":
    main()
