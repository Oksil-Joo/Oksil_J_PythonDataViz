import matplotlib.pyplot as plt
import numpy as np

N = 2
gold = [139, 36] 
silver = [76, 120] 
bronze = [35, 11] 

ind = np.arange(N) 
width = 0.2      
plt.bar(ind - width, gold, width, label='Gold', color ='gold')
plt.bar(ind, silver, width, label='Silver', color ='silver')
plt.bar(ind + width, bronze, width, label='Bronze', color ='chocolate')

plt.ylabel("Medals")
plt.xlabel("Countries")
plt.title("CAN vs USA Men's Ice Hockey Medal Count", fontweight = 'bold')

plt.xticks(ind + width / 3, ('CAN', 'USA'))
plt.legend(loc='best')
plt.show()