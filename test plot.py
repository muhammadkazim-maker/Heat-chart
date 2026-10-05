# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.title("Test Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.show()
# import matplotlib.pyplot as plt
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# plt.plot(x,y)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Test Plot')
# plt.show()
# plt.savefig('plot1.png')
# import matplotlib.pyplot as plt
# x= [1,2,3,4]
# y=[10,20,15,25]
# plt.plot(x,y)
# plt.title("my first graph")
# plt.show()
# import matplotlib.pyplot as plt

# x= ["mon","Tue","Wed","Thur","Fri"]
# y=[10,15,7,20,12]

# plt.plot(x,y)
# plt.title("The report of salings")
# plt.xlabel("The days of week")
# plt.ylabel("Sales per day ")
# plt.show()
# months = [1,2,3,4]
# sales = [1200,2344,1234,2156]
# plt.plot(months,sales,color = "red", linestyle = "--", linewidth = 3, marker = "o" ,label = "2025 sales data")
# plt.xlabel("months")
# plt.ylabel("sales per month")
# plt.title("monthly sales data reports")
# plt.legend(loc = "upper left",fontsize = 12)
# plt.grid(color = "gray",linestyle = ":",linewidth = 1)
# plt.xlim(1,4)
# plt.ylim(0,2500)
# plt.xticks([1,2,3,4],["M1","M2","M3","M4"])
# import matplotlib.pyplot as plt
# plt.show()
# days = [1, 2, 3, 4, 5, 6, 7]
# temp = [22, 25, 21, 24, 28, 27, 26]
# plt.plot(days,temp,color = "green",linestyle="-.",linewidth=2,marker="s",label="daily temp")
# plt.title("daily tempreture track")
# plt.xlabel("day")
# plt.ylabel("Tempreture (c)")
# plt.xticks([1,2,3,4,5,6,7],["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
# plt.legend(loc="upper left")
# plt.grid(color="gray")
# plt.show()
# months = [1, 2, 3, 4]

# sales_2024 = [1000, 1500, 1100, 1800]

# sales_2025 = [1200, 2344, 1234, 2156]
# plt.plot(months ,sales_2024, color= 'blue',linestyle = ":",marker = "o",label = "2024")
# plt.plot(months ,sales_2025, color= 'red',linestyle = "--",marker = "^",label = "2025")
# plt.ylim(500,2500)
# plt.xticks([1,2,3,4],["jan","feb","mar","apr"])
# plt.title("Year-over-Year Sales Comparison")
# plt.legend()
# plt.show()
# hours = [0, 2, 4, 6, 8, 10]

# battery = [100, 85, 65, 40, 20, 5]
# plt.plot(hours,battery,color="purple",linewidth = 2.5 ,marker = "D")
# plt.xlim(0,12)
# plt.ylim(0,100)
# plt.yticks(battery,[0, 20, 40, 60, 80, 100])
# plt.xlabel("hours used ")
# plt.ylabel("battery percentage (%)")
# plt.grid(color="gray",linestyle = ("--"))
# plt.show()\
import matplotlib.pyplot as plt

# hours = [0, 2, 4, 6, 8, 10]
# battery = [100, 85, 65, 40, 20, 5]

# plt.plot(
#     hours,
#     battery,
#     color="purple",
#     marker="D",
#     linewidth=2.5,
#     label="Battery Life",
# )
# plt.xlabel("hours used")
# plt.ylabel("battery percentage (%)")

# plt.xlim(0, 12)
# plt.ylim(0, 100)  # Corrected range
# plt.yticks([0, 20, 40, 60, 80, 100])  # Explicit ticks from 0 to 100

# plt.grid(color="gray", linestyle="--", alpha=0.7)
# plt.show()
# import matplotlib.pyplot as plt

# weeks = [1, 2, 3, 4, 5]
# weight_loss = [80, 79.2, 78.5, 78.0, 77.1]

# plt.plot(
#     weeks,
#     weight_loss,
#     color="cyan",
#     marker="o",
#     markersize=8,
#     markerfacecolor="yellow",
#     markeredgecolor="black",
#     label="Weight Progress",
# )

# plt.xlabel("Weeks")
# plt.ylabel("Weight (kg)")
# plt.title("5-Week Fitness Progress")

