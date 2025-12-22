import os
from style.dubois_theme import DUBOIS_THEME, FONT_FAMILY
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import streamlit.components.v1 as components
import tempfile

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Circular Energy Fund – Dashboard Cliente",
    layout="wide"
)

from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent / "assets"

# =========================
# PATHS (SAFE FOR LOCAL + RENDER)
# =========================
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# =========================
# LOAD DATA
# =========================
energy = pd.read_excel(DATA_DIR / "energy_production.xlsx", parse_dates=["date"])
consumption = pd.read_excel(DATA_DIR / "energy_consumption.xlsx", parse_dates=["date"])
members = pd.read_excel(DATA_DIR / "members.xlsx")
cashflow = pd.read_excel(DATA_DIR / "cashflow.xlsx")
market = pd.read_excel(DATA_DIR / "market_prices_it_eu.xlsx")




# clean columns (safety)
for df in [energy, consumption, members, cashflow, market]:
    df.columns = df.columns.str.strip()

col_logo, col_text = st.columns([1, 4])

with col_logo:
    st.image(
        str(ASSETS_DIR / "logo.png"),
        use_column_width=True
    )

with col_text:
    st.markdown("""
### Obiettivo del Progetto

Il **Circular Energy Fund** nasce con l’obiettivo di creare un **veicolo di investimento partecipativo**
che consenta a una comunità di circa **100 soci** di investire collettivamente nella realizzazione
di un **impianto fotovoltaico sostenibile in Sicilia**.

Il progetto è concepito per:
- produrre energia rinnovabile senza sottrarre terreno all’agricoltura  
- favorire l’utilizzo di **materiali e fornitori locali**  
- garantire **trasparenza, tracciabilità e governance condivisa**

I benefici economici ed energetici rimangono all’interno della comunità dei soci,
che possono usufruire di **energia elettrica a prezzo agevolato**
e di **rendimenti indiretti nel lungo periodo**.
""")

st.divider()

# =========================
# META BLOCK – 6 COLUMNS
# =========================
components.html(
"""
<style>
.meta-container {
    background-color: #f4f6f8;
    padding: 24px 32px;
    border-radius: 8px;
    margin-bottom: 32px;
    font-family: sans-serif;
}

.meta-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 32px;
}

.meta-item {
    font-size: 0.9em;
    line-height: 1.6;
    color: #111;
}

.meta-item b {
    display: block;
    letter-spacing: 0.12em;
    font-size: 0.7em;
    margin-bottom: 8px;
    color: #555;
}

.meta-item a {
    color: #1f77b4;
    text-decoration: none;
    border-bottom: 1px solid #1f77b4;
}
</style>

<div class="meta-container">
  <div class="meta-grid">

    <div class="meta-item">
      <b>CLIENT</b>
      Circular Energy Fund
    </div>

    <div class="meta-item">
      <b>LINK</b>
      <a href="#">Project Dashboard</a>
    </div>

    <div class="meta-item">
      <b>AWARDS</b>
      Concept demo
    </div>

    <div class="meta-item">
      <b>CATEGORIES</b>
      Renewable Energy<br>
      Data Visualization
    </div>

    <div class="meta-item">
      <b>TOOLS</b>
      Python<br>
      Streamlit<br>
      Plotly
    </div>

    <div class="meta-item">
      <b>DATA</b>
      IPCC<br>
      Eurostat
    </div>

  </div>
</div>
""",
height=180
)
st.divider()

# =========================
# HEADER
# =========================
st.title("🟢 Circular Energy Fund")
st.subheader("Veicolo di investimento partecipativo e sostenibile")

# =========================
# KPI SECTION
# =========================
col1, col2, col3, col4 = st.columns(4)

total_capacity_kwp = 200
annual_production_mwh = energy["production_kwh"].sum() / 1000
co2_avoided = 135
n_members = len(members)

col1.metric("Capacità installata", f"{total_capacity_kwp} kWp")
col2.metric("Produzione annua", f"{annual_production_mwh:.0f} MWh")
col3.metric("Soci", n_members)
col4.metric("CO₂ evitata", f"{co2_avoided} t/anno")


st.subheader("🟢 Perché è un fondo circolare")

