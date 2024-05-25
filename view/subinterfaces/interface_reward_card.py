from typing import cast, Dict

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from qfluentwidgets import ImageLabel, StrongBodyLabel, BodyLabel

from ui.reward_card_widget_ui import Ui_Form
from handlers.subinterfaces.handlers_interface_reward import *
from handlers.subinterfaces.handlers_interface_reward_card import *
from common.tools import abspath_


class RewardCard(QWidget, Ui_Form):
    '''奖励条目卡片'''
    def __init__(self, parent=None, content: Dict=None):
        '''
            content (Dict, optional): 卡片的内容，应当传入一个字典
        '''
        super().__init__(parent)
        self.content = content

        self.setupUi(self)  # 初始化UI
        self.init_display(content)  # 初始化显示的内容

    def init_display(self, content: Dict):        
        # 设置并调整奖励图标的大小
        self.image_label = cast(ImageLabel, self.findChild(ImageLabel, 'imageLabel_2'))
        self.image_label.setImage(abspath_('res', 'icons', f"{content.get('icon')}"))
        self.image_label.setFixedSize(48, 48)
        # 设置并调整固定的奖杯图标及其大小，消耗的奖杯
        self.reward_icon_label = cast(ImageLabel, self.findChild(ImageLabel, 'rewardIconLabel'))
        self.reward_icon_label.setImage(abspath_('res', 'reward.png'))
        self.reward_icon_label.setFixedSize(24, 24)
        self.consume_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'consumeLabel'))  
        self.consume_label.setText(str(content.get('consume'))) 
        # 设置奖励内容和已兑换情况
        self.content_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'descLabel'))
        self.content_label.setText(content.get('content'))
        self.completion_label = cast(BodyLabel, self.findChild(BodyLabel, 'completionLabel'))
        self.cpl_times = len(query_reward_completion_by_reward(content.get('id')))
        if self.cpl_times > 0:
            self.completion_label.setText(f'奖励已兑换 {self.cpl_times} 次')

    @Slot(bool)
    def reward_complete(self):
        '''兑换奖励按钮的槽函数'''
        return handler_reward_complete(self)        