# plt.xticks(weeks, ["W1", "W2", "W3", "W4", "W5"])
# plt.legend()
# plt.grid(color="gray", linestyle=":", alpha=0.6)

# plt.show()
# import matplotlib.pyplot as plt
# product = ["A","B","C","D"]
# sales =[ 1000,1500,800,1200]
# plt.bar(product,sales ,color = "orange",label= "2025 sales ")
# plt.xlabel("products")
# plt.ylabel("sales")
# plt.title("sales report for product of 2025")
# plt.legend()
# plt.show()
# product = ["A","B","C","D"]
# sales =[ 1000,1500,800,1200]
# plt.barh(product,sales ,color = "orange",label= "2025 sales ")
# plt.xlabel("products")
# plt.ylabel("sales")
# plt.title("sales report for product of 2025")
# plt.legend()
# plt.show()
# regions = ["North","South","East","West"]
# revenue = [3000,2000,1500,1000]
# plt.pie(revenue,labels=regions,autopct="%1.1f%%",colors = ["red","lightgreen","lightblue","gold"])
# plt.title("revenue contribution by region")
# plt.show()
# import matplotlib.pyplot as plt
# scores= [12,34,5,63,56,43,56,78,90,79,87,67,58,67,84,65]
# plt.hist(scores,bins = 5,color="skyblue",edgecolor= "red",)
# plt.xlabel("score reange")
# plt.ylabel("num of students")
# plt.title("score distribution of students")
# plt.show()
# import matplotlib.pyplot as plt
# hours_studied=(1,2,3,4,5,6,7,8)
# exam_scores=(50,55,60,65,70,75,80,85)
# plt.scatter(hours_studied,exam_scores,color = "green",marker="o",label ="student data")
# plt.xlabel("hours studied")
# plt.ylabel("exam scores")
# plt.title("relationship between study time and scores")
# plt.legend()
# plt.grid(True)
# plt.show()
# import matplotlib.pyplot as plt
# plt.scatter ([1,2,3],[45,67,55],color = "red",label = "class 1",marker="o")
# plt.scatter ([1,2,3],[34,66,54],color = "darkblue",label = "class 2",marker="o")

# plt.xlabel("hours studied")
# plt.ylabel("exam scores")
# plt.title("relationship between study time and scores between two clases")
# plt.legend(loc = "upper left")
# plt.grid(True)
# plt.show()
# import matplotlib.pyplot as plt
# x=[1,2,3,4]
# y=[23,55,58,89]
# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title("line graph")

# plt.subplot(1,2,2)
# plt.bar(x,y,color="orange")
# plt.title("bar graph")
# plt.show()
# import matplotlib.pyplot as plt
# fig,ax=plt.subplots(1,2,figsize=(10,5))
# x=[1,2,3,4]
# y=[23,55,58,89]
# ax[0].plot(x,y)
# ax[0].set_title("line plot")

# ax[1].bar(x,y)
# ax[1].set_title("bar chart")
# plt.tight_layout(
# )
# plt.savefig("plots comparison.png",dpi=300,bbox_inches="tight")
# plt.show()
# import matplotlib.pyplot as plt

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# expenses = [1200, 1350, 1100, 1500, 1250, 1400]
# savings = [400, 300, 600, 200, 500, 450]
# fig,ax=plt.subplots(figsize = (8,5))
# ax.plot(months,expenses,marker=("o"),label="expenses per months",color="red")
# ax.plot(months,savings,marker="s",color="green",label="savings per months")
# ax.spines["top"].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.set_xlabel("months")
# ax.set_ylabel("monthly saving and expenses ratio")
# ax.grid(linestyle=(":"),alpha=0.5)
# ax.legend(loc="upper left")
# plt.tight_layout()
# plt.savefig("my basic to advance first graph.pdf",dpi=300,bbox_inches="tight")
# plt.show()
# import matplotlib.pyplot as plt
# num_of_seconds=[0,1,2,3,4,5,6,7,8,9]
# speed_in_mph=[119.9,128.6,137.3,146.0,154.7,163.4,172.1,180.8,189.5,198.2]
# fig,ax=plt.subplots(figsize=(5,10))
# ax.plot(num_of_seconds,speed_in_mph,color="pink",marker="s",label="speed in mph")
# ax.set_xlabel("number in seconds")
# ax.set_ylabel("speed(mph)")
# ax.set_ylim(0,250)
# ax.set_xlim(0,10)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# plt.tight_layout()

