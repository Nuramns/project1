import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Sales Dashboard")

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Rename for easier handling
df.rename(columns={'Revenue ($)': 'Revenue'}, inplace=True)

# Drop any missing values in required columns
df = df.dropna(subset=['Month', 'Region', 'Revenue'])

# Sidebar filter
selected_month = st.sidebar.selectbox("Select Month", sorted(df['Month'].unique(), reverse=True))

# Filter by selected month
filtered_df = df[df['Month'] == selected_month]

# Group by Region and sum Revenue
revenue_by_region = filtered_df.groupby('Region')['Revenue'].sum().reset_index()

# Display bar chart
st.subheader(f"Total Revenue by Region – {selected_month}")
fig, ax = plt.subplots()
ax.bar(revenue_by_region['Region'], revenue_by_region['Revenue'], color='skyblue')
ax.set_xlabel("Region")
ax.set_ylabel("Total Revenue ($)")
ax.set_title("Revenue by Region")
st.pyplot(fig)
