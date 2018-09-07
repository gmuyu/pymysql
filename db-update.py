import pymysql
connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='12345',db='student',charset='utf8')
cursor=connection.cursor()

# 在表StudentInfo中插入学生信息
cursor.execute("INSERT INTO StudentInfo(Name) VALUES('张三')")
cursor.execute("INSERT INTO StudentInfo(Name) VALUES('李四')")

# 查询表StudentInfo中记录
rowNums=cursor.execute("SELECT * FROM StudentInfo")
print("查询的行数为"+str(rowNums))

# 批量插入学生信息
sql1='INSERT INTO StudentInfo(Id,Name) VALUES(%s,%s)'
insertRow=cursor.executemany(sql1,[(7,'gmy'),(8,'byw')])
print('插入的行数为'+str(insertRow))

# 获取新创数据自增id
lastInsertId=cursor.lastrowid
print("插入的最后一条记录id为"+str(lastInsertId))

# 批量插入用户信息到user表
sql2="INSERT INTO user(userName,password) VALUES(%s,%s)"
insertRow=cursor.executemany(sql2,[("admin","12345"),("user1","111222"),("user2","222222")])
cursor.execute("SELECT * FROM user")
result=cursor.fetchall()
print("用户名和密码为：")
for i in range(len(result)):
    print(result[i])

# 更新表StudentInfo中的学生信息
sql3='UPDATE StudentInfo SET Name =%s WHERE Id =%s'
updateRow=cursor.execute(sql3,('gsr','5'))
print('更新的行数为'+str(updateRow))

# 批量更新course表中课程分数
sql4="UPDATE course SET grade=%s WHERE grade=%s"
updateRow=cursor.executemany(sql4,[('95','优秀'),('85','良好'),('75','中等'),('65','及格')])
print('更新的行数为'+str(updateRow))

# 删除表course中学分为2的课程信息
sql5='DELETE FROM course WHERE credit =%s'
deleteRow=cursor.execute(sql5,'2')
print('删除的行数为'+str(deleteRow))

# 在表StudentInfo中添加字段age
sql6="ALTER TABLE StudentInfo ADD age INT"
cursor.execute(sql6)

# 将表course按成绩降序排序
sql7="SELECT * FROM course ORDER BY grade DESC"
cursor=connection.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute(sql7)
resultlist=cursor.fetchall()
for i in range(len(resultlist)):
    print(resultlist[i])

connection.commit()
cursor.close()
connection.close()