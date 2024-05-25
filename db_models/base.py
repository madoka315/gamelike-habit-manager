from peewee import SqliteDatabase, Model

from common.tools import abspath_
from config import DB_PATH


db = SqliteDatabase(abspath_(DB_PATH))


class BaseModel(Model):
    class Meta:
        database = db  # 设置基类的数据库连接

    @classmethod
    def execute_with_foreign_keys(cls, query):
        '''执行时确保级联操作'''
        db.execute_sql('PRAGMA foreign_keys = ON;')
        return query.execute()        
    
    @classmethod
    def executes_with_foreign_keys_commit(cls, querys):
        '''执行多条语句，同时确保级联操作'''
        db.execute_sql('PRAGMA foreign_keys = ON;')
        for query in querys:            
            db.execute_sql(query)
            db.commit()
            