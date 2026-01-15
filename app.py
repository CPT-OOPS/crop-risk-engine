import streamlit as st
import pandas as pd
from engine.anomaly import rainfall_deviation, temperature_stress, yield_drop
from engine.risk_score import calculate_risk, risk_level
from engine.pdf_report import generate_pdf
import os

st.set_page_config(page_title="Crop Risk Dashboard", layout="wide")
st.title("🌾 Crop Failure Early Warning Dashboard")

DATA_PATH = "data/districts.csv"
df = pd.read_csv(DATA_PATH)

districts = df["district"].unique().tolist()
selected = st.selectbox("Select District", districts)

ddf = df[df["district"] == selected].sort_values("year")

rain_dev = rainfall_deviation(ddf["rainfall"])
temp_dev = temperature_stress(ddf["temp"])
yield_dev = yield_drop(ddf["yield"])

risk = calculate_risk(rain_dev, temp_dev, yield_dev)
level = risk_level(risk)

col1, col2, col3 = st.columns(3)
col1.metric("Rainfall Deviation (%)", rain_dev)
col2.metric("Temperature Stress (°C)", temp_dev)
col3.metric("Yield Drop (%)", yield_dev)

st.subheader(f"⚠ Risk Level: {level}")

st.line_chart(ddf.set_index("year")[["rainfall","temp","yield"]])

if st.button("Generate PDF Report"):
    os.makedirs("reports", exist_ok=True)
    path = f"reports/{selected}_risk_report.pdf"
    report = [
        f"District: {selected}",
        f"Rainfall Deviation: {rain_dev}%",
        f"Temperature Stress: {temp_dev}°C",
        f"Yield Drop: {yield_dev}%",
        f"Risk Score: {risk}",
        f"Risk Level: {level}"
    ]
    generate_pdf(path, report)

    with open(path, "rb") as f:
        st.download_button("Download Report", f, file_name=os.path.basename(path))
