import pandas as pd

# Load the CSV file
file_path = "C:/Users/DELL/Desktop/ai/projecti/supermarket_sales - Sheet1.csv"
data = pd.read_csv(file_path)

# Print the first few rows of the data
print(data.head())

# Check for missing values
missing_values = data.isnull().sum()

# Print missing values
print("Missing Values:\n", missing_values)

# Check current data types
print("Current Data Types:\n", data.dtypes)

# Convert 'Quantity' to integer
data['Quantity'] = data['Quantity'].astype(int)

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Convert 'Customer type' to category
data['Customer type'] = data['Customer type'].astype('category')

# Check updated data types
print("Updated Data Types:\n", data.dtypes)

# Summary statistics
summary_stats = data.describe(include='all')
print("Summary Statistics:\n", summary_stats)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your dataset
file_path = "C:/Users/DELL/Desktop/ai/projecti/supermarket_sales - Sheet1.csv"
data = pd.read_csv(file_path)

# Distribution of numerical features
numerical_features = data.select_dtypes(include=['float64', 'int64'])

# Calculate the number of subplots needed based on the number of numerical columns
num_plots = min(len(numerical_features.columns), 6)  # Maximum 6 subplots

# Set up the layout for subplots
num_rows = 2
num_cols = 3

plt.figure(figsize=(15, 10))
for i, column in enumerate(numerical_features.columns, 1):
    if i <= num_plots:
        plt.subplot(num_rows, num_cols, i)
        sns.histplot(data[column], kde=True)
        plt.title(column)
        plt.tight_layout()

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math

# Load your dataset
file_path = "C:/Users/DELL/Desktop/ai/projecti/supermarket_sales - Sheet1.csv"
data = pd.read_csv(file_path)

# Count of categorical features
categorical_features = data.select_dtypes(include=['object', 'category'])

# Calculate the number of subplots needed based on the number of categorical columns
num_plots = len(categorical_features.columns)

# Determine the number of rows and columns for subplots
num_cols = 3
num_rows = math.ceil(num_plots / num_cols)

plt.figure(figsize=(15, 5 * num_rows))
for i, column in enumerate(categorical_features.columns, 1):
    plt.subplot(num_rows, num_cols, i)
    sns.countplot(data[column])
    plt.title(column)
    plt.xticks(rotation=45)
    plt.tight_layout()

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your dataset
file_path = "C:/Users/DELL/Desktop/ai/projecti/supermarket_sales - Sheet1.csv"
data = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Aggregate sales over time (daily)
daily_sales = data.groupby('Date')['Total'].sum().reset_index()

# Plotting sales over time
plt.figure(figsize=(14, 6))
sns.lineplot(x='Date', y='Total', data=daily_sales)
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

# Sales distribution by product line
plt.figure(figsize=(12, 6))
sns.boxplot(x='Product line', y='Total', data=data)
plt.title('Sales Distribution by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Customer demographics analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
file_path = r"C:\Users\DELL\Desktop\ai\projecti\supermarket_sales - Sheet1.csv"
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and calculate total sales
daily_sales = df.groupby('Date')['Total'].sum()

# Plotting sales over time
plt.figure(figsize=(14, 6))
sns.lineplot(x=daily_sales.index, y=daily_sales.values, marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Plotting sales distribution by product line
plt.figure(figsize=(12, 6))
sns.boxplot(x='Product line', y='Total', data=df, palette='Set2')
plt.title('Sales Distribution by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Customer demographics analysis
plt.figure(figsize=(16, 10))

# Gender distribution
plt.subplot(2, 2, 1)
sns.countplot(x='Gender', data=df, palette='Set1')
plt.title('Gender Distribution')

# Customer type distribution
plt.subplot(2, 2, 2)
sns.countplot(x='Customer type', data=df, palette='Set1')
plt.title('Customer Type Distribution')

# Branch distribution
plt.subplot(2, 2, 3)
sns.countplot(x='Branch', data=df, palette='Set1')
plt.title('Branch Distribution')

# Payment method distribution
plt.subplot(2, 2, 4)
sns.countplot(x='Payment', data=df, palette='Set1')
plt.title('Payment Method Distribution')

plt.tight_layout()
plt.show()


