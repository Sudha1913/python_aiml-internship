# ============================================
# WEATHER DATA ANALYSIS
# Using NumPy, Pandas, and Matplotlib
# ============================================

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------
# STEP 1: Create Weather Dataset
# --------------------------------------------

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Temperature": [30, 32, 29, 35, 33, 31, 34],
    "Humidity": [65, 70, 60, 75, 68, 64, 72],
    "Rainfall": [2, 5, 0, 10, 4, 1, 7]
}

df = pd.DataFrame(data)

print("===== WEATHER DATA =====")
print(df)

# --------------------------------------------
# STEP 2: NumPy Calculations
# --------------------------------------------

temp_array = np.array(df["Temperature"])
humidity_array = np.array(df["Humidity"])

print("\n===== WEATHER ANALYSIS =====")

print("Average Temperature:", np.mean(temp_array))
print("Maximum Temperature:", np.max(temp_array))
print("Minimum Temperature:", np.min(temp_array))

print("Average Humidity:", np.mean(humidity_array))

# --------------------------------------------
# STEP 3: Find Hottest Day
# --------------------------------------------

hot_day = df.loc[df["Temperature"].idxmax()]

print("\n===== HOTTEST DAY =====")
print("Day:", hot_day["Day"])
print("Temperature:", hot_day["Temperature"])

# --------------------------------------------
# STEP 4: Line Plot
# --------------------------------------------

plt.plot(df["Day"], df["Temperature"], marker='o')

plt.title("Temperature Changes During Week")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()

# --------------------------------------------
# STEP 5: Bar Chart
# --------------------------------------------

plt.bar(df["Day"], df["Humidity"],
color=["red", "blue", "green", "orange", "purple", "pink", "cyan"])

plt.title("Humidity Levels")
plt.xlabel("Days")
plt.ylabel("Humidity (%)")

plt.show()

# --------------------------------------------
# STEP 6: Pie Chart
# --------------------------------------------

plt.pie(df["Rainfall"],
        labels=df["Day"],
        autopct='%1.1f%%')

plt.title("Rainfall Distribution")

plt.show()

# --------------------------------------------
# STEP 7: Add Weather Condition Column
# --------------------------------------------

conditions = []

for temp in df["Temperature"]:
    if temp >= 34:
        conditions.append("Hot")
    elif temp >= 30:
        conditions.append("Warm")
    else:
        conditions.append("Cool")

df["Condition"] = conditions

print("\n===== FINAL WEATHER REPORT =====")
print(df)

print("\nProgram Executed Successfully!")