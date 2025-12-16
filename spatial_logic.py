import math

# it will mark river coordinates (x, y)
RIVERS = {
    "River_A": (10, 20),
    "River_B": (40, 60),
    "River_C": (70, 30)
}

def nearest_river(drone_pos):
    min_dist = float("inf")
    nearest = None

    for river, pos in RIVERS.items():
        dist = math.dist(drone_pos, pos)
        if dist < min_dist:
            min_dist = dist
            nearest = river

    return nearest, round(min_dist, 2)

# Additional function to assess danger zones colour cordinates hai isme 
def danger_zone(water_level, predicted_level):
    if water_level > 3.5 or predicted_level > 4.0:
        return "🔴 HIGH DANGER ZONE"
    elif water_level > 2.5:
        return "🟠 MEDIUM DANGER ZONE"
    else:
        return "🟢 SAFE ZONE"
def spatial_analysis(water_level):
    if water_level > 80:
        return "HIGH"
    elif water_level > 60:
        return "MODERATE"
    else:
        return "LOW"
def flood_zone_alert(risk_level):
    if risk_level == "HIGH":
        return "🚨 FLOOD ZONE ALERT: Immediate action required!"
    elif risk_level == "MODERATE":
        return "⚠️ Flood Zone Warning: Stay alert."
    else:
        return "✅ Safe Zone: No flood risk detected."
    def spatial_analysis(water_level):
     if water_level > 80:
        return "HIGH"
     elif water_level > 60:
        return "MODERATE"
     else:
        return "LOW"


def zone_mapper(water_level):
    if water_level > 80:
        return "Zone C (Low Land)"
    elif water_level > 60:
        return "Zone B (Mid Land)"
    else:
        return "Zone A (Safe Zone)"
def flood_zone_alert(risk_level):
    if risk_level == "HIGH":
        return "🚨 FLOOD ZONE ALERT: Immediate action required!"
    elif risk_level == "MODERATE":
        return "⚠️ Flood Zone Warning: Stay alert."
    else:
        return "✅ Safe Zone: No flood risk detected."
# spatial_logic.py
def spatial_analysis(level):
    if level > 75:
        return "Flood-prone zone"
    elif level < 30:
        return "Drought-prone zone"
    else:
        return "Safe zone"    
    
    
        
