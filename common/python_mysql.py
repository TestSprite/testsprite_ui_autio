# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2023/3/15  15:39
# 文件名：python_mysql.py
import pymysql
def link_mysql(host,user,password,db,sql):
    global cur, conn
    try:
        #打开数据库连接 connect(host,username,pwd,dbname)
        conn=pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db,
            charset='utf8'
        )
        #使用cursor()方法创建一个游标对象 cursor->to execute queries with
        cur=conn.cursor()
        #执行sql语句
        sql=sql
        cur.execute(sql)
        #像数据库提交
        conn.commit()
    except:
        #发送错误时回滚
        conn.rollback()
    # 关闭游标
    cur.close()
    #关闭数据库连接
    conn.close()

# if __name__ == '__main__':
#     sql = '''
#     delete from admin_roles where name='助理1'
#     '''
#     link_mysql("60.205.182.126", "test_read", "1q2w3e4r", "ukuoffer_test_new", sql)