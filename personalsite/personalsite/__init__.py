'''
Django默认配置是sqlite3数据库, 加入如下内容
防止出现Error Loading MySQLdb module
'''
import pymysql
pymysql.install_as_MySQLdb()
