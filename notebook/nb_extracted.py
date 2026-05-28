# --- Code Cell 5 ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# --- Code Cell 8 ---
clean_df = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/dashboard/clean_data.csv")
customers = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/data/customers_dataset.csv")
orders = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/data/orders_dataset.csv")
order_items = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/data/order_items_dataset.csv")
payments = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/data/order_payments_dataset.csv")
reviews = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/data/order_reviews_dataset.csv")
products = pd.read_csv("https://raw.githubusercontent.com/louiee-jason/ecommerce-dashboard-analysis/main/data/products_dataset.csv")


# --- Code Cell 9 ---
df1 = orders.merge(order_items, on='order_id')
df2 = df1.merge(products, on='product_id')
df3 = df2.merge(customers, on='customer_id')
df = df3.merge(payments, on='order_id')


# --- Code Cell 11 ---
df.head()


# --- Code Cell 12 ---
df.info()


# --- Code Cell 14 ---
df = df[[
    'order_id',
    'customer_id',
    'order_purchase_timestamp',
    'product_category_name',
    'payment_value',
    'customer_city',
    'customer_state',
    'price',
    'freight_value',
    'payment_type',
    'payment_installments'
]]


# --- Code Cell 15 ---
df.head()


# --- Code Cell 17 ---
df['product_category_name'].value_counts() #check distribution


# --- Code Cell 18 ---
sns.boxplot(x=df['payment_value']) #check outlier
plt.title('Boxplot Before Outlier Removal')
plt.show()


# --- Code Cell 21 ---
df.isnull().sum()


# --- Code Cell 22 ---
df.duplicated().sum()


# --- Code Cell 23 ---
# handle missing values
df['product_category_name'].fillna('unknown', inplace=True)

# cek ulang missing values
df.isnull().sum()

# cek duplicate
df.duplicated().sum()

# convert tipe data timestamp ke datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])


# --- Code Cell 24 ---
df.isnull().sum()


# --- Code Cell 25 ---
# =========================
# Missing Value Chart
# =========================

import pandas as pd
import matplotlib.pyplot as plt

# Calculate missing values
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

# Plot
plt.figure(figsize=(12,6))
missing.plot(kind='bar')

plt.title('Missing Values per Column')
plt.xlabel('Columns')
plt.ylabel('Number of Missing Values')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --- Code Cell 26 ---
df.info() #cek ulang tipe data


# --- Code Cell 27 ---
# handle outlier
Q1 = df['payment_value'].quantile(0.25)
Q3 = df['payment_value'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['payment_value'] >= lower_bound) & (df['payment_value'] <= upper_bound)]


# --- Code Cell 28 ---
# check outlier after iqr

sns.boxplot(x=df['payment_value'])
plt.title('Boxplot After Outlier Removal')
plt.show()


# --- Code Cell 32 ---
df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M')

monthly = df.groupby('order_month').agg({
    'order_id': 'nunique',
    'payment_value': 'sum'
}).reset_index()

monthly


# --- Code Cell 35 ---
category_revenue = df.groupby('product_category_name').agg({
    'payment_value': 'sum'
}).sort_values(by='payment_value', ascending=False)

category_revenue.head(10)


# --- Code Cell 38 ---
payment_dist = df['payment_type'].value_counts()

payment_dist


# --- Code Cell 42 ---
df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M')

monthly = df.groupby('order_month').agg({
    'order_id': 'nunique',
    'payment_value': 'sum'
}).reset_index()
monthly['order_month'] = monthly['order_month'].dt.to_timestamp()
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly, x='order_month', y='payment_value')
plt.xticks(rotation=45)
plt.title('Monthly Revenue Trend')
plt.show()


# --- Code Cell 45 ---
top_category = category_revenue.head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_category['payment_value'], y=top_category.index)
plt.title('Top 10 Product Categories by Revenue')
plt.xlabel('Total Revenue')
plt.ylabel('Product Category')
plt.show()


# --- Code Cell 48 ---
plt.figure(figsize=(6,6))
plt.pie(payment_dist, labels=payment_dist.index, autopct='%1.1f%%')
plt.title('Payment Method Distribution')
plt.show()


# --- Code Cell 51 ---
# RFM Analysis
reference_date = df['order_purchase_timestamp'].max()

rfm = df.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (reference_date - x.max()).days,
    'order_id': 'nunique',
    'payment_value': 'sum'
}).reset_index()

rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']


# --- Code Cell 52 ---
# Binning
rfm['R_score'] = pd.qcut(rfm['recency'], 3, labels=[3,2,1])
rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 3, labels=[1,2,3])
rfm['M_score'] = pd.qcut(rfm['monetary'], 3, labels=[1,2,3])


# --- Code Cell 53 ---
# hitung total score r f m
rfm['RFM_score'] = rfm[['R_score','F_score','M_score']].astype(int).sum(axis=1)


# --- Code Cell 54 ---
# customer segmentation
rfm['segment'] = 'Low Value'
rfm.loc[rfm['RFM_score'] >= 7, 'segment'] = 'High Value'
rfm.loc[(rfm['RFM_score'] >= 5) & (rfm['RFM_score'] < 7), 'segment'] = 'Mid Value'


# --- Code Cell 55 ---
display(rfm.head())


# --- Code Cell 56 ---
print(rfm['segment'].value_counts())


# --- Code Cell 57 ---
display(rfm.groupby('segment')[['recency','frequency','monetary']].mean())


# --- Code Cell 58 ---
df_sample = df.sample(n=20000, random_state=42) #download data untuk dashboard, karena ukuran terlalu besar untuk github sehingga dilakukan sampling agar ukuran dataset lebih kecil
df_sample.to_csv('main_data.csv', index=False)

