import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yfinance as yf

# 1. Define the tickers (using FX pairs as an example, but works for stocks too)
tickers = ["EURUSD=X", "GBPUSD=X", "JPY=X", "AUDUSD=X", "CAD=X"]

# Manually set fixed dates here:
start_date = "2022-01-01"
end_date = "2026-04-31"

print(f"Fetching data from {start_date} to {end_date}...")

# Fetching data for the past year
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=365)



# 2. Download historical price data from Yahoo Finance
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# 3. Calculate Daily Percentage Returns
returns = data.pct_change().dropna()

# 4. STANDARDIZE THE DATASET (Z-score normalization)
# Formula applied to each column: (Value - Mean) / Standard Deviation
# This centers the data around 0 and scales it so the standard deviation is 1.
standardized_returns = (returns - returns.mean()) / returns.std()

# 5. Compute Covariance and Correlation Matrices of the STANDARDIZED data
# Notice how these two matrices will now output the exact same values!
covariance_matrix = standardized_returns.cov()
correlation_matrix = standardized_returns.corr()

# 6. Visualizing the Data using Seaborn Heatmaps
plt.figure(figsize=(14, 6))

# --- Plot 1: Covariance Matrix (Standardized Data) ---
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
sns.heatmap(
    covariance_matrix,
    annot=True,
    fmt=".2f",  # Changed to .2f because values are now scaled between -1 and 1
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    cbar=True,
)
plt.title(
    "Covariance Matrix\n(Standardized Returns)", fontsize=12, fontweight="bold"
)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# --- Plot 2: Correlation Matrix (Standardized Data) ---
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    cbar=True,
)
plt.title(
    "Correlation Matrix\n(Standardized Returns)", fontsize=12, fontweight="bold"
)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Adjust layout so labels don't overlap and show the plots
plt.tight_layout()
plt.show()

# 7. Print the matrices directly to the console to inspect the raw numbers
print("\n--- Covariance Matrix (Standardized) ---")
print(covariance_matrix)
print("\n--- Correlation Matrix (Standardized) ---")
print(correlation_matrix)
