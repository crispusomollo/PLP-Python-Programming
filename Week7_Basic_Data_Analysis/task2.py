# Step 1: Import the pandas library
import pandas as pd

# Load the dataset (replace 'dataset.csv' with your file path)
data = pd.read_csv('dataset.csv')

# Step 2: Compute basic statistics of numerical columns
print("Basic statistics for numerical columns:")
print(data.describe())

# Step 3: Group by a categorical column and calculate the mean for a numerical column
# Replace 'Category' with the name of your categorical column
# Replace 'Value' with the name of your numerical column
grouped_data = data.groupby('Category')['Value'].mean().reset_index()

print("\nMean of 'Value' for each 'Category':")
print(grouped_data)

# Step 4: Identify patterns or interesting findings
# Example: Check if there are any categories with significantly higher or lower mean values
highest_mean = grouped_data.loc[grouped_data['Value'].idxmax()]
lowest_mean = grouped_data.loc[grouped_data['Value'].idxmin()]

print("\nCategory with the highest mean 'Value':")
print(highest_mean)

print("\nCategory with the lowest mean 'Value':")
print(lowest_mean)
