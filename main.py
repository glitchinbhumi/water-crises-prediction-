import time
import csv
import matplotlib.pyplot as plt

from sensor_simulator import get_sensor_data
from risck_prediction import predict_water_level
from spatial_logic import spatial_analysis, zone_mapper
from ai_logic import assess_risk, system_decision
from drone_logic import drone_decision
from cloud_seeding import cloud_seeding_decision
from farmer_logic import send_farmer_alert

# -------------------------------
# Setup
# -------------------------------

# Real-time history
water_levels = []
timestamps = []

# CSV file for logging
CSV_FILE = "data/live_water_data.csv"

# create csv header once
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "Water Level", "Rainfall", "Area Risk", "AI Risk", "Decision"])

# Setup interactive plot
plt.ion()
fig, ax = plt.subplots()

print("\n===== SMART WATER & CLIMATE AI SYSTEM STARTED =====")

# -------------------------------
# Main Loop
# -------------------------------
while True:
    try:
        # 1️⃣ Sensor Data
        data = get_sensor_data()
        level = data["water_level"]
        rainfall = data["rainfall"]

        # 2️⃣ Prediction
        predicted_level = predict_water_level([level])

        # 3️⃣ Spatial Analysis
        area_risk = spatial_analysis(level)
        zone = zone_mapper(level)

        # 4️⃣ AI Risk Assessment
        ai_risk = assess_risk(level, rainfall)
        decision = system_decision(ai_risk)

        # 5️⃣ Drone & Cloud Actions
        drone_action = drone_decision(ai_risk)
        cloud_action = cloud_seeding_decision(area_risk)

        # 6️⃣ Farmer Alert
        if area_risk == "HIGH":
            send_farmer_alert("Flood Risk Detected!")

        # 7️⃣ Save Data to CSV
        timestamp = time.strftime("%H:%M:%S")
        timestamps.append(timestamp)
        water_levels.append(level)
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, level, rainfall, area_risk, ai_risk, decision])

        # 8️⃣ Real-Time Graph
        ax.clear()
        ax.plot(timestamps, water_levels, marker='o', linestyle='-', color='b')
        ax.set_title("Real-Time Water Level (AI Enabled)")
        ax.set_xlabel("Time")
        ax.set_ylabel("Water Level")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(0.1)

        # 9️⃣ Print Status
        print("\n========== SYSTEM STATUS ==========")
        print(f"Time          : {timestamp}")
        print(f"Zone          : {zone}")
        print(f"Water Level   : {level}")
        print(f"Rainfall      : {rainfall}")
        print(f"Predicted     : {predicted_level}")
        print(f"Area Risk     : {area_risk}")
        print(f"AI Risk       : {ai_risk}")
        print(f"Decision      : {decision}")
        print(f"Drone Action  : {drone_action}")
        print(f"Cloud Action  : {cloud_action}")

        # 10️⃣ Loop Delay
        time.sleep(3)

    except KeyboardInterrupt:
        print("\nSystem stopped by user.")
        break
    except Exception as e:
        print(f"\n[ERROR] {e}")
        time.sleep(3)



