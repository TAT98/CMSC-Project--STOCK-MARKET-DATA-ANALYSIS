import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv(r'E:\Assignments\CMSC\Final Project\AAPL_stock_data.csv')

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

# Compute moving averages (e.g., 30-day and 100-day)
data['30_day_MA'] = data['Close'].rolling(window=30).mean()
data['100_day_MA'] = data['Close'].rolling(window=100).mean()

# Plot moving averages
plt.figure(figsize=(10, 6))
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
