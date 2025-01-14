import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
data_1 = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')
data_2 = pd.read_csv('Unemployment_in_India.csv')

# Strip whitespace from column names and values
data_1.columns = data_1.columns.str.strip()
data_2.columns = data_2.columns.str.strip()
data_1['Date'] = data_1['Date'].str.strip()
data_2['Date'] = data_2['Date'].str.strip()

# Convert Date columns to datetime format
data_1['Date'] = pd.to_datetime(data_1['Date'], format='%d-%m-%Y')
data_2['Date'] = pd.to_datetime(data_2['Date'], format='%d-%m-%Y')

# Check for missing values
print("\nMissing values in Dataset 1:")
print(data_1.isnull().sum())
print("\nMissing values in Dataset 2:")
print(data_2.isnull().sum())

# Fill or drop missing values (example: forward fill)
data_1.ffill(inplace=True)
data_2.ffill(inplace=True)

# Merge datasets on common columns (if needed)
data_combined = pd.merge(data_1, data_2, on=['Region', 'Date'], suffixes=('_1', '_2'), how='outer')

# Exploratory Data Analysis
# 1. Trend of unemployment rate over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_1, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title('Trend of Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend(loc='upper right')
plt.savefig('trend_of_unemployment_rate.png')
plt.show()

# 2. Average unemployment rate by region
avg_unemployment_by_region = data_1.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_unemployment_by_region.plot(kind='bar', color='skyblue')
plt.title('Average Unemployment Rate by Region')
plt.xlabel('Region')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.savefig('average_unemployment_by_region.png')
plt.show()

# 3. Comparison of rural and urban unemployment rates (Dataset 2)
rural_urban_comparison = data_2.groupby('Area')['Estimated Unemployment Rate (%)'].mean()
plt.figure(figsize=(8, 6))
rural_urban_comparison.plot(kind='bar', color=['green', 'orange'])
plt.title('Rural vs Urban Unemployment Rates')
plt.xlabel('Area')
plt.ylabel('Average Unemployment Rate (%)')
plt.savefig('rural_vs_urban_unemployment_rates.png')
plt.show()

# Save combined dataset for further use
data_combined.to_csv('Combined_Unemployment_Data.csv', index=False)

print("Analysis complete. Combined dataset saved as 'Combined_Unemployment_Data.csv'.")
