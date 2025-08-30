import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: NumPy - Create array and calculate mean
arr = np.arange(1, 11)  # Numbers 1 to 10
mean_value = np.mean(arr)
print("NumPy Array:", arr)
print("Mean of Array:", mean_value)

# Task 2: Pandas - Create DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, 27, 22, 29],
    'Score': [85, 90, 88, 92]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# Task 3: Requests - Fetch data from a public API
response = requests.get("https://api.github.com")
if response.status_code == 200:
    data = response.json()
    print("\nPublic API Data (GitHub):")
    print("Current User URL:", data.get("current_user_url"))
else:
    print("Failed to fetch data from API.")

# Task 4: Matplotlib - Plot a simple line graph
plt.plot(arr, arr**2, marker='o')  # Plot numbers and their squares
plt.title("Line Graph: Numbers vs Squares")
plt.xlabel("Number")
plt.ylabel("Square of Number")
plt.grid(True)
plt.show()
