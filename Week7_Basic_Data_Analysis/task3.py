import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.read_csv('dataset.csv')

# Assume we have a 'Date' column and a 'Sales' column

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Grouping by a categorical column (e.g., 'Category') and calculating the mean
grouped_data = data.groupby('Category')['Value'].mean().reset_index()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Category'], grouped_data['Value'], color='lightgreen')
plt.title('Average Value by Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Value'], bins=15, color='purple', edgecolor='black')
plt.title('Distribution of Value')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['SepalLength'], data['PetalLength'], color='orange', alpha=0.6)
plt.title('Relationship Between Sepal Length and Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.grid(True)
plt.show()
