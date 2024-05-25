from typing import cast, Dict

from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import ImageLabel, StrongBodyLabel

from ui.interface_reward_ui import Ui_Frame
from view.subinterfaces.interface_reward_card import RewardCard
from handlers.subinterfaces.handlers_interface_reward import *
from common.tools import *
from common.cur_user import CurUser


class RewardInterface(QFrame, Ui_Frame):
    '''奖励兑换子界面'''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        # 初始化ui
        self.setupUi(self)
        self.init_display()
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('RewardInterface')

    def init_display(self):
        '''初始化显示'''
        # 设置并调整固定的奖杯图标及其大小，调整奖励图标的大小
        self.reward_icon_label = cast(ImageLabel, self.findChild(ImageLabel, 'rewardIconLabel'))
        self.reward_icon_label.setImage(abspath_('res', 'reward.png'))
        self.reward_icon_label.setFixedSize(24, 24)
        self.update_reward()
        self.init_card_area()

    def init_card_area(self):
        '''初始化卡片区域'''
        self.vlayout = cast(QVBoxLayout,self.findChild(QVBoxLayout, 'vlayout'))
        self.update_card_area()

    def update_reward(self):
        '''更新奖杯值'''
        self.reward_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'rewardLabel'))
        user_reward = query_reward_val_by_user(CurUser().uid)
        self.reward_label.setText(f'奖杯值：{user_reward}')

    def update_card_area(self):
        # 清空已有的卡片
        remove_widget_by_layout(self.vlayout)
        # 查询奖励条目数据并添加卡片
        rewards = query_reward_all()
        for reward in rewards:
            # 是否属于当前用户
            if not reward.get('belong_user') == CurUser().uid:
                continue
            card = RewardCard(self, reward)
            self.vlayout.addWidget(card)     


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    window = RewardInterface()
    window.show()
    app.exec()   
