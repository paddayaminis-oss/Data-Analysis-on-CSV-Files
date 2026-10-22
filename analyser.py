import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
sns.set_theme(style="whitegrid")
os.makedirs("outputs", exist_ok=True)

def analyze_sales():
    # 1. Load Data
    file_path = "data/sales_data.csv"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please run generate_data.py first.")
        return

    df = pd.read_csv(file_path)
    
    # 2. Data Preprocessing
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    print("--- Dataset Overview ---")
    print(df.head(), "\n")

    # 3. Group by Product (Total Sales & Quantity)
    product_summary = df.groupby("Product")[["Total_Sales", "Quantity"]].sum().reset_index()
    product_summary = product_summary.sort_values(by="Total_Sales", ascending=False)
    
    print("--- Sales Summary by Product ---")
    print(product_summary, "\n")

    # 4. Group by Month (Total Sales Trend)
    monthly_summary = df.groupby("Month")["Total_Sales"].sum().reset_index()

    print("--- Monthly Sales Trend ---")
    print(monthly_summary, "\n")

    # 5. Visualizations
    
    # Chart 1: Bar Chart - Total Sales by Product
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=product_summary, 
        x="Product", 
        y="Total_Sales", 
        palette="Blues_r",
        hue="Product",
        legend=False
    )
    plt.title("Total Sales by Product", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Product", fontsize=12)
    plt.ylabel("Total Sales ($)", fontsize=12)
    plt.xticks(rotation=15)
    
    # Add values on top of bars
    for p in ax.patches:
        ax.annotate(
            f"${p.get_height():,.0f}", 
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center', 
            xytext=(0, 8), 
            textcoords='offset points',
            fontsize=10
        )
        
    plt.tight_layout()
    plt.savefig("outputs/product_sales_bar.png", dpi=300)
    plt.close()

    # Chart 2: Line Chart - Monthly Sales Trend
    plt.figure(figsize=(12, 6))
    plt.plot(
        monthly_summary["Month"], 
        monthly_summary["Total_Sales"], 
        marker="o", 
        linewidth=2.5, 
        markersize=8, 
        color="#1f77b4"
    )
    plt.title("Monthly Sales Trend (2025)", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Sales ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("outputs/monthly_sales_trend.png", dpi=300)
    plt.close()

    print("Analysis complete! Charts successfully saved in the 'outputs/' folder.")

if __name__ == "__main__":
    analyze_sales()