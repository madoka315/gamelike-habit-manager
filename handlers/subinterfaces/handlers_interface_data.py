from typing import List, Dict

from db_models.habit import Habit, HabitCompletion
from db_models.reward import Reward, RewardCompletion
# 复用方法
from handlers.subinterfaces.handlers_interface_reward import query_reward_val_by_user
from handlers.subinterfaces.handlers_interface_habit import *
from handlers.subinterfaces.handlers_interface_reward import *


def query_habit_completion_all() -> List[Dict]:
    """查询所有习惯完成情况

    Returns:
        List[Dict]: 包含习惯完成条目字典的列表
    """
    res = []
    cpls = HabitCompletion.select()
    for cpl in cpls:
        res.append({
            'belong_habit': cpl.belong_habit.id,
            'belong_user': cpl.belong_user.id,
            'earned_reward': cpl.earned_reward,
            'completed_at': cpl.completed_at
        })
    return res


def query_reward_completion_all() -> List[Dict]:
    """查询所有奖励的完成情况

    Returns:
        List[Dict]: 包含奖励兑换条目字典的列表
    """
    res = []
    cpls = RewardCompletion.select()
    for cpl in cpls:
        res.append({
            'belong_reward': cpl.belong_reward.id,
            'belong_user': cpl.belong_user.id,
            'completed_at': cpl.completed_at
        })
    return res    


def query_habit_data() -> List[Dict]:
    '''数据统计用-查询并返回习惯对应的数据
    
    Returns:
        List[Dict]: [{ belong_user, content, completion, total_earned }, ]
    '''
    res = []
    habits = query_habit_all()  # 获取所有习惯条目
    for habit in habits:
        # 根据习惯查询完成情况
        cpls = query_habit_completion_by_habit(habit.get('id'))
        # 计算需要的完成次数和总获得奖杯
        completion = len(cpls)
        total_earned = sum([cpl.get('earned_reward') for cpl in cpls])
        res.append({
            'belong_user': habit.get('belong_user'),
            'content': habit.get('content'),
            'completion': completion,
            'total_earned': total_earned
        })
    return res    


def query_reward_data() -> List[Dict]:
    '''数据统计用-查询并返回奖励条目对应的数据
    
    Returns:
        List[Dict]: [{ belong_user, content, completion, total_consumed }, ]
    '''
    # 获取奖励数据
    res = []
    for reward in query_reward_all():
        # 获取奖励的完成情况
        cpls = query_reward_completion_by_reward(reward.get('id'))
        # 计算需要的完成次数和总获得奖杯
        completion = len(cpls)
        total_consumed = reward.get('consume') * completion
        res.append({
            'belong_user': reward.get('belong_user'),
            'content': reward.get('content'),
            'completion': completion,
            'total_consumed': total_consumed
        })
    return res 


def query_detail_data():
    """数据统计用-查询并倒序返回 习惯和奖励的所有记录的详细数据
    
    Returns:
        List[Dict]: [{ type(是习惯还是奖励条目), ... }, ]
    """
    habitcpls = []
    habits = query_habit_all()  # 查询所有习惯
    for habit in habits:
        # 根据习惯ID查询完成情况，并添加到habitcpls列表
        cpls = query_habit_completion_by_habit(habit.get('id')) 
        for cpl in cpls:
            # 为习惯完成数据设置类型和内容
            cpl['type'] = 'habit'
            cpl['content'] = habit.get('content')
            habitcpls.append(cpl)
    
    rewardcpls = []
    rewards = query_reward_all()  # 查询所有奖励
    for reward in rewards:
        # 根据奖励ID查询完成情况，并扩展到rewardcpls列表
        cpls = query_reward_completion_by_reward(reward.get('id'))
        for cpl in cpls:
            # 为奖励完成数据设置类型和内容
            cpl['type'] = 'reward'
            cpl['consume'] = reward.get('consume')
            cpl['content'] = reward.get('content')
            rewardcpls.append(cpl)    
    
    # 将习惯和奖励的完成数据合并，并按完成时间逆序排序
    res = habitcpls + rewardcpls
    res.sort(key=lambda x: x['completed_at'], reverse=True)    
    return res             