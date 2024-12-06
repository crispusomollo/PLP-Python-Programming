# Step 1: Import the pandas library
import pandas as pd

# Step 2: Load the dataset
file_path = 'dataset.csv'  # Replace with your dataset path
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
    exit()

# Step 3: Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Step 4: Explore the structure of the dataset
print("\nDataset information:")
print(data.info())

# Check for missing values in the dataset
print("\nMissing values in each column:")
print(data.isnull().sum())

# Step 5: Clean the dataset (e.g., fill missing values with the mean)
# Option 1: Fill missing values with the mean for numerical columns
data = data.fillna(data.mean())

# Option 2: Drop rows with any missing values
# data = data.dropna()

# Verify that missing values have been handled
print("\nMissing values after cleaning:")
print(data.isnull().sum())