st.info("""
Il **Circular Energy Fund** è concepito come un **sistema circolare**, in cui
energia, benefici economici e dati rimangono all’interno della comunità dei soci.

**In pratica:**
- l’energia prodotta viene prioritariamente **autoconsumata dai soci**
- i benefici economici derivano da **risparmi diretti**, non da speculazione
- produzione, consumi e flussi economici sono **misurabili e verificabili**
- la governance è **partecipativa e orientata al lungo periodo**

Questo approccio riduce l’esposizione alla volatilità dei prezzi energetici
e rafforza la resilienza economica della comunità.
""")

st.subheader("🟢 Benefici per il singolo socio")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.success("""
    **🟢 Energia a prezzo agevolato**

    Accesso a energia rinnovabile
    a un prezzo stabile e inferiore
    rispetto al mercato.
    """)

with col_b:
    st.success("""
    **🟢 Risparmio economico**

    Riduzione della spesa energetica
    annuale grazie all’autoconsumo
    condiviso.
    """)

with col_c:
    st.success("""
    **🟢 Impatto positivo**

    Partecipazione attiva a un
    progetto sostenibile, locale
    e trasparente.
    """)

# =========================
# MAPPA – LOCALIZZAZIONE PROGETTO
# =========================
st.header("🟢 Localizzazione del Progetto")

st.markdown("""
L’impianto fotovoltaico è localizzato in **Sicilia**, in un’area idonea che
non sottrae terreno all’agricoltura e favorisce l’integrazione con il territorio.
""")

# Coordinate progetto (Sicilia)
project_location = pd.DataFrame({
    "name": ["Impianto Fotovoltaico – Circular Energy Fund"],
    "lat": [37.5],
    "lon": [14.0]
})

fig_map = px.scatter_geo(
    project_location,
    lat="lat",
    lon="lon",
    text="name",
    projection="natural earth",
)

fig_map.update_traces(
    marker=dict(
        size=14,
        color="orange",
        symbol="circle"
    ),
    textposition="top center"
)

