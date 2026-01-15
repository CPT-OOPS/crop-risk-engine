def calculate_risk(rain_dev, temp_dev, yield_dev):
    risk = (abs(rain_dev) * 0.5) + (abs(temp_dev) * 10 * 0.3) + (abs(yield_dev) * 0.2)
    return round(risk, 2)

def risk_level(score):
    if score > 40:
        return "CRITICAL"
    elif score > 25:
        return "HIGH"
    elif score > 15:
        return "MODERATE"
    else:
        return "SAFE"
