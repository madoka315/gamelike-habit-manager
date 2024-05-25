import os
from typing import cast
from datetime import datetime

from PySide6.QtWidgets import QWidget
from qfluentwidgets import SpinBox, LineEdit, SwitchButton, ComboBox

from db_models.habit import Habit
from common.tools import TopInfoBar
from common.cur_user import CurUser


def handler_period_presets_changed(self, index: int):
    '''周期预设下拉框的槽函数,根据选择的预设,设定默认值

    Args:
        index (int): 下拉框的当前选中项的索引
            0: 无限循环; 1: 每日; 2: 每周; 3: 每月; 4: 每年
    '''
    preset_values = {
        0: (1, 1), 1: (1, 1), 2: (7, 1), 3: (30, 1), 4: (365, 1)
    }
    self = cast(QWidget, self)
    spinbox_days = cast(SpinBox, self.findChild(SpinBox, 'spinBox_days'))
    spinbox_times = cast(SpinBox, self.findChild(SpinBox, 'spinBox_times'))
    # 根据不同的选择预设不同的周期和次数
    spinbox_days.setValue(preset_values[index][0])
    spinbox_times.setValue(preset_values[index][1])


def handler_icon_card_clicked(self, icon_path: str):    
    '''图标卡片的槽函数'''
    # 先检查之前是否选择过了，选择过的话要恢复样式
    if self.selected_icon_card != -1:
        self.icon_cards[self.selected_icon_card].set_selected(False)
    # 设置当前选中的图标卡片
    self.selected_icon_card = self.icon_card_paths.index(icon_path)
    self.icon_cards[self.selected_icon_card].set_selected(True)


def handler_accepted(self):
    '''确认按钮的槽函数
    需要验证输入的数据是否合法，
    如果不合法则提醒，如果合法则插入数据库、更新界面
    '''
    ## 验证填写的内容是否合理
    content = self.findChild(LineEdit, 'lineEdit_content').text().strip()
    reward = self.findChild(LineEdit, 'lineEdit_reward').text().strip()
    if not validate_content_reward(self, content, reward):
        return
    
    ## 验证是否和数据库重合
    is_random_reward = self.findChild(SwitchButton, 'switchButton').isChecked() # 是否随机奖励
    icon = self.icon_card_paths[self.selected_icon_card]    
    icon = os.path.basename(icon)   # 数据库只存储图标文件名，而不是完整路径
    period_preset = self.findChild(ComboBox, 'comboBox').currentIndex() # 周期预设
    if period_preset == 0:
        # 选中“无限循环”
        habit_type = 0
        type1_limit_days = None
        type1_limit_times = None
    else:
        # 选中其它说明是type1
        habit_type = 1
        type1_limit_days = self.findChild(SpinBox, 'spinBox_days').value()
        type1_limit_times = self.findChild(SpinBox, 'spinBox_times').value()
    db_habit = Habit.select().where(
        Habit.content == content, 
        Habit.icon == icon, 
        Habit.habit_type == habit_type, 
        Habit.type_1_limit_days == type1_limit_days, 
        Habit.type_1_limit_times == type1_limit_times
        )
    if db_habit:
        TopInfoBar.error(self, '错误', '该习惯已经存在')
        return     

    ## 插入数据库
    Habit(
        belong_user=CurUser().uid,
        created_at=datetime.now().strftime('%Y-%m-%d'),
        icon=icon,
        content=content,
        reward=int(reward),
        is_random_reward=is_random_reward,
        habit_type=habit_type,
        type_1_limit_times=type1_limit_times,
        type_1_limit_days=type1_limit_days
    ).save()
    # 关闭弹窗，更新界面
    self.parentWidget().update_card_area()
    self.close()


def validate_content_reward(self, content, reward) -> bool:
    # 验证习惯内容
    if len(content) == 0 or len(content) > 64:
        TopInfoBar.error(self, '错误', '习惯内容必须在1-64个字之间')
        return False
    # 验证奖励值
    try:
        reward = int(reward)
    except ValueError:    
        # 输入的不是数字
        TopInfoBar.error(self, '错误', '请输入数字奖励值')
        return False
    if reward <= 0 or reward > 100000000:
        TopInfoBar.error(self, '错误', '奖励值不可过低过高')
        return False
    return True