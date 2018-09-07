import pymysql
connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='12345',db='student',charset='utf8')
cursor=connection.cursor()

# 查询表course中的所有记录
sql1='SELECT * FROM course'
rowNums=cursor.execute(sql1)
print('查询的行数为'+str(rowNums))

# 查询表course中courseNum,courseName,credit,grade的字段信息
sql2="SELECT courseNum,courseName,credit,grade FROM course"
cursor.execute(sql2)

# 获取查询的第一条记录
row_1=cursor.fetchone()
print("查询的第一条记录为："+str(row_1))

# 获取查询的前三条记录
row_2=cursor.fetchmany(3)
print("查询的前三条记录为："+str(row_2))

# 获取查询的所有记录
resultlist=cursor.fetchall()
print("查询的所有记录为：")
for i in range(len(resultlist)):
    print(resultlist[i])

# 查询课程名为工程力学的记录
sql3="SELECT * FROM course WHERE courseName='工程力学'"
cursor.execute(sql3)
resultlist=cursor.fetchall()
print("工程力学课程信息为：")
for i in range(len(resultlist)):
    print(resultlist[i])

# 查询课程工程力学的分数
sql4="SELECT grade FROM course WHERE courseName='工程力学'"
cursor.execute(sql4)
resultlist=cursor.fetchone()
print('工程力学的成绩为'+str(resultlist[0]))

# 查询返回字典类型
cursor=connection.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM course")
resultlist=cursor.fetchall()
for i in range(len(resultlist)):
    print(resultlist[i])

connection.commit()
cursor.close()
connection.close()
