#!/usr/bin/env python3
"""
coca cola price - Factor_based Trading Strategy

Strategy Type: factor_based
Description: coca cola price
Created: 2025-06-25T00:35:56.345Z

WARNING: This is a template implementation. Thoroughly backtest before live trading.
"""

import os
import sys
import logging
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('strategy.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class cocacolapriceStrategy:
    """
    coca cola price Implementation
    
    Strategy Type: factor_based
    Risk Level: Monitor drawdowns and position sizes carefully
    """
    
    def __init__(self, config=None):
        self.config = config or self.get_default_config()
        self.positions = {}
        self.performance_metrics = {}
        logger.info(f"Initialized coca cola price strategy")
        
    def get_default_config(self):
        """Default configuration parameters"""
        return {
            'max_position_size': 0.05,  # 5% max position size
            'stop_loss_pct': 0.05,      # 5% stop loss
            'lookback_period': 20,       # 20-day lookback
            'rebalance_freq': 'daily',   # Rebalancing frequency
            'transaction_costs': 0.001,  # 0.1% transaction costs
        }
    
    def load_data(self, symbols, start_date, end_date):
        """Load market data for analysis"""
        try:
            import yfinance as yf
            data = yf.download(symbols, start=start_date, end=end_date)
            logger.info(f"Loaded data for {len(symbols)} symbols")
            return data
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return None

# =============================================================================
# USER'S STRATEGY IMPLEMENTATION
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# Strategy class definition
class CocaColaPriceStrategy:
    def __init__(self, data, short_window=20, long_window=50, risk_per_trade=0.01, initial_capital=100000):
        # Initialize parameters
        self.data = data.copy()
        self.short_window = short_window
        self.long_window = long_window
        self.risk_per_trade = risk_per_trade
        self.initial_capital = initial_capital
        self.signals = pd.DataFrame(index=self.data.index)
        self.positions = pd.DataFrame(index=self.data.index)
        self.results = None

    def generate_signals(self):
        # Generate factor-based signals using moving average crossover
        self.signals['price'] = self.data['Close']
        self.signals['short_ma'] = self.data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        self.signals['long_ma'] = self.data['Close'].rolling(window=self.long_window, min_periods=1).mean()
        self.signals['signal'] = 0
        self.signals['signal'][self.short_window:] = np.where(
            self.signals['short_ma'][self.short_window:] > self.signals['long_ma'][self.short_window:], 1, -1
        )
        self.signals['positions'] = self.signals['signal'].diff()
        logging.info("Signals generated.")

    def position_sizing(self):
        # Calculate position size based on risk per trade and ATR
        self.signals['ATR'] = self.data['High'].rolling(window=14).max() - self.data['Low'].rolling(window=14).min()
        self.signals['ATR'].fillna(method='bfill', inplace=True)
        self.signals['position_size'] = (self.initial_capital * self.risk_per_trade) / (self.signals['ATR'] + 1e-6)
        self.signals['position_size'] = self.signals['position_size'].astype(int)
        logging.info("Position sizing calculated.")

    def backtest(self):
        # Backtest the strategy
        self.positions['position'] = self.signals['signal'].shift(1).fillna(0)
        self.positions['position_size'] = self.signals['position_size'].shift(1).fillna(0)
        self.positions['holdings'] = self.positions['position'] * self.positions['position_size'] * self.data['Close']
        self.positions['cash'] = self.initial_capital - (self.positions['position_size'] * self.data['Close'] * self.positions['position']).cumsum()
        self.positions['total'] = self.positions['cash'] + self.positions['holdings']
        self.positions['returns'] = self.positions['total'].pct_change().fillna(0)
        self.results = self.positions
        logging.info("Backtest completed.")

    def calculate_performance(self):
        # Calculate performance metrics
        if self.results is None:
            logging.error("No results to calculate performance.")
            return None
        returns = self.results['returns']
        sharpe_ratio = np.sqrt(252) * returns.mean() / (returns.std() + 1e-6)
        cumulative_returns = (1 + returns).cumprod()
        rolling_max = cumulative_returns.cummax()
        drawdown = (cumulative_returns - rolling_max) / rolling_max
        max_drawdown = drawdown.min()
        total_return = cumulative_returns.iloc[-1] - 1
        performance = {
            'Sharpe Ratio': sharpe_ratio,
            'Max Drawdown': max_drawdown,
            'Total Return': total_return
        }
        logging.info("Performance calculated.")
        return performance

    def plot_results(self):
        # Plot the strategy results
        plt.figure(figsize=(12,6))
        plt.plot(self.results['total'], label='Portfolio Value')
        plt.title('Coca Cola Price Strategy Portfolio Value')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.show()

# Sample data generation for demonstration
def generate_sample_data(num_days=252):
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=num_days, freq='B')
    price = 60 + np.cumsum(np.random.normal(0, 1, num_days))
    high = price + np.random.uniform(0.5, 1.5, num_days)
    low = price - np.random.uniform(0.5, 1.5, num_days)
    open_ = price + np.random.uniform(-0.5, 0.5, num_days)
    close = price + np.random.uniform(-0.5, 0.5, num_days)
    volume = np.random.randint(1000000, 5000000, num_days)
    data = pd.DataFrame({
        'Open': open_,
        'High': high,
        'Low': low,
        'Close': close,
        'Volume': volume
    }, index=dates)
    return data

# Main execution block
if __name__ == "__main__":
    # Generate sample data
    data = generate_sample_data()
    # Initialize strategy
    strategy = CocaColaPriceStrategy(data)
    try:
        # Generate signals
        strategy.generate_signals()
        # Position sizing
        strategy.position_sizing()
        # Backtest
        strategy.backtest()
        # Performance metrics
        performance = strategy.calculate_performance()
        print("Performance Metrics:")
        for k, v in performance.items():
            print("%s: %s" % (k, v))
        # Plot results
        strategy.plot_results()
    except Exception as e:
        logging.error("Error running strategy: %s" % str(e))

# =============================================================================
# STRATEGY EXECUTION AND TESTING
# =============================================================================

if __name__ == "__main__":
    # Example usage and testing
    strategy = cocacolapriceStrategy()
    print(f"Strategy '{strategyName}' initialized successfully!")
    
    # Example data loading
    symbols = ['SPY', 'QQQ', 'IWM']
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    
    print(f"Loading data for symbols: {symbols}")
    data = strategy.load_data(symbols, start_date, end_date)
    
    if data is not None:
        print(f"Data loaded successfully. Shape: {data.shape}")
        print("Strategy ready for backtesting!")
    else:
        print("Failed to load data. Check your internet connection.")
