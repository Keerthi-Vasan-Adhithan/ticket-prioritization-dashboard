import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

try:
    # Load analyzed data
    df = pd.read_csv('data/analyzed_tickets.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Streamlit app
    st.title("Customer Support Ticket Prioritization Dashboard - Keerthi Vasan")
    st.write("Analyze and prioritize customer support tickets by urgency and category.")

    # Filters
    st.sidebar.header("Filters")
    categories = ['All'] + sorted(df['category'].unique().tolist())
    selected_category = st.sidebar.selectbox("Select Category", categories)
    priorities = ['All'] + sorted(df['priority'].unique().tolist())
    selected_priority = st.sidebar.selectbox("Select Priority", priorities)

    # Apply filters
    filtered_df = df
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
    if selected_priority != 'All':
        filtered_df = filtered_df[filtered_df['priority'] == selected_priority]

    # Pie chart: Priority distribution
    priority_counts = filtered_df['priority'].value_counts().reset_index()
    priority_counts.columns = ['priority', 'count']
    fig_pie = px.pie(priority_counts, values='count', names='priority', 
                    title='Ticket Priority Distribution', 
                    color_discrete_sequence=['#FF4B4B', '#FFA500', '#4CAF50'])
    st.plotly_chart(fig_pie)

    # Bar chart: Tickets by category
    category_counts = filtered_df['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']
    fig_bar = px.bar(category_counts, x='category', y='count', 
                    title='Tickets by Category', 
                    color='category', 
                    color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig_bar)

    # Line chart: Tickets over time
    filtered_df['date'] = filtered_df['timestamp'].dt.date
    tickets_over_time = filtered_df.groupby('date').size().reset_index(name='count')
    fig_line = px.line(tickets_over_time, x='date', y='count', 
                      title='Tickets Over Time', 
                      markers=True)
    st.plotly_chart(fig_line)

    # Word cloud: Common words in descriptions
    st.subheader("Word Cloud of Ticket Descriptions")
    text = ' '.join(filtered_df['description'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
    st.image(f"data:image/png;base64,{img_str}")
    plt.close()

    # Display filtered tickets
    st.subheader("Filtered Tickets")
    st.dataframe(filtered_df[['ticket_id', 'description', 'category', 'priority', 'sentiment_label']].head(10))

except FileNotFoundError:
    st.error("Error: analyzed_tickets.csv not found in data/ folder")
except Exception as e:
    st.error(f"Error: {e}")
