from typing import cast

from PySide6.QtWidgets import QFrame, QWidget
from PySide6.QtCore import Qt
from qfluentwidgets import Action, FluentIcon, CommandBar, FlowLayout

from ui.interface_habit_ui import Ui_Frame
from view.subinterfaces.interface_habit_card import HabitCard
from handlers.subinterfaces.handlers_interface_habit import *
from common.cur_user import CurUser
from common.tools import remove_widget_by_layout


class HabitInterface(QFrame, Ui_Frame):
    '''自律习惯子界面'''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        # 初始化ui
        self.setupUi(self)
        # 初始化工具条和卡片区域
        self.init_commandbar()
        self.init_card_area()
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('HabitInterface')

    def init_card_area(self):
        # 创建用于展示习惯卡片的滚动布局，滚动布局依附于widget容器
        self.widget = cast(QWidget, self.findChild(QWidget, 'widget'))
        self.flow_layout = FlowLayout(self.widget)
        # 更新卡片区域
        self.update_card_area()

    def init_commandbar(self):
        self.cb = cast(CommandBar, self.findChild(CommandBar, 'commandbar'))
        # 图标底部显示文本
        self.cb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # 添加按钮
        self.cb.addAction(Action(FluentIcon.ADD, '添加', triggered=self.action_habit_add))

    def update_card_area(self):
        '''更新卡片区域'''
        remove_widget_by_layout(self.flow_layout)  
        # 查询习惯条目数据并添加卡片
        habits = query_habit_all()
        for habit in habits:
            # 是否属于当前用户
            if not habit.get('belong_user') == CurUser().uid:
                continue
            card = HabitCard(self, habit)
            self.flow_layout.addWidget(card)      

    def action_habit_add(self):
        return handler_habit_add(self)   