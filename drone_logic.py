def drone_decision(mode):
    if mode == "DISASTER_MODE":
        return "Launch drone for flood mapping"
    if mode == "AGRICULTURE_MODE":
        return "Trace pollution source upstream"
    if mode == "FISHERIES_MODE":
        return "Survey water surface"
    return "Drone idle"
    time.sleep(2)
def drone_action(risk_level, water_level, turbidity):
    """
    Decides drone mission based on AI output
    """

    if risk_level == "HIGH":
        return {
            "deploy": True,
            "mission": "🚁 AERIAL FLOOD SURVEY + EMERGENCY ALERT",
            "altitude": "LOW",
            "return": "AUTO"
        }

    elif turbidity > 80:
        return {
            "deploy": True,
            "mission": "☣️ WATER POLLUTION SCAN + AREA MARKING",
            "altitude": "MEDIUM",
            "return": "AUTO"
        }

    elif water_level > 3.0:
        return {
            "deploy": True,
            "mission": "🌧️ RIVER OVERFLOW MONITORING",
            "altitude": "HIGH",
            "return": "AUTO"
        }

    else:
        return {
            "deploy": False,
            "mission": "🛑 NO FLIGHT REQUIRED",
            "altitude": None,
            "return": None
        }
def drone_decision(risk):
    if risk == "CRITICAL":
        return "Drone Deployed for Surveillance"
    elif risk == "WARNING":
        return "Drone on Standby"
    else:
        return "No Drone Required"        
