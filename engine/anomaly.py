def rainfall_deviation(series):
    baseline = series[:-1].mean()
    current = series.iloc[-1]
    return round(((current - baseline) / baseline) * 100, 2)

def temperature_stress(series):
    baseline = series[:-1].mean()
    current = series.iloc[-1]
    return round(current - baseline, 2)

def yield_drop(series):
    baseline = series[:-1].mean()
    current = series.iloc[-1]
    return round(((current - baseline) / baseline) * 100, 2)