# plt.show()
# import matplotlib.pyplot as plt

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# expenses = [1200, 1350, 1100, 1500, 1250, 1400]
# savings = [400, 300, 600, 200, 500, 450]
# import matplotlib.pyplot as plt

# fig, ax1 = plt.subplots(figsize=(8, 5))

# # Pehla metric (Left Y-Axis)
# ax1.plot(months, expenses, color='red', label='Expenses ($)')
# ax1.set_ylabel('Expenses in USD', color='red')
# ax1.tick_params(axis='y', labelcolor='red')

# # Doosra Y-Axis create karein
# ax2 = ax1.twinx()

# # Doosra metric (Right Y-Axis)
# ax2.plot(months, savings, color='blue', label='Savings Rate (%)')
# ax2.set_ylabel('Savings Rate (%)', color='blue')
# ax2.tick_params(axis='y', labelcolor='blue')
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt

# quarters = ['Q1', 'Q2', 'Q3', 'Q4']
# revenue = [45000, 62000, 58000, 71000]          # Values in USD ($)
# profit_margin = [12.5, 18.2, 15.0, 22.4]     #this is value in percentagea
# fig,ax1=plt.subplots(figsize=(9,5))
# ax1.bar(quarters,revenue,color="#13c922",width=0.4)
# ax1.set_ylabel("revenue ($)",color="green")
# ax1.spines["top"].set_visible(False)
# ax1.tick_params(axis="y",labelcolor="blue")

# ax2=ax1.twinx()
# ax2.plot(quarters,profit_margin,marker="o",color="#2c5aa0",linewidth=2.5)
# ax2.set_ylabel("profit margin (%)",color="green")
# ax2.spines["top"].set_visible(False)
# ax2.tick_params(axis="y",labelcolor="green")

# plt.title("Quarterly Revenue vs Profit Margin")
# plt.show()


# import matplotlib.pyplot as plt

# quarters = ['Q1', 'Q2', 'Q3', 'Q4']
# sales_hardware = [30, 45, 40, 60]      # Values in $k
# sales_software = [20, 25, 35, 50]      # Values in $k
# operating_cost = [15, 18, 16, 22]      # Values in $k
# satisfaction = [78, 82, 85, 89]         # Customer CSAT %

# fig,ax=plt.subplots(2,2,figsize=(12,8))
# ax[0,0].plot(quarters,sales_hardware,color="red",)
# ax[0,0].set_ylabel("sales hardware in ($)", color="darkblue",fontweight="bold")
# ax[0,0].set_xlabel("quarters",color="purple")
# ax[0,0].set_title("quateres and sales",color="blue")
# ax[0,0].tick_params(axis="y",labelcolor="red")
# ax[0,0].grid(color="grey",alpha=0.4)



# ax[0,1].bar(quarters,sales_software,color="pink")
# ax[0,1].set_xlabel("quarters")
# ax[0,1].set_ylabel("sales of software in ($)")
# ax[0,1].set_title("sales of software")
# ax[0,1].grid(color="grey",alpha=0.4)
# ax[0,1].tick_params(axis="y",labelcolor="red")



# ax[1,0].scatter(quarters,operating_cost,color="orange")
# ax[1,0].set_xlabel("quarters")
# ax[1,0].set_ylabel("operating cost in ($)")
# ax[1,0].set_title("operating cost")
# ax[1,0].grid(color="grey",alpha=0.4)
# ax[1,0].tick_params(axis="y",labelcolor="red")



# ax[1,1].plot(quarters,satisfaction,marker="o",color="green")
# ax[1,1].set_xlabel("quarters")
# ax[1,1].set_ylabel("customer csat in (%)")
# ax[1,1].set_title("satisfaction")
# ax[1,1].grid(color="grey",alpha=0.4)
# ax[1,1].tick_params(axis="y",labelcolor="red")


# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# sales = [150, 200, 180, 300, 280, 400]
# visitors = [1000, 1200, 1100, 1800, 1600, 2200]
# conversion_rate = [15, 16.6, 16.3, 16.6, 17.5, 18.1]

