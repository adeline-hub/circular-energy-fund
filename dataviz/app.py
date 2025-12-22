import os
import pandas as pd
import streamlit as st
import plotly.express as px
from style.dubois_theme import DUBOIS_THEME, FONT_FAMILY

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

energy = pd.read_csv(
    os.path.join(BASE_DIR, "data/energy.csv"),
    encoding="latin-1"
)

finance = pd.read_csv(
    os.path.join(BASE_DIR, "data/finance.csv"),
    encoding="latin-1"
)

finance.columns = finance.columns.str.replace("ï»¿", "").str.strip()

st.markdown(
    "<h1 style='text-align:center;'>100 famiglie, un impianto solare</h1>",
    unsafe_allow_html=True
)

# --- KPI ---
col1, col2, col3 = st.columns(3)
col1.metric("Produzione annua", "300.000 kWh")
col2.metric("Autoconsumo", "75%")
col3.metric("Famiglie servite", "100")

# --- Energia ---
energy_plot = energy[
    energy["metric"].isin(["self_consumed_energy", "shared_energy"])
]

fig_energy = px.bar(
    energy_plot,
    x="metric",
    y="value",
    color="metric",
    title="Energia prodotta e utilizzata",
    color_discrete_map={
        "self_consumed_energy": DUBOIS_THEME["primary"],
        "shared_energy": DUBOIS_THEME["secondary"]
    }
)

fig_energy.update_layout(
    plot_bgcolor=DUBOIS_THEME["background"],
    font_family=FONT_FAMILY,
    showlegend=False
)

st.plotly_chart(fig_energy, use_container_width=True)

# --- Cashflow ---
fig_cash = px.line(
    finance,
    x="year",
    y="cumulative_cashflow",
    title="Cashflow cumulato nel tempo",
    markers=True
)

fig_cash.update_layout(
    plot_bgcolor=DUBOIS_THEME["background"],
    font_family=FONT_FAMILY
)

st.plotly_chart(fig_cash, use_container_width=True)