import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("web_traffic.csv", parse_dates=["timestamp"])

# Basic Cleanup
df['hour'] = df['timestamp'].dt.hour
df['date'] = df['timestamp'].dt.date

# --- OVERALL KPIs ---
total_sessions = df.shape[0]
total_bounces = df['bounce'].sum()
total_conversions = df['conversion'].sum()
avg_duration = df['duration'].mean()
bounce_rate = round((total_bounces / total_sessions) * 100, 2)
conversion_rate = round((total_conversions / total_sessions) * 100, 2)

print("\n===== 📊 OVERALL SUMMARY =====")
print(f"Total Sessions        : {total_sessions}")
print(f"Total Bounces         : {total_bounces} ({bounce_rate}%)")
print(f"Total Conversions     : {total_conversions} ({conversion_rate}%)")
print(f"Avg Session Duration  : {round(avg_duration, 2)} seconds")
print("=================================\n")

# --- Bounce Rate by Source ---
print("🔎 Bounce Rate by Source:")
print((df.groupby("source")["bounce"].mean() * 100).round(2).sort_values(), "\n")

# --- Conversion Rate by Device ---
print("🧠 Conversion Rate by Device:")
print((df.groupby("device")["conversion"].mean() * 100).round(2).sort_values(), "\n")

# --- Traffic by Device Type ---
device_share = df['device'].value_counts(normalize=True) * 100
print("📱 Device Traffic Share:")
print(device_share.round(2), "\n")

# --- Most Visited Pages ---
print("📋 Top Visited Pages:")
print(df['page'].value_counts().head(10), "\n")

# --- Peak Hour of Traffic ---
print("⏰ Peak Traffic Hour:")
print(df['hour'].value_counts().sort_values(ascending=False).head(3), "\n")

# === VISUALIZATIONS ===

# Bounce Rate by Source
df.groupby("source")["bounce"].mean().sort_values().mul(100).plot(kind="bar", color="coral")
plt.title("Bounce Rate by Source")
plt.ylabel("Bounce Rate (%)")
plt.tight_layout()
plt.show()

# Conversion Rate by Device
df.groupby("device")["conversion"].mean().sort_values().mul(100).plot(kind="bar", color="mediumseagreen")
plt.title("Conversion Rate by Device")
plt.ylabel("Conversion Rate (%)")
plt.tight_layout()
plt.show()

# Session Duration Histogram
plt.hist(df["duration"], bins=50, color="skyblue", edgecolor="black")
plt.title("Session Duration Distribution")
plt.xlabel("Duration (seconds)")
plt.ylabel("Sessions")
plt.tight_layout()
plt.show()

# Most Visited Pages
df['page'].value_counts().plot(kind="bar", color="steelblue")
plt.title("Most Visited Pages")
plt.ylabel("Session Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Conversion Funnel Drop-off
funnel_pages = ["/cart", "/checkout", "/thankyou"]
df[df["page"].isin(funnel_pages)]["page"].value_counts().reindex(funnel_pages).plot(kind="bar", color="orchid")
plt.title("Funnel Drop-off: Cart ➝ Checkout ➝ Thankyou")
plt.ylabel("Sessions")
plt.tight_layout()
plt.show()

# Bounce Rate by Page
df.groupby("page")["bounce"].mean().mul(100).sort_values().plot(kind="barh", color="darkorange")
plt.title("Bounce Rate by Page")
plt.xlabel("Bounce Rate (%)")
plt.tight_layout()
plt.show()

# Traffic Trend by Day
df.groupby("date")["session_id"].count().plot(figsize=(10, 4), title="Daily Sessions Over Time")
plt.ylabel("Session Count")
plt.xlabel("Date")
plt.tight_layout()
plt.show()

# Heatmap: Hour vs Source
heatmap_data = df.groupby(["hour", "source"]).size().unstack().fillna(0)
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=False)
plt.title("Traffic by Hour & Source")
plt.ylabel("Hour of Day")
plt.tight_layout()
plt.show()

# Pie Chart: Device Share
df['device'].value_counts().plot(kind="pie", autopct='%1.1f%%', colors=["gold", "lightblue", "lightgreen"])
plt.title("Device Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()
