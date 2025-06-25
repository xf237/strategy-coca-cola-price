# COCA COLA PRICE

## Factor-Based Systematic Trading Strategy

[![GitHub Stars](https://img.shields.io/github/stars/chris-cpz/strategy-coca-cola-price?style=for-the-badge&logo=github)](https://github.com/chris-cpz/strategy-coca-cola-price)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/downloads/)

---

## Abstract

This repository implements a systematic factor-based trading strategy grounded in quantitative finance research, exploiting empirically identified market inefficiencies to achieve superior risk-adjusted returns compared to passive benchmarks.

---

## Research Hypothesis

**Hypothesis (H₀)**: Factor-based signals provide no statistically significant outperformance relative to market benchmarks.  
**Alternative Hypothesis (H₁)**: Factor-based signals generate statistically significant positive alpha.

---

## Methodology

### Strategy Development

- Define clear economic rationale for chosen factors  
- Generate quantitative signals using statistical and machine-learning models  
- Employ robust backtesting, walk-forward analysis, and stress testing  
- Incorporate transaction costs and realistic execution assumptions

### Performance Validation

- Historical data validation (minimum 10 years)  
- Walk-forward and cross-validation procedures  
- Statistical hypothesis testing (e.g., Sharpe ratio significance)

---

## Key Strategy Components

| Component               | Details                                |
|-------------------------|----------------------------------------|
| Strategy Type           | Factor-Based                           |
| Rebalancing Frequency   | Daily / Weekly                         |
| Risk Management         | Volatility targeting, position sizing  |
| Data Sources            | Real-time & historical data vendors    |
| Minimum Capital         | $100,000                               |

---

## Target Metrics

| Metric            | Objective              |
|-------------------|------------------------|
| Sharpe Ratio      | > 1.5 annualized       |
| Maximum Drawdown  | < 15%                  |
| Annual Volatility | 12–18%                 |

---

## Installation

```bash
# Clone repository
git clone https://github.com/chris-cpz/strategy-coca-cola-price.git
cd strategy-coca-cola-price

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## API Configuration

Create a `.env` file in the project root directory and add your API keys in the following format:

```env
ALPHA_VANTAGE_API_KEY=your_key_here
IEX_CLOUD_API_KEY=your_key_here
QUANDL_API_KEY=your_key_here
```

---

## Backtesting & Validation

- **Historical Analysis**: ≥ 10 years of data  
- **Walk-forward Testing**: 12-month calibration, 6-month validation  
- **Monte Carlo Simulations**: >10,000 iterations  
- **Stress Testing**: Extreme-scenario performance evaluation

---

## Risk Controls

- **Maximum position limit**: 5%  
- **Volatility-based position sizing**  
- **Predefined stop-loss thresholds**  
- **Sector concentration limits**

---

## Technology Stack

| Component   | Tools                    | Purpose                     |
|------------|---------------------------|-----------------------------|
| Data       | pandas, numpy             | Efficient data processing   |
| ML Models  | scikit-learn              | Signal generation           |
| Backtesting| zipline, pyfolio          | Backtesting & reporting     |
| Execution  | Interactive Brokers API   | Trading execution           |

---

## Limitations & Risks

- Potential overfitting to historical data  
- Sensitivity to model assumptions and parameters  
- Execution slippage and latency impacts  
- Market regime shifts affecting factor performance

---

## References

- Jegadeesh, N., & Titman, S. (1993). *Returns to Buying Winners and Selling Losers*. *Journal of Finance*.  
- Fama, E.F., & French, K.R. (2012). *Size, value, and momentum in international stock returns*. *Journal of Financial Economics*.  
- Asness, C.S., Moskowitz, T.J., & Pedersen, L.H. (2013). *Value and momentum everywhere*. *Journal of Finance*.

---

## Disclaimer

This strategy is for research purposes only. Past performance does not guarantee future results. Trading involves substantial risk of loss.

---

## Contribution Guidelines

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for details on submitting improvements.

---

## License

MIT License. See [`LICENSE`](LICENSE) for full terms.
