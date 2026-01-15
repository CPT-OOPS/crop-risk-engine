from engine.loader import load_data
from engine.anomaly import rainfall_deviation, temperature_stress, yield_drop
from engine.risk_score import calculate_risk, risk_level
from engine.pdf_report import generate_pdf

df = load_data("data/sample.csv")

district = df["district"].iloc[0]

rain_dev = rainfall_deviation(df["rainfall"])
temp_dev = temperature_stress(df["temp"])
yield_dev = yield_drop(df["yield"])

risk = calculate_risk(rain_dev, temp_dev, yield_dev)
level = risk_level(risk)

report = [
    f"District: {district}",
    f"Rainfall Deviation: {rain_dev}%",
    f"Temperature Stress: {temp_dev}°C",
    f"Yield Drop: {yield_dev}%",
    "-------------------------------",
    f"RISK SCORE: {risk}",
    f"RISK LEVEL: {level}"
]

for line in report:
    print(line)

generate_pdf("reports/crop_risk_report.pdf", report)
print("\nPDF Report Generated in /reports folder")
