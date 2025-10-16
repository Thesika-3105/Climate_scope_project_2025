import streamlit as st
import pandas as pd
import plotly.express as px

# ================================
# 🔸 Page Configuration
# ================================
st.set_page_config(page_title="ClimateScope Dashboard", layout="wide")

# ================================
# 📥 Load Data
# ================================
@st.cache_data
def load_data():
    df = pd.read_csv("processed/cleaned_weather.csv")
    df['last_updated'] = pd.to_datetime(df['last_updated'], errors='coerce')
    return df

df = load_data()

st.title("🌍 ClimateScope – Global Weather Insights Dashboard (Final Version)")

# Show dataset columns
st.subheader("🔎 Columns in dataset:")
st.write(list(df.columns))

# ================================
# 📅 Date Range Setup
# ================================
min_dt = df['last_updated'].min()
max_dt = df['last_updated'].max()

# Sidebar Filters
st.sidebar.header("🔧 Global Filters")

# ✅ Unique keys added to avoid duplicate widget errors
date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=min_dt,
    max_value=max_dt,
    value=(min_dt, max_dt),
    key="global_date_slider"
)

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=sorted(df['country'].dropna().unique()),
    default=[],
    key="global_country_multiselect"
)

# Filter data based on selections
mask = (df['last_updated'] >= pd.to_datetime(date_range[0])) & (df['last_updated'] <= pd.to_datetime(date_range[1]))
if selected_countries:
    mask &= df['country'].isin(selected_countries)

filtered_df = df[mask]

st.write(f"📊 Showing data for {len(filtered_df)} records")

# ================================
# 📈 TABS FOR SECTIONS
# ================================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Trends", "📅 Seasonality", "📊 Correlations", "🌍 Geographic", "⚠️ Extremes"])

# ----------------------------
# 📈 1. Trends
# ----------------------------
with tab1:
    st.subheader("📈 Global / Regional Trends")

    st.write("👉 Time-series charts will go here.")
    if not filtered_df.empty:
        fig = px.line(
            filtered_df.sort_values("last_updated"),
            x="last_updated",
            y="temperature_celsius",
            color="country",
            title="Temperature Trends Over Time"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for the selected filters.")

# ----------------------------
# 📅 2. Seasonality
# ----------------------------
with tab2:
    st.subheader("📅 Seasonal Patterns")

    st.write("👉 Monthly/seasonal analysis will go here.")

    season_countries = st.multiselect(
        "Select Countries for Seasonality",
        options=sorted(df['country'].dropna().unique()),
        key="seasonality_multiselect"
    )

    if season_countries:
        season_df = df[df['country'].isin(season_countries)]
        season_df['month'] = season_df['last_updated'].dt.month
        fig = px.box(
            season_df,
            x="month",
            y="temperature_celsius",
            color="country",
            title="Seasonal Temperature Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# 📊 3. Correlations
# ----------------------------
with tab3:
    st.subheader("📊 Correlations")

    st.write("👉 Correlation heatmaps or scatter plots can go here.")
    numeric_cols = df.select_dtypes(include=['number']).columns
    st.write(filtered_df[numeric_cols].corr())

# ----------------------------
# 🌍 4. Geographic Patterns
# ----------------------------
with tab4:
    st.subheader("🌍 Geographic Patterns")

    st.write("👉 Choropleth or map visualizations will go here.")
    if not filtered_df.empty:
        fig = px.scatter_geo(
            filtered_df,
            lat="latitude",
            lon="longitude",
            color="temperature_celsius",
            hover_name="location_name",
            size="temperature_celsius",
            projection="natural earth",
            title="Temperature Distribution Map"
        )
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# ⚠️ 5. Extremes
# ----------------------------
with tab5:
    st.subheader("⚠️ Extreme Weather Events")
    st.write("👉 Detected anomalies or extremes will be displayed here.")

    extremes_df = filtered_df[
        (filtered_df['temperature_celsius'] > 45) | (filtered_df['temperature_celsius'] < -20)
    ]
    st.write(extremes_df.head(50))
