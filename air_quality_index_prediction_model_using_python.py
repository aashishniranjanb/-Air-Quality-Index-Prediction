import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/content/432c92d7855c48075139.csv"
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

df.columns = df.columns.str.lower().str.replace(' ', '_')

pollutant_cols = ['pm2.5', 'pm10', 'no', 'no2', 'nox', 'nh3', 'co', 'so2', 'o3', 'benzene', 'toluene', 'xylene']
df[pollutant_cols] = df[pollutant_cols].fillna(df[pollutant_cols].median())

df = df.dropna(subset=['aqi', 'aqi_bucket'])
df = df.drop_duplicates()

# Distribution of AQI
plt.figure(figsize=(8, 6))
sns.histplot(df['aqi'], kde=True, bins=30, color='skyblue')
plt.title("Distribution of AQI")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.show()

# Correlation Heatmap of Pollutants and AQI
plt.figure(figsize=(12, 10))
corr = df[pollutant_cols + ['aqi']].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap of Pollutants and AQI")
plt.show()

# Time Series Plot of AQI for a Specific City
city = 'Ahmedabad'
df_city = df[df['city'].str.lower() == city.lower()].sort_values('date')
plt.figure(figsize=(20, 10))
plt.plot(df_city['date'], df_city['aqi'], marker='o', linestyle='-', color='green')
plt.title(f"Time Series of AQI in {city}")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

city = 'Bengaluru'
df_city = df[df['city'].str.lower() == city.lower()].sort_values('date')
plt.figure(figsize=(20, 10))
plt.plot(df_city['date'], df_city['aqi'], marker='o', linestyle='-', color='blue')
plt.title(f"Time Series of AQI in {city}")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

city = 'Delhi'
df_city = df[df['city'].str.lower() == city.lower()].sort_values('date')
plt.figure(figsize=(20, 10))
plt.plot(df_city['date'], df_city['aqi'], marker='o', linestyle='-', color='red')
plt.title(f"Time Series of AQI in {city}")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot: Distribution of Pollutant Values by AQI Bucket
plt.figure(figsize=(25, 18))
melted = pd.melt(df, id_vars=['aqi_bucket'], value_vars=pollutant_cols,
                 var_name='Pollutant', value_name='Value')
sns.boxplot(x='Pollutant', y='Value', hue='aqi_bucket', data=melted)
plt.title("Distribution of Pollutant Values by AQI Bucket")
plt.xlabel("Pollutant")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend(title='AQI Bucket', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
