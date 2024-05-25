
from typing import Dict, Tuple
from datetime import datetime, timedelta, time
import random

from qfluentwidgets import MessageBox

from db_models.habit import Habit, HabitCompletion
from db_models.user import User
from view.dialog.dialog_habit_edit import HabitEditDialog
from handlers.subinterfaces.handlers_interface_habit import query_habit_completion_by_habit
from common.tools import TopInfoBar
from common.cur_user import CurUser


class ProgressHandler():
    '''习惯条目的进度数据处理'''
    @staticmethod
    def _query(habit_content: Dict) -> Tuple[int, str]:
        '''根据习惯内容获取进度值和提示

        Args:
            habit_content (Dict): 习惯内容字典

        Returns:
            List[int, str]: [进度值，提示]
        '''
        habit_type = habit_content.get('habit_type')
        if habit_type == 0:
            # 如果习惯类型是0，即可被无限完成，直接返回百分百
            return (100, '可完成 ∞ 次')
        
        '''习惯类型是1，则要计算周期剩余天数 以及周期内已经完成了几次
        例如习惯的创建日期是2024-05-01，limit_days是7，则表示7天为一个周期，
        如果今天是2024-05-09，则最近的周期是08~14，本周期还剩6天
        '''
        limit_days = habit_content.get('type_1_limit_days')
        limit_times = habit_content.get('type_1_limit_times')
        created_at = habit_content.get('created_at')
        created_at = datetime.combine(created_at, time()) # 将date对象转换为datetime对象
        now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) # 当前日期

        # 查询该习惯的所有完成情况
        completions = query_habit_completion_by_habit(habit_content.get('id'))
        if limit_days == 1:
            # 如果周期为1天，只需检查今天的完成次数
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            today_end = today_start + timedelta(days=1) - timedelta.resolution
            period_completions = [cpl for cpl in completions
                                if today_start <= datetime.combine(cpl.get('completed_at'), time()) < today_end]
            period_completions_times = len(period_completions)
            period_msg = '每日任务 '
        else:
            # 计算从创建时间到今天的总天数
            total_days = (now - created_at).days + 1
            # 总天数取余limit_days，得到今天在周期内的天数
            period_offset_now = total_days % limit_days
            period_start = now - timedelta(days=period_offset_now - 1) # 当前周期开始时间
            period_end = period_start + timedelta(days=limit_days - 1)  # 当前周期结束时间
            # 当前周期内的完成情况
            period_completions = [cpl for cpl in completions 
                                if period_start <= datetime.combine(cpl.get('completed_at'), time()) <= period_end]
            period_completions_times = len(period_completions)
            period_msg = f'当前周期：{period_offset_now}/{limit_days}天 '
        # 计算进度值
        progress = period_completions_times / limit_times * 100
        if progress > 100:
            progress = 100       
        return (progress, period_msg + f'已完成{period_completions_times}/{limit_times}次')
        
    @staticmethod
    def query_value(habit_content: Dict) -> int:
        '''根据习惯内容获取进度值'''
        return ProgressHandler._query(habit_content)[0]   

    @staticmethod
    def query_msg(habit_content: Dict) -> str:  
        '''根据习惯内容获取进度提示'''
        return ProgressHandler._query(habit_content)[1] 
    

def handler_delete(self):
    '''删除习惯条目动作'''
    interface = self.parent().parent().parent().parent()    # 获得父界面
    message_box = MessageBox(
        '请确认', f'是否删除习惯“{self.content.get("content")}”？\n已经记录的完成情况也会被删除', interface
        )   # 进行提示
    if message_box.exec():
        # 执行数据库删除
        habit_id = self.content.get('id')
        Habit.execute_with_foreign_keys(Habit.delete().where(Habit.id == habit_id))
        interface.update_card_area()
        TopInfoBar.success(interface, '提示', '删除成功')
    else:
        TopInfoBar.warning(interface, '提示', '取消了操作')   


def handler_edit(self):       
    ''''编辑习惯条目动作'''
    interface = self.parent().parent().parent().parent()    # 获得父界面
    dialog = HabitEditDialog(interface, self.content)   # 弹出编辑对话框
    dialog.show()


def handler_checkin(self):
    '''打卡动作
    
    1. 需要验证是否可以打卡
    2. 打卡成功后，获得奖励，更新界面，弹出提示
    '''
    interface = self.parent().parent().parent().parent()    # 获得父界面
    belong_habit = self.content.get('id')   # 打卡的习惯id
    # 如果是周期性任务，要验证是否可以打卡
    habit_type = self.content.get('habit_type')
    if habit_type == 1 and ProgressHandler.query_value(self.content) == 100:
        # 周期内打卡满了
        TopInfoBar.warning(interface, '打卡失败', '周期内打卡已满啦，无需打卡')
        return
    
    # 插入数据库
    reward = self.content.get('reward')
    if self.content.get('is_random_reward'):
        # 打卡奖励是随机浮动的，则随机生成一个
        reward = int(reward * random.uniform(0.5, 2))
    HabitCompletion(
        belong_habit=belong_habit,
        belong_user=CurUser().uid,
        earned_reward=reward, 
        completed_at=datetime.now().strftime('%Y-%m-%d')
        ).save()
    User.update(reward=User.reward + reward).where(User.id == CurUser().uid).execute()
    # 更新界面
    interface.update_card_area()
    TopInfoBar.success(interface, '打卡成功', f'获得了{reward}🏆！继续坚持吧！', duration=3000)