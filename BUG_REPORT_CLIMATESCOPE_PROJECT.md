# 🪲 Overall Bug Report — ClimateScope Dashboard Project 2025

## 📘 Project Information
**Project Title:** ClimateScope Dashboard Analysis  
**Developer:** Thesika S N  
**Frameworks Used:** Streamlit, Plotly, Pandas, NumPy  
**Language:** Python 3.10+   
**Final Report Date:** November 2025  

---

## 🧭 Overview
The **ClimateScope Dashboard** is a climate analytics application that visualizes global weather trends, air quality indices, and extreme climate patterns using real-time data.  

Throughout development, multiple issues were encountered — ranging from data serialization and visualization deprecations to layout misalignments and functional bugs.  
This report consolidates **all major bugs identified and resolved** during the project lifecycle.

---

## 🐞 Summary of Reported Bugs

| **Bug ID** | **Category** | **Issue Summary** | **Status** |
|-------------|---------------|-------------------|-------------|
| B-001 | Data Loading | File path handling failure when dataset not found | ✅ Fixed |
| B-002 | Plot Rendering | Missing or blank visualizations in certain tabs | ✅ Fixed |
| B-003 | Deprecation | Plotly `scatter_mapbox()` deprecated | ✅ Fixed |
| B-004 | Serialization | PyArrow ArrowInvalid datetime conversion error | ✅ Fixed |
| B-005 | Visualization | Missing Wind Speed Analysis plot | ✅ Fixed |
| B-006 | DataTable | Excessive empty boxes in Summary statistics | ✅ Fixed |
| B-007 | Mapping | Country name mapping deprecated (`locationmode="country names"`) | ✅ Fixed |
| B-008 | Layout/UI | Inconsistent spacing and misaligned gradient boxes | ✅ Fixed |
| B-009 | Streamlit Config | Deprecated chart displayModeBar keyword | ✅ Fixed |
| B-010 | Plot Visibility | Non-rendering plots on tabs (only overview visible) | ✅ Fixed |
| B-011 | AQI Table | Table overflow and missing color styling | ✅ Fixed |
| B-012 | Missing Docs | Guidelines and Help page not integrated | ✅ Fixed |

---

## 🧩 Detailed Bug Analysis and Fixes

### 🐛 B-001 — Dataset Loading Failure
**Symptom:**  
The dashboard stopped execution when `cleaned_weather.csv` wasn’t found in the expected path.

**Cause:**  
Hardcoded file path dependency caused failure when directory structure changed.

**Fix:**  
Added flexible file search across multiple directories:
```python
for f in ["processed/cleaned_weather.csv", "cleaned_weather.csv", "data/cleaned_weather.csv"]:
    if os.path.exists(f):
        return pd.read_csv(f)