fig_map.update_layout(
    geo=dict(
        scope="europe",
        center=dict(lat=37.5, lon=14.0),
        projection_scale=6,
        showland=True,
        landcolor="rgb(243, 243, 243)",
        showcountries=True,
        countrycolor="rgb(204, 204, 204)"
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)

st.plotly_chart(fig_map, use_container_width=True)


# =========================
# TIMELINE PROGETTO (20 ANNI)
# =========================
st.header("🟢 Timeline del Progetto (20 anni)")

st.markdown("""
La timeline seguente illustra l’evoluzione del progetto nel tempo,
dall’investimento iniziale fino alla piena maturità economica ed energetica.
""")

fig_timeline = px.line(
    cashflow,
    x="year",
    y="cumulative_cashflow",
    markers=True,
    title="Evoluzione del valore cumulato del progetto"
)

fig_timeline.add_hline(
    y=0,
    line_dash="dash",
    line_color="red",
    annotation_text="Break-even",
    annotation_position="top left"
)

fig_timeline.update_layout(
    xaxis_title="Anno",
    yaxis_title="Cashflow cumulato (€)"
)

st.plotly_chart(fig_timeline, use_container_width=True)

# =========================
st.subheader("🟢 Fasi chiave del progetto")

col_a, col_b = st.columns(2)

with col_a:
    st.success("""
    **2024 – Avvio del progetto**
- Investimento iniziale per la realizzazione dell’impianto
- Avvio della produzione di energia rinnovabile

**2025–2029 – Fase di stabilizzazione**
- Riduzione della spesa energetica per i soci
- Miglioramento dell’autoconsumo e dell’efficienza
- Avvicinamento al punto di pareggio (break‑even)
    """)

with col_b:
    st.success("""
    **2030 – Break-even**
- Recupero dell’investimento iniziale
- Il progetto diventa economicamente autosufficiente

**2031–2044 – Maturità**
- Benefici economici ed energetici stabili
- Protezione dalla volatilità dei prezzi dell’energia
- Massimizzazione dell’impatto ambientale e sociale
    """)
# =========================


col1, col2, col3 = st.columns(3)

col1.metric("Durata progetto", "20 anni")
col2.metric("Break-even", "≈ 7–8 anni")
col3.metric("Benefici netti a regime", "≥ 30.000 €/anno")


# =========================
# ENERGY PRODUCTION (LINE CHART)
# =========================
st.header("🟢 Produzione Fotovoltaica")

fig_prod = px.line(
    energy,
    x="date",
    y="production_kwh",
    title="Produzione fotovoltaica giornaliera (Sicilia)",
    labels={
        "date": "Data",
        "production_kwh": "Produzione (kWh)"
    }
)

st.plotly_chart(fig_prod, use_container_width=True)

# =========================
# CONSUMPTION VS SELF-CONSUMPTION
# =========================
st.header("🟢 Autoconsumo Comunità")

fig_cons = px.line(
    consumption,
    x="date",
    y=["total_consumption_kwh", "self_consumed_kwh"],
    title="Consumo totale vs Autoconsumo",
    labels={"value": "kWh", "variable": "Tipo"}
)

st.plotly_chart(fig_cons, use_container_width=True)

# =========================
# MEMBERS DISTRIBUTION (BAR)
# =========================
st.header("🟢 Distribuzione Energia ai Soci")

fig_members = px.bar(
    members,
    x="member_id",
    y="energy_share_kwh",
    title="Energia condivisa per socio",
    labels={
        "member_id": "Socio",
        "energy_share_kwh": "Energia (kWh)"
    }
)

st.plotly_chart(fig_members, use_container_width=True)

# =========================
# CASHFLOW (LINE)
# =========================
st.header("🟢 Analisi Economica")

fig_cash = px.line(
    cashflow,
    x="year",
    y=["net_cashflow", "cumulative_cashflow"],
    title="Cashflow del progetto",
    labels={"value": "€", "variable": "Tipo"}
)

st.plotly_chart(fig_cash, use_container_width=True)
# =========================


# =========================
# SCENARI CLIMATICI (20 ANNI)
# =========================

st.header("🟢 Scenari di lungo periodo e cambiamento climatico")

st.markdown("""
L’analisi seguente considera tre **scenari evolutivi** su un orizzonte di **20 anni**.
Gli scenari tengono conto sia di fattori **climatici** (irraggiamento, temperature),
sia di fattori **economici** (prezzo dell’energia, efficienza tecnologica).
""")

years = cashflow["year"]

base_cashflow = cashflow["net_cashflow"]

scenarios = pd.DataFrame({
    "year": years,
    "Pessimistico": base_cashflow * (1 - 0.2 * (years - years.min())),
    "Realistico": base_cashflow * (1 - 0.01 * (years - years.min())),
    "Ottimistico": base_cashflow * (1 + 0.09 * (years - years.min()))
})

# Cumulative cashflow
scenarios_cum = scenarios.copy()
for col in ["Pessimistico", "Realistico", "Ottimistico"]:
    scenarios_cum[col] = scenarios[col].cumsum()

fig_scenarios = px.line(
    scenarios_cum,
    x="year",
    y=["Pessimistico", "Realistico", "Ottimistico"],
    title="Evoluzione del cashflow cumulato – Scenari climatici",
    labels={"value": "Cashflow cumulato (€)", "variable": "Scenario"}
)

fig_scenarios.add_hline(
    y=0,
    line_dash="dash",
    line_color="red",
    annotation_text="Break-even"
)

st.plotly_chart(fig_scenarios, use_container_width=True)

st.markdown("""
**Interpretazione degli scenari**

- 🔴 **Scenario pessimista**: il progetto rimane sostenibile, ma con tempi di rientro più lunghi.
- 🟡 **Scenario realistico**: il progetto raggiunge il break-even e genera benefici stabili nel lungo periodo.
- 🟢 **Scenario ottimistico**: il miglioramento tecnologico e la resilienza climatica anticipano i benefici.

In tutti gli scenari, la **localizzazione in Sicilia** e l’orientamento all’autoconsumo
contribuiscono a mitigare i rischi climatici ed economici.
""")
# =========================
# MARKET COMPARISON
# =========================
st.header("🟢 Prezzo Energia – Confronto Mercato")

fig_market = px.line(
    market,
    x="year",
    y=["italy_price_eur_kwh", "eu_avg_price_eur_kwh", "cef_member_price"],
    title="Prezzo energia (€ / kWh)",
    labels={"value": "€/kWh", "variable": "Mercato"}
)

st.plotly_chart(fig_market, use_container_width=True)

# =========================
# SMART GRID COMMUNITY
# =========================

st.header("⚡ Smart Grid Comunitaria")

st.markdown("""
La Smart Grid del **Circular Energy Fund** coordina in tempo reale
la produzione fotovoltaica e i consumi dei soci, con l’obiettivo di:

- massimizzare l’**autoconsumo locale**
- ridurre la dipendenza dalla rete elettrica
- garantire una distribuzione **equa e trasparente** dell’energia
- aumentare la resilienza del sistema nel lungo periodo
""")

# =========================
# SMART GRID – ENERGY FLOWS
# =========================
st.subheader("🔌 Flussi energetici della Smart Grid")

smartgrid_df = pd.DataFrame({
    "Fonte": ["Produzione FV", "Produzione FV", "Produzione FV"],
    "Destinazione": ["Autoconsumo Soci", "Rete Elettrica", "Perdite"],
    "Energia (kWh)": [
        consumption["self_consumed_kwh"].sum(),
        (energy["production_kwh"].sum() - consumption["self_consumed_kwh"].sum()),
        energy["production_kwh"].sum() * 0.02  # perdite stimate 2%
    ]
})

fig_sg = px.bar(
    smartgrid_df,
    x="Destinazione",
    y="Energia (kWh)",
    color="Destinazione",
    title="Distribuzione dell’energia nella Smart Grid"
)

st.plotly_chart(fig_sg, use_container_width=True)

st.subheader("🟢 Indicatori Smart Grid")

col1, col2, col3, col4 = st.columns(4)

autoconsumo_rate = consumption["self_consumed_kwh"].sum() / energy["production_kwh"].sum()

col1.metric("Autoconsumo", f"{autoconsumo_rate:.0%}")
col2.metric("Energia condivisa", f"{consumption['self_consumed_kwh'].sum()/1000:.0f} MWh")
col3.metric("Energia immessa in rete", f"{(energy['production_kwh'].sum() - consumption['self_consumed_kwh'].sum())/1000:.0f} MWh")
col4.metric("Efficienza Smart Grid", "Alta")

st.info("""
La Smart Grid consente di adattare il sistema alle variazioni climatiche,
ottimizzando l’uso dell’energia nei periodi di maggiore produzione
e riducendo gli sprechi in condizioni estreme.
""")

# =========================
# SMART GRID – HEATMAP
# =========================

st.header("🟢 Smart Grid – Produzione vs Consumo (Heatmap Oraria)")

st.markdown("""
La seguente heatmap rappresenta una **ricostruzione oraria realistica**
della produzione fotovoltaica e dei consumi della comunità,
basata su profili tipici italiani.

🟢 Serve a visualizzare **come la Smart Grid coordina produzione e domanda**
nell’arco della giornata.
""")
import numpy as np

def hourly_profile(hours, peak_hour, width=3):
    """Genera una curva gaussiana normalizzata"""
    return np.exp(-0.5 * ((hours - peak_hour) / width) ** 2)

hours = np.arange(24)

# Profili normalizzati
pv_profile = hourly_profile(hours, peak_hour=13, width=3)
pv_profile /= pv_profile.sum()

consumption_profile = (
    hourly_profile(hours, 8, 2) +
    hourly_profile(hours, 20, 3)
)
consumption_profile /= consumption_profile.sum()

# Usa un mese rappresentativo (es. giugno)
month_data = energy[energy["date"].dt.month == 6].copy()
cons_month = consumption[consumption["date"].dt.month == 6]

records = []

for _, row in month_data.iterrows():
    day = row["date"].date()
    daily_prod = row["production_kwh"]
    daily_cons = cons_month.loc[
        cons_month["date"] == row["date"], "total_consumption_kwh"
    ].values[0]

    for h in hours:
        records.append({
            "day": day,
            "hour": h,
            "production_kwh": daily_prod * pv_profile[h],
            "consumption_kwh": daily_cons * consumption_profile[h],
        })

hourly_df = pd.DataFrame(records)

st.subheader("🟢 Produzione fotovoltaica – Heatmap")

prod_heat = hourly_df.pivot_table(
    index="hour",
    columns="day",
    values="production_kwh",
    aggfunc="sum"
)

fig_prod_heat = px.imshow(
    prod_heat,
    aspect="auto",
    color_continuous_scale="YlOrRd",
    labels=dict(x="Giorno", y="Ora", color="kWh"),
)

st.plotly_chart(fig_prod_heat, use_container_width=True)

st.subheader("🟢 Consumo comunità – Heatmap")

cons_heat = hourly_df.pivot_table(
    index="hour",
    columns="day",
    values="consumption_kwh",
    aggfunc="sum"
)

fig_cons_heat = px.imshow(
    cons_heat,
    aspect="auto",
    color_continuous_scale="Blues",
    labels=dict(x="Giorno", y="Ora", color="kWh"),
)

st.plotly_chart(fig_cons_heat, use_container_width=True)

st.info("""
**Come leggere le heatmap**

- Le aree più intense indicano **maggiore produzione o consumo**
- Il picco di produzione avviene nelle ore centrali della giornata
- I picchi di consumo avvengono al mattino e in serata
- La Smart Grid consente di **allineare domanda e produzione**
  attraverso autoconsumo e gestione intelligente dei carichi
""")

# =========================
# SMART GRID – BATTERY STORAGE
# =========================

st.header("🟢 Smart Grid – Simulazione Sistema di Accumulo (Batterie)")

st.markdown("""
La simulazione seguente mostra l’effetto di un **sistema di accumulo**
integrato nella Smart Grid comunitaria.

**Ipotesi principali:**
- Capacità batteria: **500 kWh**
- Efficienza carica/scarica: **90%**
- Priorità: autoconsumo → batteria → rete
- Orizzonte: profilo orario tipico (mese rappresentativo)
""")

BATTERY_CAPACITY = 500  # kWh
BATTERY_EFFICIENCY = 0.9

battery_level = 0
battery_trace = []

for _, row in hourly_df.iterrows():
    production = row["production_kwh"]
    consumption = row["consumption_kwh"]

    surplus = production - consumption

    # Caso 1: surplus → carica batteria
    if surplus > 0:
        charge = min(
            surplus * BATTERY_EFFICIENCY,
            BATTERY_CAPACITY - battery_level
        )
        battery_level += charge
        grid_export = surplus - charge
        battery_discharge = 0

    # Caso 2: deficit → scarica batteria
    else:
        discharge = min(
            battery_level,
            abs(surplus) / BATTERY_EFFICIENCY
        )
        battery_level -= discharge
        battery_discharge = discharge
        grid_export = 0

    battery_trace.append({
        "day": row["day"],
        "hour": row["hour"],
        "battery_level_kwh": battery_level,
        "battery_charge_kwh": max(surplus, 0),
        "battery_discharge_kwh": battery_discharge,
        "grid_export_kwh": grid_export,
    })

battery_df = pd.DataFrame(battery_trace)

st.subheader("🟢 Livello di carica della batteria")

fig_battery = px.line(
    battery_df,
    x=battery_df.index,
    y="battery_level_kwh",
    title="Evoluzione del livello di carica della batteria",
    labels={"battery_level_kwh": "kWh"}
)

st.plotly_chart(fig_battery, use_container_width=True)

st.subheader("🟢 Impatto del sistema di accumulo")

energy_without_storage = (
    hourly_df["production_kwh"].sum()
    - hourly_df["consumption_kwh"].sum()
)

energy_with_storage = battery_df["battery_discharge_kwh"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Capacità batteria", f"{BATTERY_CAPACITY} kWh")
col2.metric("Energia resa disponibile", f"{energy_with_storage:.0f} kWh")
col3.metric("Riduzione energia immessa in rete", "Significativa")

st.subheader("🟢 Autoconsumo con accumulo – Heatmap")

autoconsumption_with_storage = (
    hourly_df["consumption_kwh"]
    - battery_df["grid_export_kwh"]
)

heat_storage = pd.DataFrame({
    "hour": hourly_df["hour"],
    "day": hourly_df["day"],
    "autoconsumption_kwh": autoconsumption_with_storage
})

heatmap_storage = heat_storage.pivot_table(
    index="hour",
    columns="day",
    values="autoconsumption_kwh",
    aggfunc="sum"
)

fig_storage_heat = px.imshow(
    heatmap_storage,
    aspect="auto",
    color_continuous_scale="Greens",
    labels=dict(x="Giorno", y="Ora", color="kWh"),
)

st.plotly_chart(fig_storage_heat, use_container_width=True)

st.info("""
**Cosa dimostra la simulazione**

- La batteria accumula energia nelle ore di surplus fotovoltaico
- L’energia viene rilasciata nelle ore serali e notturne
- L’autoconsumo aumenta in modo significativo
- La Smart Grid diventa più resiliente a:
  - variazioni climatiche
  - picchi di consumo
  - volatilità dei prezzi energetici
""")


# =========================
# FOOTER
# =========================
st.divider()

st.markdown(
    """
    <div style="text-align: center; color: grey; font-size: 0.9em;">
        🟢 Contatto: <a href="mailto:danki.datastudio@gmail.com">danki.datastudio@gmail.com</a><br>
        Dati simulati a scopo illustrativo – Circular Energy Fund
    </div>
    """,
    unsafe_allow_html=True
)