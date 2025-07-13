import pandas as pd

try:
    df = pd.read_csv('data/cleaned_tickets.csv')
    print("Cleaned dataset loaded successfully!")
    print("First 5 rows:")
    print(df.head())
    print("Columns:", df.columns.tolist())
    print("Rows:", len(df))
    print("Sample descriptions:", df['description'].head().tolist())
    print("Unique categories:", df['category'].unique())
    print("Timestamp range:", df['timestamp'].min(), "to", df['timestamp'].max())
except FileNotFoundError:
    print("Error: cleaned_tickets.csv not found")
except Exception as e:
    print(f"Error: {e}")