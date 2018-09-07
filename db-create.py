import pymysql
connection=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='12345',db='student',charset='utf8')
cursor=connection.cursor()

# 创建学生信息表StudentInfo
sql1="CREATE TABLE IF NOT EXISTS StudentInfo(Id INT PRIMARY KEY AUTO_INCREMENT,Name VARCHAR(25))"
cursor.execute(sql1)

# 创建用户信息表user
sql2="CREATE TABLE IF NOT EXISTS user(userName VARCHAR(25) PRIMARY KEY,password VARCHAR(25))"
cursor.execute(sql2)

connection.commit()
cursor.close()
connection.close()