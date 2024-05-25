from peewee import CharField, ForeignKeyField, IntegerField, DateField

from db_models.base import BaseModel
from db_models.user import User


class Reward(BaseModel):
    '''奖励条目模型
    
    belong_user: 所属用户
        (backref表示外键引用模型上自动生成一个属性，用于查询user拥有的habits)
    icon: 奖励图标
    content: 奖励内容
    consume: 消耗奖励值
    '''
    belong_user = ForeignKeyField(
        User, backref='rewards', on_delete='CASCADE', on_update='CASCADE')
    icon = CharField()
    content = CharField(max_length=64)
    consume = IntegerField()


class RewardCompletion(BaseModel):
    '''奖励兑换完成条目模型
    
    belong_reward: 所属习惯
    belong_user: 所属用户
    completed_at: 完成时间
    '''
    belong_reward = ForeignKeyField(
        Reward, backref='statuses', on_delete='CASCADE', on_update='CASCADE')
    belong_user = ForeignKeyField(
        User, backref='reward_statuses', on_delete='CASCADE', on_update='CASCADE')
    completed_at = DateField()