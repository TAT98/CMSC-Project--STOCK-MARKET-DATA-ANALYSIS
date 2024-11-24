import pandas as pd

def analyze_extremes():
    # Updated dataset for analysis
    data = pd.DataFrame({
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
                                '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']),
        'Close': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    })
    
    # Calculate mean and standard deviation
    mean_price = data['Close'].mean()
    std_price = data['Close'].std()
    
    # Print mean and standard deviation for debugging
    print(f"Mean Price: {mean_price}")
    print(f"Standard Deviation: {std_price}")
    
    # Adjust thresholds (using 1.0 * std for more reasonable detection of extremes)
    extreme_up = mean_price + 1.0 * std_price
    extreme_down = mean_price - 1.0 * std_price
    
    # Print extreme thresholds for debugging
    print(f"Extreme Up Threshold: {extreme_up}")
    print(f"Extreme Down Threshold: {extreme_down}")
    
    # Detect extreme up and down days
    up_days = data[data['Close'] > extreme_up]
    down_days = data[data['Close'] < extreme_down]
    
    print(f"Extreme Up Days: {len(up_days)}")
    print(f"Extreme Down Days: {len(down_days)}")
    
    # Optionally save to CSV (ensure directory exists)
    up_days.to_csv('figures/extreme_up_days.csv', index=False)
    down_days.to_csv('figures/extreme_down_days.csv', index=False)

# Run the analysis
analyze_extremes()
