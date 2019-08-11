#若需要使用Mysqldb,则用下面这两个语句:
import pymysql  #将pymysql导入到py中
pymysql.install_as_MySQLdb() #使用pymysql代替mysqldb

import web

db = web.database(dbn="mysql",host='localhost',port=3306,user="root",pw="root",db="test",charset="utf8")

results = db.query("SELECT * from user")

dict = {}
for i in results:
    dict[results.username] = user.age
print(dict)