from typing import cast, Dict

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from qfluentwidgets import (Action, FluentIcon, CommandBar, ImageLabel, BodyLabel, 
                            StrongBodyLabel, ProgressBar)

from ui.habit_card_widget_ui import Ui_Form
from handlers.subinterfaces.handlers_interface_habit_card import *
from common.tools import abspath_


class HabitCard(QWidget, Ui_Form):
    '''习惯条目卡片'''
    def __init__(self, parent=None, content: Dict=None) -> None:
        '''
            content (Dict, optional): 卡片的内容，应当传入一个字典
        '''
        super().__init__(parent)
        self.content = content
        
        self.setupUi(self)  # 初始化ui
        self.init_display(content)  # 初始化显示的内容
        self.init_commandbar()  # 初始化工具条

    def init_display(self, content: Dict):  
        # 设置并调整固定的奖杯图标及其大小，调整习惯图标的大小
        self.reward_icon_label = cast(ImageLabel, self.findChild(ImageLabel, 'rewardIconLabel'))
        self.reward_icon_label.setImage(abspath_('res', 'reward.png'))
        self.reward_icon_label.setFixedSize(24, 24)
        self.image_label = cast(ImageLabel, self.findChild(ImageLabel, 'imageLabel'))
        self.image_label.setImage(abspath_('res', 'icons', f"{content.get('icon')}"))
        self.image_label.setFixedSize(48, 48)
        # 设置奖励值和习惯内容
        self.reward_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'rewardLabel'))  
        self.reward_label.setText(str(content.get('reward'))) 
        self.content_label = cast(BodyLabel, self.findChild(BodyLabel, 'contentLabel'))
        self.content_label.setText(content.get('content'))
        # 设置进度
        self.progress_bar = cast(ProgressBar, self.findChild(ProgressBar, 'progressBar'))
        self.progress_bar.setValue(ProgressHandler.query_value(content))
        self.progress_label = cast(BodyLabel, self.findChild(BodyLabel, 'progressLabel'))
        self.progress_label.setText(ProgressHandler.query_msg(content))

    def init_commandbar(self):
        self.cb = cast(CommandBar, self.findChild(CommandBar, 'commandBar'))
        # 图标侧边显示文本
        self.cb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # 添加按钮
        self.cb.addAction(Action(FluentIcon.CHECKBOX, '打卡', triggered=self.action_checkin))
        self.cb.addAction(Action(FluentIcon.EDIT, '编辑', triggered=self.action_edit))
        self.cb.addAction(Action(FluentIcon.DELETE, '删除', triggered=self.action_delete))

    def action_delete(self):
        return handler_delete(self)               
    
    def action_edit(self):
        return handler_edit(self)
    
    def action_checkin(self):
        return handler_checkin(self)