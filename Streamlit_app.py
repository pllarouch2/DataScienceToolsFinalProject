import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Analyse Hôtelière", layout="wide")

st.title("🏨 Dashboard Analyse : City Hotel vs Resort Hotel")
st.markdown("Ce tableau de bord explore les tendances de réservations, les prix et les annulations.")


# 1. Chargement des données
@st.cache_data
def load_data():
    # Assure-toi que le fichier csv est dans le même dossier
    df = pd.read_csv('data/hotel_bookings.csv')
    return df


df = load_data()

# --- SIDEBAR (Filtres) ---
st.sidebar.header("Filtres")
# Filtre par type d'hôtel
hotel_filter = st.sidebar.multiselect(
    "Choisir le type d'hôtel:",
    options=df["hotel"].unique(),
    default=df["hotel"].unique()
)

# Filtre par année
year_filter = st.sidebar.multiselect(
    "Choisir l'année:",
    options=sorted(df["arrival_date_year"].unique()),
    default=sorted(df["arrival_date_year"].unique())
)

# Application des filtres
df_selection = df.query("hotel == @hotel_filter & arrival_date_year == @year_filter")

# --- KPI (Indicateurs Clés) ---
st.subheader("Vue d'ensemble")
col1, col2, col3 = st.columns(3)

total_bookings = df_selection.shape[0]
avg_adr = df_selection['adr'].mean()
cancel_rate = (df_selection['is_canceled'].mean() * 100)

col1.metric("Nombre de réservations", f"{total_bookings:,}")
col2.metric("Prix Moyen (ADR)", f"{avg_adr:.2f} €")
col3.metric("Taux d'annulation", f"{cancel_rate:.1f} %")

st.markdown("---")

# --- ONGLETS D'ANALYSE ---
tab1, tab2, tab3 = st.tabs(["📊 Évolution Temporelle", "🌍 Provenance & Segments", "💰 Analyse des Prix"])

with tab1:
    st.header("Saisonnalité des réservations")
    # Préparation des données pour le graphique temporel
    # On trie les mois correctement
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

    # On compte les réservations par mois et par hôtel
    monthly_data = df_selection.groupby(['arrival_date_month', 'hotel']).size().reset_index(name='count')

    # Visualisation Plotly (Interactive)
    fig_time = px.line(monthly_data, x='arrival_date_month', y='count', color='hotel',
                       category_orders={"arrival_date_month": month_order},
                       markers=True, title="Nombre de réservations par mois")
    st.plotly_chart(fig_time, use_container_width=True)

with tab2:
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Top 10 Pays d'origine")
        top_countries = df_selection['country'].value_counts().head(10).reset_index()
        top_countries.columns = ['country', 'count']
        fig_map = px.bar(top_countries, x='country', y='count', color='count',
                         title="Origine des clients (Top 10)")
        st.plotly_chart(fig_map, use_container_width=True)

    with col_right:
        st.subheader("Segments de marché")
        # Pie chart des segments
        fig_pie = px.pie(df_selection, names='market_segment', title="Répartition par segment de marché")
        st.plotly_chart(fig_pie, use_container_width=True)

with tab3:
    st.header("Distribution des Prix (ADR)")

    # On filtre les valeurs aberrantes pour le graphique (ADR < 500) pour y voir plus clair
    df_price = df_selection[df_selection['adr'] < 500]

    fig_box = px.box(df_price, x="hotel", y="adr", color="hotel",
                     title="Distribution du prix moyen par nuit (Boxplot)",
                     points="outliers")  # Affiche les points aberrants
    st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("**Note:** Les valeurs extrêmes supérieures à 500€ ont été masquées pour la lisibilité.")