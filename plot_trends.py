import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv(r'E:\Assignments\CMSC\Final Project\AAPL_stock_data.csv')

# Check data
print(data.head())  # Check the first few rows
print(data[['Date', 'Close']].head(40))  # Check relevant columns

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Handle any invalid date format

# Compute moving averages (e.g., 30-day and 100-day)
data['5_day_MA'] = data['Close'].rolling(window=5).mean()  # Try a smaller window for testing
data['30_day_MA'] = data['Close'].rolling(window=30).mean()
data['100_day_MA'] = data['Close'].rolling(window=100).mean()

# Handle NaN values (fill or drop)
data['5_day_MA'] = data['5_day_MA'].fillna(method='bfill')  # Backfill NaN values
data['30_day_MA'] = data['30_day_MA'].fillna(method='bfill')  # Backfill NaN values
data['100_day_MA'] = data['100_day_MA'].fillna(method='bfill')  # Backfill NaN values

# Plot stock price trend
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='AAPL Stock Price')
plt.title('AAPL Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('figures/stock_price_trend.png')
plt.close()

# Plot moving averages (5-day, 30-day, and 100-day)
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['5_day_MA'], label='5-Day Moving Average')
plt.plot(data['Date'], data['30_day_MA'], label='30-Day Moving Average')
plt.plot(data['Date'], data['100_day_MA'], label='100-Day Moving Average')
plt.title('AAPL Stock Price Moving Averages')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('figures/moving_averages.png')
plt.close()

print("Plots generated and saved.")
