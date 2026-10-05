# import numpy as np
# import matplotlib.pyplot as plt

# # Rows: Time Slots (6 slots in a day)
# # Columns: Days of Week (Mon - Sun)
# traffic_data = np.array([
#     [ 200,  180,  220,  210,  300,  500,  450],  # 12 AM - 4 AM
#     [ 150,  130,  140,  160,  200,  300,  280],  # 4 AM - 8 AM
#     [ 850,  900,  880,  920, 1100,  800,  750],  # 8 AM - 12 PM
#     [1200, 1250, 1180, 1300, 1600, 1400, 1350],  # 12 PM - 4 PM
#     [1500, 1600, 1550, 1700, 2100, 2400, 2200],  # 4 PM - 8 PM (Peak Hours)
#     [ 950,  980, 1020, 1100, 1800, 2000, 1750]   # 8 PM - 12 AM
# ])

# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# time_slots = ['12AM-4AM', '4AM-8AM', '8AM-12PM', '12PM-4PM', '4PM-8PM', '8PM-12AM']

# fig, ax = plt.subplots(figsize=(10, 6))

# cmx = ax.imshow(traffic_data, cmap="coolwarm", aspect="auto")

# cbar = fig.colorbar(cmx, ax=ax, label="Active Users (in Thousands)")
# cbar.ax.tick_params(labelsize=10)

# ax.set_xticks(range(len(days)))
# ax.set_xticklabels(days, fontsize=11, fontweight="bold")
# ax.set_yticks(range(len(time_slots)))
# ax.set_yticklabels(time_slots, fontsize=11)

# # Dynamic text color threshold (raised to 1800 for dark red backgrounds)
# norm = plt.Normalize(traffic_data.min(), traffic_data.max())

# for i in range(len(time_slots)):
#     for j in range(len(days)):
#         val = traffic_data[i, j]
        
#         # White text for dark/high values, black text for lighter background cells
#         text_color = "white" if val >= 1800 else "black"
#         text_weight = "bold" if val >= 1800 else "normal"
        
#         ax.text(
#             j, i, str(val),
#             ha="center",
#             va="center",
#             color=text_color,
#             fontweight=text_weight,
#             fontsize=12
#         )

# ax.set_title("E-Commerce Mobile App Hourly Traffic and Conversion", fontsize=14, color="navy", fontweight="bold", pad=15)

# # Remove all outer frame spines for a cleaner aesthetic
# for spine in ax.spines.values():
#     spine.set_visible(False)

# plt.tight_layout()
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

traffic_data = np.array([
    [ 200,  180,  220,  210,  300,  500,  450],
    [ 150,  130,  140,  160,  200,  300,  280],
    [ 850,  900,  880,  920, 1100,  800,  750]
])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# 1. Title Touching the Heatmap
ax1.imshow(traffic_data, cmap="coolwarm", aspect="auto")
ax1.set_title("pad = 0 (Touching Border)", pad=0, color="red", fontweight="bold")

# 2. Title Separated by Padding
ax2.imshow(traffic_data, cmap="coolwarm", aspect="auto")
ax2.set_title("pad = 30 (Pushed Up)", pad=30, color="green", fontweight="bold")

plt.tight_layout()
plt.show()