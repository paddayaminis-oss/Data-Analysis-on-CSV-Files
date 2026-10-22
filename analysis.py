import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')
total_sales = df.groupby('Product')['Sales'].sum()
total_sales.plot(kind='bar', title='Total Sales by Product')
plt.ylabel('Sales')
plt.show()

monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.ylabel('Sales')
plt.show()
