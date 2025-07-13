import pandas as pd
from textblob import TextBlob

try:
    # Load cleaned data
    df = pd.read_csv('data/cleaned_tickets.csv')

    # Sentiment analysis
    df['sentiment'] = df['description'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df['sentiment_label'] = df['sentiment'].apply(
        lambda x: 'negative' if x < 0 else 'positive' if x > 0 else 'neutral'
    )

    # Prioritize tickets
    def prioritize_ticket(row):
        urgent_keywords = ['urgent', 'crash', 'critical', 'down', 'timeout', 'error', 'not working', 'failure', 'denied', 'corruption']
        medium_keywords = ['help', 'issue', 'problem', 'slow', 'assistance', 'query']
        if any(word in row['description'] for word in urgent_keywords) or row['sentiment'] < 0:
            return 'High'
        elif any(word in row['description'] for word in medium_keywords):
            return 'Medium'
        return 'Low'

    df['priority'] = df.apply(prioritize_ticket, axis=1)

    # Save results
    df.to_csv('data/analyzed_tickets.csv', index=False)
    print("Analysis complete, saved to data/analyzed_tickets.csv")
    print("Priority distribution:")
    print(df['priority'].value_counts())
    print("Sentiment distribution:")
    print(df['sentiment_label'].value_counts())
    print("Tickets by category:")
    print(df.groupby('category').size())

except FileNotFoundError:
    print("Error: cleaned_tickets.csv not found")
except Exception as e:
    print(f"Error: {e}")