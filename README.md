# Customer Support Ticket Prioritization Dashboard

A Streamlit dashboard to prioritize customer support tickets using sentiment analysis and keyword-based prioritization, built by Kevin for IT portfolio.

## Overview
- **Purpose**: Analyzes customer support tickets to prioritize them as High, Medium, or Low based on urgency keywords (e.g., "urgent," "crash") and sentiment analysis using TextBlob.
- **Tech Stack**: Python 3.12.4, Pandas, TextBlob, Streamlit, Plotly, WordCloud, SQLite.
- **Features**:
  - Pie chart: Priority distribution 
  - Bar chart: Tickets by category.
  - Line chart: Ticket trends over time.
  - Word cloud: Common ticket description words.
  - Filters: Interactive category and priority selection.
  - SQLite: SQL queries for ticket analysis.

## Setup
1. Clone the repository:

```bash
   git clone https://github.com/Keerthi-Vasan-Adhithan/ticket-prioritization-dashboard.git
   cd ticket-prioritization-dashboard
```

2. Install dependencies:

```bash
pip install pandas==2.2.2 textblob==0.18.0.post0 scikit-learn==1.5.1 streamlit==1.39.0 plotly==5.24.1 wordcloud==1.9.3

```

3. Run the dashboard:

```bash
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

### Results:
<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/1a1e5e34-2dea-496e-9793-1da8ad06e30c" />
<img width="1005" height="561" alt="image" src="https://github.com/user-attachments/assets/9a1a6f98-ef14-455c-9666-a87d673d8d1a" />
<img width="998" height="550" alt="image" src="https://github.com/user-attachments/assets/7c82acec-18ee-4322-826f-a6c77e7a20e2" />
<img width="1077" height="513" alt="image" src="https://github.com/user-attachments/assets/f8945e35-20a1-4177-85a0-c6efbf88a0f9" />
<img width="924" height="621" alt="image" src="https://github.com/user-attachments/assets/0d9c4d85-d286-4bdd-8f17-a58f72b67f8d" />

