import pandas as pd

try:
    df = pd.read_csv('data/tickets.csv')
    print("Dataset loaded successfully!")
    print("First 5 rows:")
    print(df.head())
    print("Columns:", df.columns.tolist())
    print("Rows:", len(df))
    print("Missing values:\n", df.isnull().sum())
except FileNotFoundError:
    print("Error: tickets.csv not found in data/ folder")
except pd.errors.ParserError:
    print("Error: Check CSV format (commas, headers)")
except Exception as e:
    print(f"Error: {e}")