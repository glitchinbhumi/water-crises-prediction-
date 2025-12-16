# farmer_logic.py

def send_farmer_alert(message):
    print("🌾 FARMER ALERT SYSTEM")
    print(f"📢 MESSAGE: {message}")
    print("✅ Alert sent successfully\n")
def send_farmer_alert(risk):
    if risk == "HIGH":
        print("📢 ALERT SENT TO FARMERS: Flood risk detected!")
    elif risk == "MEDIUM":
        print("⚠️ Warning sent: Monitor water levels.")
    else:
        print("✅ No alert needed.")
