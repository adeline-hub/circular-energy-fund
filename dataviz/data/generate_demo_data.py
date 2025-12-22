import pandas as pd
import numpy as np
from pathlib import Path

# =========================
# PATH SETUP (IMPORTANT)
# =========================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR

np.random.seed(42)

# =========================
# 1. ENERGY PRODUCTION
# =========================
dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")

base_production = 300_000 / len(dates)
seasonality = 1 + 0.6 * np.sin(2 * np.pi * (dates.dayofyear - 80) / 365)
noise = np.random.normal(0, 0.08, len(dates))

production_kwh = base_production * seasonality * (1 + noise)
production_kwh = np.clip(production_kwh, 200, None)

energy_production = pd.DataFrame({
    "date": dates,
    "production_kwh": production_kwh.round(0)
})

energy_production.to_excel(DATA_DIR / "energy_production.xlsx", index=False)

# =========================
# 2. ENERGY CONSUMPTION
# =========================
total_consumption = production_kwh * np.random.uniform(1.1, 1.3, len(dates))
self_consumed = np.minimum(
    production_kwh,
    total_consumption * np.random.uniform(0.7, 0.75, len(dates))
)

energy_consumption = pd.DataFrame({
    "date": dates,
    "total_consumption_kwh": total_consumption.round(0),
    "self_consumed_kwh": self_consumed.round(0),
    "grid_import_kwh": (total_consumption - self_consumed).round(0)
})

energy_consumption.to_excel(DATA_DIR / "energy_consumption.xlsx", index=False)

# =========================
# 3. MEMBERS
# =========================
n_members = 100

members = pd.DataFrame({
    "member_id": [f"M{i:03d}" for i in range(1, n_members + 1)],
    "investment_eur": np.random.choice([3000, 4000, 5000, 6000], n_members),
    "annual_consumption_kwh": np.random.normal(2700, 400, n_members).round(0)
})

members["energy_share_kwh"] = (members["annual_consumption_kwh"] * 0.75).round(0)
members["annual_savings_eur"] = (members["energy_share_kwh"] * 0.14).round(0)

members.to_excel(DATA_DIR / "members.xlsx", index=False)

# =========================
# 4. CASHFLOW
# =========================
years = list(range(2024, 2035))

cash_in = [42000] + list(np.linspace(38000, 47000, len(years) - 1))
cash_out = [-180000] + [-8000 - i * 300 for i in range(len(years) - 1)]

net_cashflow = np.array(cash_in) + np.array(cash_out)
cumulative_cashflow = np.cumsum(net_cashflow)

cashflow = pd.DataFrame({
    "year": years,
    "cash_in": cash_in,
    "cash_out": cash_out,
    "net_cashflow": net_cashflow,
    "cumulative_cashflow": cumulative_cashflow
})

cashflow.to_excel(DATA_DIR / "cashflow.xlsx", index=False)

# =========================
# 5. MARKET PRICES
# =========================
market_prices = pd.DataFrame({
    "year": [2020, 2021, 2022, 2023, 2024],
    "italy_price_eur_kwh": [0.22, 0.24, 0.30, 0.28, 0.26],
    "eu_avg_price_eur_kwh": [0.20, 0.21, 0.25, 0.23, 0.22],
    "cef_member_price": [0.14] * 5
})

market_prices.to_excel(DATA_DIR / "market_prices_it_eu.xlsx", index=False)

print("✅ Dataset creati correttamente nella cartella data/")