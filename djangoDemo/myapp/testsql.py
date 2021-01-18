'''
此文件主要用于测试连接mysql以及练习sql操作
'''
'''
create table 'trade' (
    'id' int(4) unsigned NOT NULL AUTO_INCREMENT,
    'name' varchar(6) NOT NULL COMMIT '用户真实姓名',
    'account' varchar(11) NOT NULL COMMIT '银行存储账号',
    'saving' decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMIT '银行储存金额',
    'expend' decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMIT '账户支出总计',
    'income' decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMIT '账户收入总计',
    PRIMARY KEY ('id'),
    UNIQUE KEY 'name_UNIQUE' ('name') 
) ENGINE=InnorDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
INSERT INTO 'trade' values(1,'乔布斯','12131313211',0.00,0.00,0.00)
'''

import pymysql

# 建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='mysqlroot',
    database='yiibaidb',
    charset='utf8',
)
# 创建游标
cursor = conn.cursor()
# 编写sql语句进行操作
# 插入数据
# sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
# data = ('雷军', '13512345678', 10000)
# # 执行sql语句
# cursor.execute(sql % data)
# # 提交（select create 等为自动提交, update insert delete等需要）
# conn.commit()
# print('插入 %s 条数据' %cursor.rowcount)
# 修改数据
# sql = 'update trade set saving=%.2f,expend=%.2f,income=%.2f where id=%s'
# data = (200,600,800,5)
# cursor.execute(sql % data)
# conn.commit()
# print("更新%s条数据" %cursor.rowcount)
# 删除数据
# sql = "delete from trade where id = %s"
# data = (4,)
# cursor.execute(sql % data)
# print("删除了%s条数据" %cursor.rowcount)
# 事务处理
# sql_1 = "update trade set saving = saving + 150,expend = expend + 300,income = income + 600 where id = 1"
# sql_2 = "update trade set saving = saving * 100,expend = expend + 100,income = income + 200 where id = 2"
# sql_3 = "update trade set saving = saving + 150,expend = expend + 900,income = income + 10000 where id = 3"
# try:
#     cursor.execute(sql_1)
#     cursor.execute(sql_2)
#     cursor.execute(sql_3)
# except Exception as e:
#     conn.rollback()
#     print(e)
#     print('事务失败')
# finally:
#     conn.commit()
#     print("事务提交")
# 测试
sql = 'select * from  employees'
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
