[![CPZ Lab](https://drive.google.com/uc?id=1CqcRie0ztUhrCnmv5cqfNHgM3FIK4sFE)](https://ai.cpz-lab.com/)

# COCA COLA PRICE — Factor‑Based Trading Strategy

[![GitHub Stars](https://img.shields.io/github/stars/chris-cpz/strategy-coca-cola-price?style=flat-square)](https://github.com/chris-cpz/strategy-coca-cola-price)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square\&logo=python)](https://www.python.org/downloads/)
![Status](https://img.shields.io/badge/status-development-orange?style=flat-square)

> **Description :** Systematic, multi‑factor strategy trading The Coca‑Cola Company (KO) equity using empirically validated return anomalies.

---

## Table of Contents

1. [Quick Synopsis](#1-quick-synopsis)
2. [Repository Map](#2-repository-map)
3. [Getting Started](#3-getting-started)
4. [Research Rationale](#4-research-rationale)
5. [Back‑Testing & Validation](#5-back-testing--validation)
6. [Risk Management](#6-risk-management)
7. [Technology Stack](#7-technology-stack)
8. [Monitoring & Governance](#8-monitoring--governance)
9. [Change Log](#9-change-log)
10. [Contributing](#10-contributing)
11. [License](#11-license)
12. [Disclaimer](#12-disclaimer)

---

## 1. Quick Synopsis

| Item                    | Detail                                                |
| ----------------------- | ----------------------------------------------------- |
| **Strategy Type**       | Multi‑factor (value, momentum, quality) equity timing |
| **Implementation Date** | 2025‑06‑25                                            |
| **Universe**            | KO (primary) + SPY & QQQ for regime context           |
| **Objective**           | Sharpe > 1.5 and max drawdown < 15 % vs buy‑and‑hold  |

---

## 2. Repository Map

```
.
├── data/               # Raw & processed market data
├── strategy/           # Core logic (signals, portfolio, execution)
├── notebooks/          # Research & exploratory analysis
├── reports/            # Auto‑generated performance reports
├── tests/              # Unit / integration tests
└── requirements.txt
```

---

## 3. Getting Started

### 3.1 Environment

| Component | Recommended             |
| --------- | ----------------------- |
| Python    | 3.8 or newer            |
| RAM       | ≥ 16 GB                 |
| OS        | macOS / Linux / Windows |

### 3.2 Installation

```bash
git clone https://github.com/chris-cpz/strategy-coca-cola-price.git
cd strategy-coca-cola-price
python -m venv venv && source venv/bin/activate   # Windows → venv\Scripts\activate
pip install -r requirements.txt
```

### 3.3 Configuration

Create a `.env` file in the project root:

```env
ALPHA_VANTAGE_API_KEY=...
IEX_CLOUD_API_KEY=...
QUANDL_API_KEY=...
```

### 3.4 Run a Back‑Test

```python
from strategy import CocaColaPriceStrategy

strat   = CocaColaPriceStrategy()
data    = strat.load_data(['KO', 'SPY', 'QQQ'], '2010-01-01', '2025-06-01')
results = strat.backtest(data)
strat.generate_report(results)  # HTML under reports/
```

---

## 4. Research Rationale

1. **Factor Premia** – Value, momentum & quality factors exhibit persistent excess returns (Fama‑French 2012; Asness et al. 2013).
2. **Behavioural Biases** – Investor over‑/under‑reaction drives mean‑reversion and trend following (Jegadeesh & Titman 1993).
3. **Single‑Name Focus** – Narrow universe enables micro‑structure edge and minimal data latency.

---

## 5. Back‑Testing & Validation

| Stage                 | Settings                                      |
| --------------------- | --------------------------------------------- |
| Historical Simulation | Daily bars 2005‑2025                          |
| Walk‑Forward          | 12 m optimisation / 6 m hold‑out              |
| Monte‑Carlo           | 10 000 paths, stationary bootstrap            |
| Stress Tests          | 2008 GFC, 2020 COVID‑19, 2022 inflation shock |
| Transaction Costs     | Bid‑ask, slippage, IBKR commissions           |

**Target Metrics**

| Metric            | Goal         |
| ----------------- | ------------ |
| Annualised Sharpe | > 1.5        |
| Max Drawdown      | < 15 %       |
| Volatility        | 12–18 % p.a. |
| Turnover          | < 150 % p.a. |

---

## 6. Risk Management

* **Position Sizing** – Volatility‑scaled, max 5 % capital per leg
* **Stop‑Loss** – 5 % trailing on open P\&L
* **Exposure Limits** – Sector ≤ 25 %, beta‑adjusted gross < 120 %
* **Model Risk** – Parameter stability checks & break‑point detection
* **Operational Risk** – Heart‑beat watchdog & order acknowledgment checks

---

## 7. Technology Stack

| Layer        | Tools                                         |
| ------------ | --------------------------------------------- |
| Data Ingest  | `pandas`, `yfinance`, custom adapters         |
| Alpha Engine | `numpy`, `scikit‑learn`                       |
| Back‑Test    | `zipline‑reloaded`, `pyfolio`                 |
| Execution    | Interactive Brokers API (`ib‑insync`)         |
| Reporting    | `plotly`, `matplotlib`, Jinja2 HTML templates |
| CI/CD        | `pytest`, GitHub Actions                      |

---

## 8. Monitoring & Governance

| Frequency   | Checks                                                   |
| ----------- | -------------------------------------------------------- |
| **Daily**   | Data integrity, signal sanity, order fill reconciliation |
| **Monthly** | Performance vs benchmark, risk metrics, drift detection  |
| **Annual**  | Model refit, parameter review, documentation audit       |

Exception handling follows a three‑tier escalation policy (automated alert → manual review → trading halt).

---

## 9. Change Log

| Version | Date       | Notes                                |
| ------- | ---------- | ------------------------------------ |
| 1.0.0   | 2025‑06‑25 | Initial public release               |
| 1.1.0   | 2025‑06‑29 | README overhaul & governance section |

---

## 10. Contributing

Pull requests are welcome — please review `CONTRIBUTING.md` and open an issue before major changes.

---

## 11. License

Distributed under the MIT License. See `LICENSE` for full text.

---

## 12. Disclaimer

*For educational and research purposes only.* Nothing herein constitutes investment advice. Trading involves risk of loss.

---

<p align="center"><sub>Built with ❤️ by CPZ Lab  •  Last updated 2025‑06‑29</sub></p>
