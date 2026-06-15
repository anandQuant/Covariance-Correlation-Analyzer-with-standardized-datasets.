# Covariance-Correlation-Analyzer-with-standardized-datasets.
A lightweight, production-ready Python tool to fetch historical market data (Stocks, Crypto, Forex pairs) from Yahoo Finance, apply data standardization (Z-score normalization), and generate side-by-side visual heatmaps for Covariance and Correlation matrices.  more in read me section.


# Financial Asset Covariance & Correlation Analyzer

This tool evaluates asset relationships based on **daily percentage returns** rather than raw prices, eliminating time-trend biases and giving you an accurate mathematical look at how assets move together.

---

## 🚀 Features

* **Live Data Fetching:** Seamlessly pulls data from the Yahoo Finance API (`yfinance`) for any stock ticker or FX pair (e.g., `EURUSD=X`).
* **Automatic Adjustments Handle:** Built to work with the latest `yfinance` data structures (using the updated `"Close"` multi-index format).
* **Z-Score Standardization:** Automatically scales data to a mean of 0 and standard deviation of 1 before matrix calculations.
* **Seaborn Visualizations:** Generates clean, publication-grade, side-by-side heatmaps to quickly spot asset trends and portfolio diversification opportunities.

---

## 🛠️ Installation

Ensure you have Python 3.8+ installed. You can install the required data science and visualization dependencies using `pip`:

```bash
pip install yfinance pandas matplotlib seaborn
