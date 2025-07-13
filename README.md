# Customer Support Ticket Prioritization Dashboard

A Streamlit dashboard to prioritize customer support tickets using sentiment analysis and keyword-based prioritization, built by Kevin for IT portfolio.

## Overview
- **Purpose**: Analyzes customer support tickets (700 entries) to prioritize them as High, Medium, or Low based on urgency keywords (e.g., "urgent," "crash") and sentiment analysis using TextBlob.
- **Tech Stack**: Python 3.12.4, Pandas, TextBlob, Streamlit, Plotly, WordCloud, SQLite.
- **Features**:
  - Pie chart: Priority distribution (High: ~257, Medium: ~126, Low: ~317).
  - Bar chart: Tickets by category (Software: 150, Account: 100, etc.).
  - Line chart: Ticket trends over time.
  - Word cloud: Common ticket description words.
  - Filters: Interactive category and priority selection.
  - SQLite: SQL queries for ticket analysis.

## Setup
1. Clone the repository:

```
   git clone https://github.com/Keerthi-Vasan-Adhithan/ticket-prioritization-dashboard.git
   cd ticket-prioritization-dashboard
```

2. Install dependencies:

```
pip install pandas==2.2.2 textblob==0.18.0.post0 scikit-learn==1.5.1 streamlit==1.39.0 plotly==5.24.1 wordcloud==1.9.3

```

3. Run the dashboard:

```
streamlit run app.py

```

### Project Structure
data/: Contains cleaned_tickets.csv, analyzed_tickets.csv.
scripts/: Python scripts for data cleaning, analysis, and SQLite setup.
app.py: Streamlit dashboard.
README.md: Project documentation.

### Usage
Open http://localhost:8501 after running streamlit run app.py.
Use sidebar filters to view specific categories or priorities.
Explore charts and word cloud for ticket insights.

### Portfolio Notes
Demonstrates skills in Python, SQL, NLP (TextBlob), and visualization (Plotly, Streamlit).
Relevant for IT roles like data analyst or support engineer.
Contact: [https://www.linkedin.com/in/keerthi-vasan-adhithan-a9292b247]

### Future Improvements
Add real-time ticket ingestion.
Enhance sentiment analysis with advanced NLP models.
Deploy dashboard online (e.g., Streamlit Cloud).
Built by Keerthi Vasan, 2025.