import sqlite3
sql = open('/Users/xiaoziqi/Desktop/Craiditx/项目/内部/营销场景二分类/sql/train_test_oot.sql', 'r', encoding = 'utf8')
sqltxt = sql.readlines()
# 此时 sqltxt 为 list 类型

# 读取之后关闭文件
sql.close()

# list 转 str
sql = "".join(sqltxt)


con = sqlite3.connect("/Users/xiaoziqi/Desktop/Craiditx/项目/内部/营销场景二分类/流失预警数据/craiditx.db")
cur = con.cursor()
cur.executescript(sql)
con.commit()
con.close()