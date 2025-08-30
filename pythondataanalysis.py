import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
df = pd.read_csv("sales_data.csv")

# Step 2: Calculate total revenue
total_revenue = df["Revenue ($)"].sum()

# Step 3: Find best-selling product
best_selling = df.groupby("Product")["Quantity Sold"].sum().idxmax()
best_selling_qty = df.groupby("Product")["Quantity Sold"].sum().max()

# Step 4: Find highest sales day (by revenue)
highest_sales_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

# Step 5: Save results to text file
summary = (
    f"Total Revenue: ${total_revenue}\n"
    f"Best-Selling Product: {best_selling} ({best_selling_qty} units sold)\n"
    f"Highest Sales Day: {highest_sales_day}\n"
)

with open("sales_summary.txt", "w") as file:
    file.write(summary)

print(summary)

# Bonus: Visualize sales trends
plt.figure(figsize=(8, 4))
daily_sales = df.groupby("Date")["Revenue ($)"].sum()
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
