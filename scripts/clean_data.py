import pandas as pd

try:
    # Load data
    df = pd.read_csv('data/tickets.csv')

    # Convert descriptions to lowercase, remove punctuation
    df['description'] = df['description'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

    # Handle missing values
    df['category'] = df['category'].fillna('General')
    df['description'] = df['description'].fillna('No description provided')
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    # Drop rows with invalid timestamps
    df = df.dropna(subset=['timestamp'])

    # Save cleaned data
    df.to_csv('data/cleaned_tickets.csv', index=False)
    print("Data cleaned and saved to data/cleaned_tickets.csv")
    print("Rows after cleaning:", len(df))
    print("Missing values after cleaning:\n", df.isnull().sum())

except FileNotFoundError:
    print("Error: tickets.csv not found in data/ folder")
except Exception as e:
    print(f"Error: {e}")