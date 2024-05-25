from typing import Dict

from PySide6.QtCore import Slot
from qfluentwidgets import LineEdit, SpinBox

from view.dialog.dialog_habit_add import HabitAddDialog
from handlers.dialog.handlers_dialog_habit_edit import *
from common.tools import abspath_


class HabitEditDialog(HabitAddDialog):
    '''习惯条目编辑弹窗。相比添加弹窗填写了已有数据项'''
    def __init__(self, parent=None, content: Dict=None):
        super().__init__(parent)
        self.id = content.get('id')
        
        self.init_display_content(content)

    def init_display_content(self, content: Dict):
        '''初始化显示已有数据'''
        self.yesButton.setText('确定更新')
        # 图标。由于数据库存储的是文件名，需要拼接完整路径
        icon_path = abspath_('res', 'icons', content.get('icon'))
        self.selected_icon_card = self.icon_card_paths.index(icon_path)   # 图标索引
        self.icon_cards[self.selected_icon_card].set_selected(True)   # 设为选中
        # 习惯内容
        self.lcontent = self.findChild(LineEdit, 'lineEdit_content')
        self.lcontent.setText(content.get('content'))
        # 奖励
        self.lreward = self.findChild(LineEdit, 'lineEdit_reward')
        self.lreward.setText(str(content.get('reward')))
        self.switch_button.setChecked(content.get('is_random_reward'))
        # 周期设定
        limit_days = content.get('type_1_limit_days')
        limit_times = content.get('type_1_limit_times')
        self.spinbox_days = self.findChild(SpinBox, 'spinBox_days')
        self.spinbox_times = self.findChild(SpinBox, 'spinBox_times')
        if limit_days and limit_times:
            # 两项有值说明是周期习惯，需要设定下拉框等
            days_presets_dict = {
                1: 1, 7: 2, 30: 3, 365: 4 
            }
            if limit_days in days_presets_dict:
                # 如果周期天数在预设值中，则设置下拉框
                self.combo_box.setCurrentIndex(days_presets_dict[limit_days]) 
            self.spinbox_days.setValue(limit_days)
            self.spinbox_times.setValue(limit_times)
        else:
            # 两项无值说明是无限循环，设置成0
            self.spinbox_days.setValue(0)
            self.spinbox_times.setValue(0)

    @Slot()
    def on_accepted(self):
        '''重写确认按钮的槽函数'''
        return handler_accepted(self)