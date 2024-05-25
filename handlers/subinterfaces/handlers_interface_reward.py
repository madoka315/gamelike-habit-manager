from typing import List, Dict

from common.cur_user import CurUser
from db_models.user import User
from db_models.reward import Reward, RewardCompletion


def query_reward_val_by_user(uid: int) -> int:
    """
    根据用户id查询用户奖励值
    """
    return User.select(User.reward).where(User.id == uid).first().reward


def query_reward_all() -> List[Dict]:
    '''查询所有奖励条目

    Returns:
        List[Dict]: 返回所有奖励条目数据字典组成的列表
    '''
    res = []
    items = Reward.select()
    for item in items:
        res.append({
            'id': item.id,
            'belong_user': item.belong_user.id,
            'icon': item.icon,
            'content': item.content,
            'consume': item.consume
        })
    return res


def query_reward_completion_by_reward(reward: Reward) -> List[Dict]:
    '''根据奖励条目查询奖励兑换情况'''
    res = []
    for item in RewardCompletion.select().where(
        RewardCompletion.belong_reward == reward,
        RewardCompletion.belong_user == CurUser().uid
        ):
        res.append({
            'belong_reward': item.belong_reward.id,
            'belong_user': item.belong_user.id,
            'completed_at': item.completed_at
            })
    return res 