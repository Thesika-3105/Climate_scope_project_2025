 feature/milestone2
import pandas as pd
import streamlit as st
import plotly.express as px

# 🌍 Streamlit page setup
st.set_page_config(page_title="ClimateScope Dashboard", layout="wide")
st.title("🌍 ClimateScope – Global Weather Insights Dashboard (Wireframe)")

# 📥 Load dataset with proper time conversion
@st.cache_data
def load_data():
    df = pd.read_csv("processed/cleaned_weather.csv")

    # 🔎 Show columns to confirm structure
    st.write("🔎 Columns in dataset:", df.columns.tolist())

    # ✅ Use 'last_updated' column for time if available
    if "year_month" in df.columns:
        df["year_month"] = pd.PeriodIndex(df["year_month"], freq="M").to_timestamp()

    elif "last_updated" in df.columns:
        df["year_month"] = pd.to_datetime(df["last_updated"], errors="coerce").dt.to_period("M").dt.to_timestamp()

    elif "date" in df.columns:
        df["year_month"] = pd.to_datetime(df["date"], errors="coerce").dt.to_period("M").dt.to_timestamp()

    else:
        # Fallback if no date-like column
        st.warning("⚠️ No time column found — using dummy date.")
        df["year_month"] = pd.to_datetime("2000-01-01")

    # Drop rows where year_month couldn't be parsed
    df = df.dropna(subset=["year_month"])
    df["year_month"] = pd.to_datetime(df["year_month"])

    return df

# Load the data
df = load_data()

# 🧠 Detect useful columns
country_col = "country" if "country" in df.columns else None
temp_col = next((c for c in df.columns if "temp" in c.lower() or "temperature" in c.lower()), None)

# 🧰 Sidebar filters
st.sidebar.header("Filters")

# ✅ Ensure min/max are Python datetime, not pandas Timestamps
min_dt = pd.to_datetime(df["year_month"].min()).to_pydatetime()
max_dt = pd.to_datetime(df["year_month"].max()).to_pydatetime()

date_range = st.sidebar.slider(
    "Date Range", min_value=min_dt, max_value=max_dt, value=(min_dt, max_dt)
)

selected_countries = []
if country_col:
    countries = sorted(df[country_col].dropna().unique().tolist())
    selected_countries = st.sidebar.multiselect(
        "Select Countries", countries[:50], default=countries[:5]
    )

# 🪄 Apply filters
mask = df["year_month"].between(date_range[0], date_range[1])
if country_col and selected_countries:
    mask &= df[country_col].isin(selected_countries)
dfv = df[mask]

# 🧭 Dashboard Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Trends", "📅 Seasonality", "📊 Correlations", "🌍 Geographic", "⚠️ Extremes"]
)

with tab1:
    st.subheader("📈 Global / Regional Trends")
    st.info("👉 Placeholder: Time-series charts will go here.")

with tab2:
    st.subheader("📅 Seasonal Patterns")
    st.info("👉 Placeholder: Monthly seasonality charts will go here .")

with tab3:
    st.subheader("📊 Correlation Analysis")
    st.info("👉 Placeholder: Correlation heatmap will go here .")

with tab4:
    st.subheader("🌍 Geographic Visualization")
    st.info("👉 Placeholder: Choropleth maps will go here .")

with tab5:
    st.subheader("⚠️ Extreme Events")
    st.info("👉 Placeholder: Extreme event charts will go here.")

import pandas as pd
import streamlit as st
import plotly.express as px

# 🌍 Streamlit page setup
st.set_page_config(page_title="ClimateScope Dashboard", layout="wide")
st.title("🌍 ClimateScope – Global Weather Insights Dashboard (Wireframe)")

# 📥 Load dataset with proper time conversion
@st.cache_data
def load_data():
    df = pd.read_csv("processed/cleaned_weather.csv")

    # 🔎 Show columns to confirm structure
    st.write("🔎 Columns in dataset:", df.columns.tolist())

    # ✅ Use 'last_updated' column for time if available
    if "year_month" in df.columns:
        df["year_month"] = pd.PeriodIndex(df["year_month"], freq="M").to_timestamp()

    elif "last_updated" in df.columns:
        df["year_month"] = pd.to_datetime(df["last_updated"], errors="coerce").dt.to_period("M").dt.to_timestamp()

    elif "date" in df.columns:
        df["year_month"] = pd.to_datetime(df["date"], errors="coerce").dt.to_period("M").dt.to_timestamp()

    else:
        # Fallback if no date-like column
        st.warning("⚠️ No time column found — using dummy date.")
        df["year_month"] = pd.to_datetime("2000-01-01")

    # Drop rows where year_month couldn't be parsed
    df = df.dropna(subset=["year_month"])
    df["year_month"] = pd.to_datetime(df["year_month"])

    return df

# Load the data
df = load_data()

# 🧠 Detect useful columns
country_col = "country" if "country" in df.columns else None
temp_col = next((c for c in df.columns if "temp" in c.lower() or "temperature" in c.lower()), None)

# 🧰 Sidebar filters
st.sidebar.header("Filters")

# ✅ Ensure min/max are Python datetime, not pandas Timestamps
min_dt = pd.to_datetime(df["year_month"].min()).to_pydatetime()
max_dt = pd.to_datetime(df["year_month"].max()).to_pydatetime()

date_range = st.sidebar.slider(
    "Date Range", min_value=min_dt, max_value=max_dt, value=(min_dt, max_dt)
)

selected_countries = []
if country_col:
    countries = sorted(df[country_col].dropna().unique().tolist())
    selected_countries = st.sidebar.multiselect(
        "Select Countries", countries[:50], default=countries[:5]
    )

# 🪄 Apply filters
mask = df["year_month"].between(date_range[0], date_range[1])
if country_col and selected_countries:
    mask &= df[country_col].isin(selected_countries)
dfv = df[mask]

# 🧭 Dashboard Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Trends", "📅 Seasonality", "📊 Correlations", "🌍 Geographic", "⚠️ Extremes"]
)

with tab1:
    st.subheader("📈 Global / Regional Trends")
    st.info("👉 Placeholder: Time-series charts will go here.")

with tab2:
    st.subheader("📅 Seasonal Patterns")
    st.info("👉 Placeholder: Monthly seasonality charts will go here .")

with tab3:
    st.subheader("📊 Correlation Analysis")
    st.info("👉 Placeholder: Correlation heatmap will go here .")

with tab4:
    st.subheader("🌍 Geographic Visualization")
    st.info("👉 Placeholder: Choropleth maps will go here .")

with tab5:
    st.subheader("⚠️ Extreme Events")
    st.info("👉 Placeholder: Extreme event charts will go here.")
 main
