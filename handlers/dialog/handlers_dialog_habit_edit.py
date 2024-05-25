import os

from qfluentwidgets import ComboBox

from db_models.habit import Habit
from handlers.dialog.handlers_dialog_habit_add import validate_content_reward


def handler_accepted(self):
    '''编辑窗口确认按钮的槽函数'''
    ## 验证填写的内容是否合理
    content = self.lcontent.text().strip()
    reward = self.lreward.text().strip()
    if not validate_content_reward(self, content, reward):
        return
    
    # 更新到数据库
    icon = self.icon_card_paths[self.selected_icon_card]    # 图标
    icon = os.path.basename(icon)   # 数据库只存储图标文件名，而不是完整路径
    is_random_reward = self.switch_button.isChecked() # 是否随机奖励
    period_preset = self.findChild(ComboBox, 'comboBox').currentIndex() # 周期预设
    period_days = self.spinbox_days.value()
    period_times = self.spinbox_times.value()
    # 周期类型，如果选中预设为“无限循环”，而且两个框都是0，作为无限循环型周期
    if period_preset == 0 and period_days == 0 and period_times == 0:
        habit_type = 0
    else:
        habit_type = 1     
    type1_limit_times = period_times if habit_type == 1 else None
    type1_limit_days = period_days if habit_type == 1 else None
    Habit.update(
        icon=icon,
        content=content,
        reward=int(reward),
        is_random_reward=is_random_reward,
        habit_type=habit_type,
        type_1_limit_times=type1_limit_times,
        type_1_limit_days=type1_limit_days
    ).where(Habit.id == self.id).execute()
    # 关闭窗口
    self.close()
    self.parent().update_card_area()