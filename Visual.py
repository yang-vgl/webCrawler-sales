import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Java'
sizes = [215, 130, 245]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.savefig('./public/charts/pie.png', bbox_inches='tight')