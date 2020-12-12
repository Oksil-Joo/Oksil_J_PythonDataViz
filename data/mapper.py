import matplotlib.pyplot as plt

countries = ['AUT', 'CAN', 'FIN', 'GER', 'NOR', 'RUS', 'SUI', 'SWE', 'URS', 'USA']

pops = [280, 625, 434, 360, 457, 263, 285, 433, 440, 653]

plt.plot(countries, pops, color=('deepskyblue'), linewidth=3.0, marker = 'o', markerfacecolor='blue', markersize=12)
plt.title("Total Medals Count for Top 10 Countries", fontweight= 'bold')
plt.ylabel("Medals")
plt.xlabel("Countries")
plt.grid(True)
plt.show()
