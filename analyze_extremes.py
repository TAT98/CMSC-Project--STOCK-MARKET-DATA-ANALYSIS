import pandas as pd
import numpy as np


# Load cleaned data
data = pd.read_csv(r'E:\Assignments\CMSC\Final Project\AAPL_stock_data.csv')

# Compute statistics
mean_price = data['Close'].mean()
std_price = data['Close'].std()

# Define extreme values (e.g., 2 standard deviations above/below the mean)
extreme_up = mean_price + 2 * std_price
extreme_down = mean_price - 2 * std_price

# Identify days with extreme stock prices
extreme_up_days = data[data['Close'] > extreme_up]
extreme_down_days = data[data['Close'] < extreme_down]

print(f"Extreme Up Days: {len(extreme_up_days)}")
print(f"Extreme Down Days: {len(extreme_down_days)}")

# Save results
extreme_up_days.to_csv('figures/extreme_up_days.csv', index=False)
extreme_down_days.to_csv('figures/extreme_down_days.csv', index=False)

