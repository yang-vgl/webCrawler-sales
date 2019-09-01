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
labels = [x[1] for x in res]
colors = [x[0] for x in res]
ig, ax = plt.subplots()
#ax.set(title="color preference of bras")
ax.set_title(label='color preference of bras', pad=20)

ax.pie(colors,  labels=labels, colors=labels, autopct='%1.1f%%', shadow=True, startangle=140, pctdistance=1.1, labeldistance=1.2, radius=1)
ax.axis('equal')
plt.savefig('./public/charts/pie.png', bbox_inches='tight')


sql = "select count(*) as num, size_refined from comments GROUP BY size_refined"
mycursor.execute(sql)
res = mycursor.fetchall()
print(res)
x = numpy.arange(4)
print(x)
size_arr = ['A', 'B', 'C', 'D']
sizes = []
for arr in size_arr:
    num = 0
    for x in res:
        if arr == x[1]:
            num = x[0]
            continue
    sizes.append(num)
print(sizes)
fig, ax = plt.subplots()
ax.set_ylabel('number')
ax.set_xlabel('size')
ax.set_title('number of purchased bras by sizes')
ax.bar(size_arr, sizes)
plt.savefig('./public/charts/bar.png', bbox_inches='tight')
