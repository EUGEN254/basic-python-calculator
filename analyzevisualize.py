# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------
# Task 1: Load and Explore Data
# -------------------------
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = iris.target
    df["species"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

    # Display first few rows
    print("First 5 rows:")
    print(df.head())

    # Check data types and missing values
    print("\nDataset Info:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # No missing values in Iris dataset, but if there were:
    # df.fillna(df.mean(), inplace=True)

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"Unexpected error: {e}")

# -------------------------
# Task 2: Basic Data Analysis
# -------------------------
print("\nBasic Statistics:")
print(df.describe())

print("\nMean values per species:")
print(df.groupby("species").mean())

# Example finding
max_sepal_length = df.groupby("species")["sepal length (cm)"].mean().idxmax()
print(f"\nSpecies with highest average sepal length: {max_sepal_length}")

# -------------------------
# Task 3: Visualizations
# -------------------------
plt.figure(figsize=(10, 6))

# Line Chart - Simulated trend (using index as "time")
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart - Sepal Length Trend")
plt.xlabel("Index (Observation)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart - Average Petal Length per Species
df.groupby("species")["petal length (cm)"].mean().plot(kind="bar", color=["skyblue", "orange", "green"])
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.show()

# Histogram - Distribution of Sepal Width
df["sepal width (cm)"].plot(kind="hist", bins=15, color="purple", edgecolor="black")
plt.title("Histogram - Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot - Sepal vs Petal Length
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set2")
plt.title("Scatter Plot - Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
