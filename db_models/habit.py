from peewee import CharField, ForeignKeyField, IntegerField, BooleanField, DateField

from db_models.base import BaseModel
from db_models.user import User


class Habit(BaseModel):
    '''自律习惯条目模型
    
    belong_user: 所属用户
        (backref表示外键引用模型上自动生成一个属性，用于查询user拥有的habits)
    created_at: 创建时间
    icon: 习惯图标
    content: 习惯内容,最多64字
    reward: 奖励值
    is_random_reward: 是否随机奖励
    habit_type: 习惯类型
        (0: 可被无限完成，1: 周期内完成指定次)
    type_1_limit_times: 周期内次数限制
        (当habit_type=1时，此字段有效)
    type_1_limit_days: n天为一周期
        (当habit_type=1时，此字段有效)
    '''
    belong_user = ForeignKeyField(
        User, backref='habits', on_delete='CASCADE', on_update='CASCADE')
    created_at = DateField()
    icon = CharField()
    content = CharField(max_length=64)
    reward = IntegerField()
    is_random_reward = BooleanField()
    habit_type = IntegerField()
    type_1_limit_times = IntegerField(null=True)
    type_1_limit_days = IntegerField(null=True)


class HabitCompletion(BaseModel):
    '''习惯完成条目模型
    
    belong_habit: 所属习惯
    belong_user: 所属用户
    earned_reward: 获得奖励值
    completed_at: 完成时间
    '''
    belong_habit = ForeignKeyField(
        Habit, backref='statuses', on_delete='CASCADE', on_update='CASCADE')
    belong_user = ForeignKeyField(
        User, backref='habit_statuses', on_delete='CASCADE', on_update='CASCADE')
    earned_reward = IntegerField()
    completed_at = DateField()