import mysql.connector

color_cn = ['红', '橙', '黄', '绿', '青', '蓝', '紫', '粉', '肤', '黑', '灰', '白']
color_eng = ['red', 'orange', 'yellow', 'green', 'green', 'blue', 'purple', 'pink', 'pink', 'black', 'grey', 'white']
sizes = ['A', 'B', 'C', 'D', 'M', 'L', 'X']

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="web_crawler"
)

mycursor = mydb.cursor()

sql = "select * from comments"
mycursor.execute(sql)
res = mycursor.fetchall()

for val in res:

    # refined size
    s = list(val[1])
    for size in s:
        try:
            value = ''
            if size in sizes:
                value = size
            else:
                continue
            sql = "UPDATE comments SET size_refined = %s WHERE id = %s"
            if value == 'M':
                value = 'A'
            if value == 'L':
                value = 'B'
            if value == 'X':
                value = 'C'
            print(value)
            str = (value, val[0])
            mycursor.execute(sql, str)
            mydb.commit()
            break
        except Exception as e:
            print(e)

    # refined color
    l = list(val[2])
    for color in l:
        try:
            index = color_cn.index(color)
            print(color_eng[index])
            sql = "UPDATE comments SET color_refined = %s WHERE id = %s"
            str_color = (color_eng[index], val[0])
            mycursor.execute(sql, str_color)
            mydb.commit()
            break
        except Exception as e:
            print(e)


