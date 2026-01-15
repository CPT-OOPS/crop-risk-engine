import streamlit as st
from engine.loader import load_data
from engine.anomaly import rainfall_deviation, temperature_stress, yield_drop
from engine.risk_score import calculate_risk, risk_level
from engine.pdf_report import generate_pdf
import os

st.set_page_config(page_title="Crop Risk Engine", layout="centered")

st.title("🌾 Crop Failure Early Warning System")

file = st.file_uploader("Upload district CSV file", type=["csv"])

if file:
    df = load_data(file)

    district = df["district"].iloc[0]

    rain_dev = rainfall_deviation(df["rainfall"])
    temp_dev = temperature_stress(df["temp"])
    yield_dev = yield_drop(df["yield"])

    risk = calculate_risk(rain_dev, temp_dev, yield_dev)
    level = risk_level(risk)

    st.subheader(f"District: {district}")

    st.metric("Rainfall Deviation (%)", rain_dev)
    st.metric("Temperature Stress (°C)", temp_dev)
    st.metric("Yield Drop (%)", yield_dev)

    st.subheader(f"⚠ Risk Level: {level}")

    if st.button("Generate PDF Report"):
        os.makedirs("reports", exist_ok=True)
        path = f"reports/{district}_crop_risk_report.pdf"
        report = [
            f"District: {district}",
            f"Rainfall Deviation: {rain_dev}%",
            f"Temperature Stress: {temp_dev}°C",
            f"Yield Drop: {yield_dev}%",
            f"Risk Score: {risk}",
            f"Risk Level: {level}"
        ]
        generate_pdf(path, report)

        with open(path, "rb") as f:
            st.download_button("Download Report", f, file_name=os.path.basename(path))
