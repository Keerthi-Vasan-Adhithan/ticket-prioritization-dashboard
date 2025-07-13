import pandas as pd

try:
    df = pd.read_csv('data/analyzed_tickets.csv')
    print("Analyzed dataset loaded successfully!")
    print("First 5 rows:")
    print(df.head())
    print("Columns:", df.columns.tolist())
    print("Rows:", len(df))
    print("Sample priorities:", df['priority'].head().tolist())
    print("Priority counts:", df['priority'].value_counts().to_dict())
    print("Sentiment counts:", df['sentiment_label'].value_counts().to_dict())
except FileNotFoundError:
    print("Error: analyzed_tickets.csv not found")
except Exception as e:
    print(f"Error: {e}")