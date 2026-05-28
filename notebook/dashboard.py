import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="E-Commerce Analytics", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
    }
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }
    .stMetric {
        background-color: #1E2129;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .css-1d391kg {
        background-color: #1E2129;
    }
</style>
""", unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/dashboard/clean_data.csv"
    df = pd.read_csv(url)
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.title("Filters")

# State Filter
state = st.sidebar.multiselect("Select State", options=df['customer_state'].unique(), default=[])
if state:
    df = df[df['customer_state'].isin(state)]

# Date Range Filter
min_date = df['order_purchase_timestamp'].min().date()
max_date = df['order_purchase_timestamp'].max().date()
start_date, end_date = st.sidebar.date_input("Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

df = df[(df['order_purchase_timestamp'].dt.date >= start_date) & (df['order_purchase_timestamp'].dt.date <= end_date)]

# --- MAIN DASHBOARD ---
st.title("E-Commerce Performance Dashboard")
st.markdown("Monitor sales trends, product performance, and customer behavior.")

# --- KEY METRICS ---
total_revenue = df['payment_value'].sum()
total_orders = df['order_id'].nunique()
total_customers = df['customer_id'].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Total Customers", f"{total_customers:,}")
col4.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

# --- CHARTS ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Monthly Revenue Trend")
    monthly = df.groupby('order_month')['payment_value'].sum().reset_index()
    fig_line = px.line(monthly, x='order_month', y='payment_value', markers=True, 
                       line_shape='spline', color_discrete_sequence=['#00E5FF'])
    fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    st.subheader("Top 10 Product Categories")
    category = df.groupby('product_category_name')['payment_value'].sum().sort_values(ascending=True).tail(10).reset_index()
    fig_bar = px.bar(category, x='payment_value', y='product_category_name', orientation='h',
                     color='payment_value', color_continuous_scale='Tealgrn')
    fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white', showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)


st.markdown("---")

col_bottom1, col_bottom2 = st.columns(2)

with col_bottom1:
    st.subheader("Payment Methods")
    payment = df['payment_type'].value_counts().reset_index()
    payment.columns = ['payment_type', 'count']
    fig_pie = px.pie(payment, names='payment_type', values='count', hole=0.4, 
                     color_discrete_sequence=['#00E5FF', '#FF007F', '#FFD700', '#00FA9A'])
    fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig_pie, use_container_width=True)

with col_bottom2:
    st.subheader("Customer Segmentation (RFM)")
    
    # Calculate RFM
    reference_date = df['order_purchase_timestamp'].max()
    rfm = df.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (reference_date - x.max()).days,
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index()
    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']
    
    # Simple Binning for Dashboard speed
    rfm['R_score'] = pd.qcut(rfm['recency'].rank(method='first'), 3, labels=[3,2,1])
    rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 3, labels=[1,2,3])
    rfm['M_score'] = pd.qcut(rfm['monetary'].rank(method='first'), 3, labels=[1,2,3])
    rfm['RFM_score'] = rfm[['R_score','F_score','M_score']].astype(int).sum(axis=1)
    
    rfm['segment'] = 'Low Value'
    rfm.loc[rfm['RFM_score'] >= 7, 'segment'] = 'High Value'
    rfm.loc[(rfm['RFM_score'] >= 5) & (rfm['RFM_score'] < 7), 'segment'] = 'Mid Value'
    
    segment_counts = rfm['segment'].value_counts().reset_index()
    segment_counts.columns = ['segment', 'count']
    fig_funnel = px.funnel(segment_counts, x='count', y='segment', color='segment',
                           color_discrete_map={'High Value': '#00E5FF', 'Mid Value': '#00B4D8', 'Low Value': '#03045E'})
    fig_funnel.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig_funnel, use_container_width=True)

# --- INSIGHTS ---
with st.expander("View Key Insights"):
    st.markdown("""
    - **Revenue Growth**: Revenue experienced a significant upward trend peaking at the end of 2017.
    - **Top Products**: Categories like *cama_mesa_banho* and *beleza_saude* dominate the sales volume.
    - **Payment Preferences**: *Credit Card* is the overwhelmingly preferred payment method, indicating trust and convenience.
    - **Customer Value**: Identifying **High Value** customers allows for targeted marketing and loyalty programs.
    """)