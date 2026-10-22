import os
import pandas as pd
import numpy as np

# Create data directory
os.makedirs("data", exist_ok=True)

# Generate sample sales data
np.random.seed(42)
date_range = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
products = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet"]

data = {
    "Date": np.random.choice(date_range, size=1000),
    "Product": np.random.choice(products, size=1000),
    "Quantity": np.random.randint(1, 6, size=1000),
    "Unit_Price": np.random.choice([800, 500, 100, 200, 300], size=1000)
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]
df = df.sort_values("Date").reset_index(drop=True)

# Save to CSV
df.to_csv("data/sales_data.csv", index=False)
print("Sample sales_data.csv generated successfully in the 'data/' folder!")