def detect_water_state(d):
    if d["water_level"] > 2.2 and d["rainfall"] > 25:
        return "AGGRESSIVE_FLOOD"

    if d["oxygen"] < 4.5 and d["temperature"] > 30:
        return "FISH_STRESS"

    if d["ph"] < 6.2 or d["turbidity"] > 70:
        return "POLLUTED"

    return "NORMAL"
