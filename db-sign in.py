import pymysql
# 用户登录
user=input('请输入用户名：')
pwd=input('请输入密码：')
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='12345',db='student',charset='utf8')
cursor=conn.cursor()
sql="SELECT * FROM user WHERE userName=%s AND password=%s"
result=cursor.execute(sql,(user,pwd))
cursor.close()
conn.close()
if result:
    print("登录成功！")
else:
    print("登录失败!")
