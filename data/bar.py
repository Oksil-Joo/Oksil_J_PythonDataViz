import matplotlib.pyplot as plt
import numpy as np

x = ['USA', 'CAN', 'NOR', 'URS', 'GER']
gold = [167, 315, 159, 250, 137]
silver = [319, 203, 171, 97, 126]
bronze = [167, 107, 127, 93, 97]

b_bronze = list(np.add(gold,silver))

plt.bar(x, gold, 0.4, label="Gold", color="gold")
plt.bar(x, silver, 0.4, bottom = gold, label = "Silver", color="silver")
plt.bar(x, bronze, 0.4, bottom = b_bronze, label = "Bronze", color="chocolate")

plt.ylabel("Medals")
plt.xlabel("Countries")
plt.title("Gold, Silver, and Bronze Medal Count for The Top 5 Countries", fontweight= 'bold')
plt.legend()
plt.show()