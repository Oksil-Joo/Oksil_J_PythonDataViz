import matplotlib.pyplot as plt

values = [93, 5, 269, 179, 9, 98]
colors = ['#ff3399', '#cc33ff', '#ff3333', '#ff9933', '#ffff00','#6633ff']
labels = ["Bobsleigh", "Curling", "Ice Hockey", "Skating", "Luge", "Skiing"]

explode = (0, 0, 0.1, 0, 0, 0)

plt.pie(values, labels=labels, startangle=45, counterclock = True, colors=colors, explode=explode, shadow = True)


plt.title("Count of Medals by Sports Event in USA", fontweight= 'bold')

plt.show()