import matplotlib.pyplot as plt
import mysql.connector
import numpy



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="web_crawler"
)

mycursor = mydb.cursor()
sql = "select count(*) as num, color_refined from comments GROUP BY color_refined"
mycursor.execute(sql)
res = mycursor.fetchall()
print(res)
print([x[0] for x in res])

labels = [x[1] for x in res]
sizes = [x[0] for x in res]
colors = labels
plt.pie(sizes,  labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.savefig('./public/charts/pie.png', bbox_inches='tight')


sql = "select count(*) as num, size_refined from comments GROUP BY size_refined"
mycursor.execute(sql)
res = mycursor.fetchall()
print(res)
x = numpy.arange(3)
sizes = [x[0] for x in res]



fig, ax = plt.subplots()
plt.bar(x, sizes)
plt.xticks(x, ([x[1] for x in res]))
plt.savefig('./public/charts/bar.png', bbox_inches='tight')
