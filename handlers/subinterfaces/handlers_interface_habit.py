from typing import List, Dict

from db_models.habit import Habit, HabitCompletion
from view.dialog.dialog_habit_add import HabitAddDialog
from common.cur_user import CurUser


def handler_habit_add(parent):
    dialog = HabitAddDialog(parent)
    dialog.show()


def query_habit_all() -> List[Dict]:
    '''查询所有习惯数据

    Returns:
        List[Dict]: 返回所有习惯数据字典组成的列表
    '''
    res = []
    items = Habit.select()
    for item in items:
        res.append({
            'id': item.id,
            'belong_user': item.belong_user.id,
            'created_at': item.created_at,
            'icon': item.icon,
            'content': item.content,
            'reward': item.reward,
            'is_random_reward': item.is_random_reward,
            'habit_type': item.habit_type,
            'type_1_limit_times': item.type_1_limit_times,
            'type_1_limit_days': item.type_1_limit_days
        })
    return res


def query_habit_completion_by_habit(habit: Habit) -> List[Dict]:
    '''根据习惯查询习惯完成情况'''
    res = []
    for item in HabitCompletion.select().where(
        HabitCompletion.belong_habit == habit,
        HabitCompletion.belong_user == CurUser().uid
        ):
        res.append({
            'belong_habit': item.belong_habit.id,
            'belong_user': item.belong_user.id,
            'earned_reward': item.earned_reward,
            'completed_at': item.completed_at
            })
    return res    


if __name__ == '__main__':
    print(query_habit_completion_by_habit(Habit.get_by_id(2)))