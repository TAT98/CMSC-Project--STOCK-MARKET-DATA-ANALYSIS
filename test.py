import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
data = pd.read_csv(r'E:\Assignments\CMSC\Final Project\AAPL_stock_data.csv')

# Ensure Date is in datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Sort by date
data = data.sort_values('Date').reset_index(drop=True)

# Handle missing values (e.g., fill or drop)
data['Close'] = data['Close'].fillna(method='ffill')

# Summary statistics
summary_stats = data['Close'].describe()
print("Summary Statistics:\n", summary_stats)


# Plot stock price trend
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='AAPL Stock Price', color='blue')
plt.title('AAPL Stock Price Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Stock Price ($)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('figures/stock_price_trend.png')
plt.show()


# Compute moving averages
data['30_day_MA'] = data['Close'].rolling(window=30).mean()
data['100_day_MA'] = data['Close'].rolling(window=100).mean()

# Plot moving averages
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Daily Closing Price', color='blue', alpha=0.6)
plt.plot(data['Date'], data['30_day_MA'], label='30-Day Moving Average', color='orange')
plt.plot(data['Date'], data['100_day_MA'], label='100-Day Moving Average', color='green')
plt.title('AAPL Stock Price Moving Averages', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Stock Price ($)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('figures/moving_averages.png')
plt.show()


# Calculate mean and standard deviation
mean_price = data['Close'].mean()
std_price = data['Close'].std()

# Define thresholds
extreme_up = mean_price + 2 * std_price
extreme_down = mean_price - 2 * std_price

# Identify extreme days
extreme_up_days = data[data['Close'] > extreme_up]
extreme_down_days = data[data['Close'] < extreme_down]

# Plot extreme price days
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data['Close'], bins=50, color='blue', alpha=0.7, label='Daily Close Price')
ax.axvline(extreme_up, color='red', linestyle='--', label='Extreme Up Threshold')
ax.axvline(extreme_down, color='green', linestyle='--', label='Extreme Down Threshold')
plt.title('Distribution of AAPL Stock Prices with Extreme Thresholds', fontsize=14)
plt.xlabel('Stock Price ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('figures/extreme_price_distribution.png')
plt.show()


# Extract year from the date
data['Year'] = data['Date'].dt.year

# Group by year and calculate volatility
yearly_volatility = data.groupby('Year')['Close'].std()

# Plot yearly volatility
plt.figure(figsize=(10, 6))
yearly_volatility.plot(kind='bar', color='purple', alpha=0.8)
plt.title('Yearly Volatility of AAPL Stock Prices', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Volatility (Standard Deviation)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('figures/yearly_volatility.png')
plt.show()


# Calculate daily returns
data['Daily_Returns'] = data['Close'].pct_change() * 100

# Plot histogram of returns
plt.figure(figsize=(10, 6))
plt.hist(data['Daily_Returns'].dropna(), bins=50, color='skyblue', alpha=0.8, edgecolor='black')
plt.title('Distribution of AAPL Daily Returns', fontsize=14)
plt.xlabel('Daily Returns (%)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('figures/daily_returns_distribution.png')
plt.show()
