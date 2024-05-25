from peewee import CharField, IntegerField

from db_models.base import BaseModel


class User(BaseModel):
    '''用户模型
    
    username: 用户名
    password: 密码
    reward: 持有的奖励值
    '''
    username = CharField(unique=True)
    password = CharField()
    reward = IntegerField()