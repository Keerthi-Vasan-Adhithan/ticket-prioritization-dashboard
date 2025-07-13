import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect('data/tickets.db')
    df = pd.read_sql_query("SELECT * FROM tickets LIMIT 5", conn)
    print("Database contents:")
    print(df)
    # Example SQL query: Count tickets by category
    category_counts = pd.read_sql_query("SELECT category, COUNT(*) as count FROM tickets GROUP BY category", conn)
    print("Tickets by category:")
    print(category_counts)
    conn.close()
except Exception as e:
    print(f"Error: {e}")