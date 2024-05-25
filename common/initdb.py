import os

from peewee import SqliteDatabase

from db_models.user import User
from db_models.habit import Habit, HabitCompletion
from db_models.reward import Reward, RewardCompletion
from config import PREPARED_EXECUTES


def init_db(db_path: str):
    need_init = False   # 标记是否是第一次初始化
    if not os.path.exists(db_path):
        # 如果不存在数据库，就先创建文件
        with open(db_path, 'w') as f:
            pass  # 文件会被创建，这里没有写入任何内容
        need_init = True
    # 连接到数据库并创建表
    db = SqliteDatabase(db_path)
    db.connect()
    db.execute_sql('PRAGMA foreign_keys = ON')

    if need_init:
        db.create_tables([User, Habit, HabitCompletion, Reward, RewardCompletion])
        # 导入预设数据
        for statement in PREPARED_EXECUTES:
            db.execute_sql(statement)
            db.commit()