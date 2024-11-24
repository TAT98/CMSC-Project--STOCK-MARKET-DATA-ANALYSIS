import pytest
import pandas as pd
import numpy as np

def test_extreme_values():
    # Test extreme up and down days
    data = pd.DataFrame({
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'Close': [100, 150, 200]
    })
    
    mean_price = data['Close'].mean()
    std_price = data['Close'].std()
    
    extreme_up = mean_price + 2 * std_price
    extreme_down = mean_price - 2 * std_price
    
    up_days = data[data['Close'] > extreme_up]
    down_days = data[data['Close'] < extreme_down]
    
    assert len(up_days) == 1  # One extreme up day
    assert len(down_days) == 0  # No extreme down days

def test_moving_average():
    # Test 30-day and 100-day moving average calculations
    data = pd.DataFrame({
        'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'Close': [100, 150, 200]
    })
    data['30_day_MA'] = data['Close'].rolling(window=30).mean()
    data['100_day_MA'] = data['Close'].rolling(window=100).mean()
    
    # Ensure that moving averages are calculated
    assert not data['30_day_MA'].isna().any()
    assert not data['100_day_MA'].isna().any()

if __name__ == "__main__":
    pytest.main()
