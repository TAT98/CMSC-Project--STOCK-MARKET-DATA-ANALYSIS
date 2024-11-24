import pytest
import pandas as pd
import numpy as np
from analyze_extremes import extreme_up_days, extreme_down_days



def test_extreme_values():
    # Test with a larger dataset of 100 data points for more meaningful extremes
    dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
    prices = np.linspace(100, 500, 100) + np.random.randn(100) * 50  # Simulating stock prices

    data = pd.DataFrame({'Date': dates, 'Close': prices})
    
    # Using percentiles to determine extreme values (e.g., 95th and 5th percentiles)
    extreme_up = data['Close'].quantile(0.95)
    extreme_down = data['Close'].quantile(0.05)

    print(f"Extreme up threshold (95th percentile): {extreme_up}")
    print(f"Extreme down threshold (5th percentile): {extreme_down}")

    # Identify the extreme days based on the defined thresholds
    up_days = data[data['Close'] > extreme_up]
    down_days = data[data['Close'] < extreme_down]

    # Print the number of extreme up and down days
    print(f"Extreme Up Days: {len(up_days)}")
    print(f"Extreme Down Days: {len(down_days)}")

    # Assert that there are extreme days
    assert len(up_days) > 0  # There should be at least one extreme up day
    assert len(down_days) > 0  # There should be at least one extreme down day



def test_moving_average():
    # Expanded data to support moving averages
    dates = pd.date_range(start='2024-01-01', periods=120, freq='D')
    prices = [i + (i % 10) * 10 for i in range(120)]  # Generate diverse values

    data = pd.DataFrame({'Date': dates, 'Close': prices})
    data['30_day_MA'] = data['Close'].rolling(window=30).mean()
    data['100_day_MA'] = data['Close'].rolling(window=100).mean()

    print(data[['Date', 'Close', '30_day_MA', '100_day_MA']].tail(10))  # Check last few rows

    # Ensure moving averages have valid values
    assert not data['30_day_MA'].isna().all()  # At least one non-NaN value
    assert not data['100_day_MA'].isna().all()  # At least one non-NaN value


if __name__ == "__main__":
    pytest.main()
