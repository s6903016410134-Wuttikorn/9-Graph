import matplotlib.pyplot as plt
import numpy as np

# สุ่มข้อมูลตัวอย่างให้ใกล้เคียงกับภาพมากที่สุด
np.random.seed(42)

# 1. กำหนดขนาดหน้าจอ และ Title หลัก
fig, axs = plt.subplots(3, 3, figsize=(16, 14))
fig.suptitle("My First Chart", fontsize=20, fontweight='bold', y=0.96)

# -------------------------------------------------------------
# Row 1, Col 1: Scatter Plot
# -------------------------------------------------------------
x1 = np.random.randint(0, 100, 100)
y1 = np.random.randint(0, 100, 100)
colors1 = y1
sc1 = axs[0, 0].scatter(x1, y1, c=colors1, cmap='Spectral', s=20)
axs[0, 0].set_title("Scatter Plot", fontsize=10)
axs[0, 0].set_xlabel("X value", fontsize=8)
axs[0, 0].set_ylabel("Y value", fontsize=8)
cbar1 = fig.colorbar(sc1, ax=axs[0, 0], fraction=0.046, pad=0.04)
cbar1.ax.tick_params(labelsize=8)

# -------------------------------------------------------------
# Row 1, Col 2: Bubble Chart
# -------------------------------------------------------------
x2 = np.random.randint(0, 100, 80)
y2 = np.random.randint(0, 100, 80)
sizes2 = np.random.randint(20, 200, 80)
colors2 = np.random.randint(0, 100, 80)
sc2 = axs[0, 1].scatter(x2, y2, s=sizes2, c=colors2, cmap='turbo_r', alpha=0.7)
axs[0, 1].set_title("Bubble Chart", fontsize=10)
axs[0, 1].set_xlabel("X value", fontsize=8)
axs[0, 1].set_ylabel("Y value", fontsize=8)
cbar2 = fig.colorbar(sc2, ax=axs[0, 1], fraction=0.046, pad=0.04)
cbar2.ax.tick_params(labelsize=8)

# -------------------------------------------------------------
# Row 1, Col 3: Horizontal Bar Chart
# -------------------------------------------------------------
categories = ['A', 'B', 'C', 'D']
values = [10, 1, 8, 2]
axs[0, 2].barh(categories, values, color='steelblue')
axs[0, 2].set_title("Horizontal Bar Chart", fontsize=10)
axs[0, 2].set_xlabel("Value", fontsize=8)
axs[0, 2].set_ylabel("Category", fontsize=8)

# -------------------------------------------------------------
# Row 2, Col 1: Sports Match Data
# -------------------------------------------------------------
minutes = np.array([100, 200, 300, 400, 500])
energy = np.array([10, 20, 30, 40, 50])
axs[1, 0].plot(minutes, energy, color='steelblue', label='Energy')
axs[1, 0].set_title("Sports Match Data", fontsize=10)
axs[1, 0].set_xlabel("Minutes", fontsize=8)
axs[1, 0].set_ylabel("Energy", fontsize=8)

# -------------------------------------------------------------
# Row 2, Col 2: Two Line Chart
# -------------------------------------------------------------
x_two = np.array([0, 1, 2, 3, 4])
line1 = np.array([1, 4, 1, 5, 3])
line2 = np.array([1, 3, 5, 1, 6])
axs[1, 1].plot(x_two, line1, color='steelblue', label='Line 1')
axs[1, 1].plot(x_two, line2, color='darkorange', label='Line 2')
axs[1, 1].set_title("Two Line Chart", fontsize=10)
axs[1, 1].set_xlabel("X", fontsize=8)
axs[1, 1].set_ylabel("Y", fontsize=8)
axs[1, 1].legend(fontsize=8, loc='upper left')

# -------------------------------------------------------------
# Row 2, Col 3: Line Chart with Markers
# -------------------------------------------------------------
x_m = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
y_m = np.array([2, 5, 3, 1, 6])
axs[1, 2].plot(x_m, y_m, color='steelblue', zorder=1)
axs[1, 2].scatter(x_m, y_m, color='darkred', s=25, zorder=2, label='Markers')
axs[1, 2].set_title("Line Chart with Markers", fontsize=10)
axs[1, 2].set_xlabel("X", fontsize=8)
axs[1, 2].set_ylabel("Y", fontsize=8)

# -------------------------------------------------------------
# Row 3, Col 1: Histogram
# -------------------------------------------------------------
hist_data = np.random.normal(50, 10, 1000)
axs[2, 0].hist(hist_data, bins=15, color='steelblue', edgecolor='black')
axs[2, 0].set_title("Histogram", fontsize=10)
axs[2, 0].set_xlabel("Value", fontsize=8)
axs[2, 0].set_ylabel("Frequency", fontsize=8)

# -------------------------------------------------------------
# Row 3, Col 2: Pie Chart (Exploded)
# -------------------------------------------------------------
pie_labels = ["Apples", "Bananas", "Cherries", "Dates"]
pie_shares = [35, 25, 20, 20]
pie_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
explode_pie = [0.1, 0, 0, 0]

axs[2, 1].pie(
    pie_shares, 
    labels=pie_labels, 
    explode=explode_pie, 
    colors=pie_colors,
    startangle=90, 
    textprops={'fontsize': 8}
)
axs[2, 1].set_title("Pie Chart (Exploded)", fontsize=10)
axs[2, 1].set_xlabel("Fruit", fontsize=8)
axs[2, 1].set_ylabel("Share (%)", fontsize=8)

# -------------------------------------------------------------
# Row 3, Col 3: Pie Chart (Legend)
# -------------------------------------------------------------
axs[2, 2].pie(
    pie_shares, 
    autopct='%1.0f%%', 
    colors=pie_colors, 
    startangle=90, 
    textprops={'fontsize': 8}
)
axs[2, 2].set_title("Pie Chart (Legend)", fontsize=10)
axs[2, 2].set_xlabel("Fruit", fontsize=8)
axs[2, 2].set_ylabel("Share (%)", fontsize=8)
axs[2, 2].legend(pie_labels, title="Fruit Stuffs", loc="upper right", bbox_to_anchor=(1.35, 1.0), fontsize=7, title_fontsize=8)

# -------------------------------------------------------------
# จัดระเบียบ Spacing ไม่ให้ตัวอักษรชนกัน
# -------------------------------------------------------------
plt.subplots_adjust(
    left=0.06,
    right=0.92,
    top=0.90,
    bottom=0.06,
    wspace=0.40,
    hspace=0.45
)

# แสดงผลกราฟ
plt.show()