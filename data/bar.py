import matplotlib.pyplot as plt
import numpy as np

x = ['AUT', 'CAN', 'FIN', 'GER', 'NOR', 'RUS', 'SUI', 'SWE', 'URS', 'USA']
gold = [79, 315, 66, 137, 159, 94, 76, 127, 250, 167]
silver = [98, 203, 147, 126, 171, 90, 77, 129, 97, 319]
bronze = [103, 107, 221, 97, 127, 79, 132, 177, 93, 167]

b_bronze = list(np.add(gold,silver))

plt.bar(x, gold, 0.4, label="Gold", color="gold")
plt.bar(x, silver, 0.4, bottom = gold, label = "Silver", color="silver")
plt.bar(x, bronze, 0.4, bottom = b_bronze, label = "Bronze", color="chocolate")

plt.ylabel("Medals")
plt.xlabel("Countries")
plt.title("Gold, Silver, and Bronze Medal Count for The Top 10 Countries", fontweight= 'bold')
plt.legend()
plt.show()