import sqlite3
import pandas as pd

try:
    # Load cleaned data
    df = pd.read_csv('data/cleaned_tickets.csv')

    # Connect to SQLite database
    conn = sqlite3.connect('data/tickets.db')
    df.to_sql('tickets', conn, if_exists='replace', index=False)
    conn.close()
    print("Database created successfully at data/tickets.db")
except FileNotFoundError:
    print("Error: cleaned_tickets.csv not found")
except Exception as e:
    print(f"Error: {e}")