# # Layout Setup
# fig = plt.figure(figsize=(11, 7))
# gs = fig.add_gridspec(2, 2)

# # Subplots Defining
# ax1 = fig.add_subplot(gs[0, :])  # Top full row
# ax2 = fig.add_subplot(gs[1, 0])  # Bottom left
# ax3 = fig.add_subplot(gs[1, 1])  # Bottom right

# # 1. Top Chart - Sales
# ax1.plot(months, sales, color='blue', marker='o')
# ax1.set_title('Monthly Sales Trend ($k)')
# ax1.grid(True, linestyle=':', alpha=0.5)

# # Annotation for Peak Sales in Top Chart
# ax1.annotate(
#     'Highest Revenue',
#     xy=('Jun', 400),
#     xytext=('Apr', 300),
#     arrowprops=dict(facecolor='red', shrink=8),
# )

# # 2. Bottom Left - Visitors Bar Chart
# ax2.bar(months, visitors, color='orange')
# ax2.set_title('Website Visitors')
# ax2.grid(True, linestyle=':', alpha=0.5)

# # 3. Bottom Right - Conversion Rate Line Chart
# ax3.plot(months, conversion_rate, color='green', marker='s')
# ax3.set_title('Conversion Rate (%)')
# ax3.grid(True, linestyle=':', alpha=0.5)

# plt.tight_layout()
# plt.show()



# 


# import matplotlib.pyplot as plt
# import numpy as np

# # Data Setup
# footfall_data = np.array([
#     [120, 150, 140, 160, 200, 350, 300],
#     [250, 280, 260, 300, 420, 600, 550],
#     [300, 320, 310, 380, 500, 750, 700],
#     [100, 110, 105, 130, 220, 400, 380],
# ])

# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# time_slots = ['Morning', 'Afternoon', 'Evening', 'Night']

# # 1. Figure aur Axes setup
# fig, ax = plt.subplots(figsize=(10, 5))

# # 2. Heatmap Render
# cax = ax.imshow(footfall_data, cmap='YlOrRd', aspect='auto')

# # 3. Colorbar Side Legend
# fig.colorbar(cax, ax=ax, label='Customer Count')

# # 4. Custom Labels for Axes
# ax.set_xticks(range(len(days)))
# ax.set_xticklabels(days)
# ax.set_yticks(range(len(time_slots)))
# ax.set_yticklabels(time_slots)

# # 5. Write values inside boxes
# for i in range(len(time_slots)):
#   for j in range(len(days)):
#     ax.text(
#         j,
#         i,
#         str(footfall_data[i, j]),
#         ha='center',
#         va='center',
#         color='black',
#         fontsize=9,
#     )

# ax.set_title('Customer Footfall Heatmap by Time & Day', fontweight='bold')
# plt.tight_layout()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Rows: Time Intervals (4 slots)
# Columns: Days of Week (Monday to Sunday)
sales_matrix = np.array([
    [ 45,  50,  55,  60,  85, 120, 110],  # Morning (8 AM - 12 PM)
    [ 90,  95, 100, 110, 150, 210, 195],  # Afternoon (12 PM - 4 PM)
    [130, 140, 135, 160, 240, 320, 290],  # Evening (4 PM - 8 PM)
    [ 60,  65,  70,  80, 110, 180, 160]   # Night (8 PM - 12 AM)
])

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
time_slots = ['Morning', 'Afternoon', 'Evening', 'Night']

fig,ax= plt.subplots(figsize=(10,5))

cmx = ax.imshow(sales_matrix,cmap='YlGn',aspect="auto")
fig.colorbar(cmx,ax=ax,label="Total Orders")

ax.set_xticks(range(len(days)))
ax.set_xticklabels(days)
ax.set_yticks(range(len(time_slots)))
ax.set_yticklabels(time_slots)

for i in range(len(time_slots)):
    for j in range(len(days)):
        val = sales_matrix[i,j]
        text_color= "white" if val >200 else "black"
        

        ax.text(
            j,
            i,
            str(val),
            ha="center",
            va="center",
            color = text_color,
            fontsize=20
            
            )


ax.set_title("Peak Sales Activity Heatmap",fontweight="bold",color="red")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()
