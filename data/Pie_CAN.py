import matplotlib.pyplot as plt

values = [22, 50, 351, 159, 3, 40]
colors = ['#ff3399', '#cc33ff', '#ff3333', '#ff9933', '#ccff33','#6633ff']
labels = ["Bobsleigh", "Curling", "Ice Hockey", "Skating", "Biathlon", "Skiing"]

explode = (0, 0, 0.1, 0, 0, 0)

plt.pie(values, labels=labels, startangle=45, counterclock = True, colors=colors, explode=explode, shadow = True)


plt.title("Count of Medals by Sports Event in Canada", fontweight= 'bold')

plt.show()