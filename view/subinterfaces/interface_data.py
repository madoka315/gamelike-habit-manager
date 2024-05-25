from typing import cast

from PySide6.QtWidgets import QFrame, QGridLayout, QVBoxLayout
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from qfluentwidgets import StrongBodyLabel, BodyLabel, ImageLabel

from ui.interface_data_ui import Ui_Frame
from handlers.subinterfaces.handlers_interface_data import *
from common.cur_user import CurUser
from common.tools import *


class DataInterface(QFrame, Ui_Frame):
    '''数据统计子界面'''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)  # 初始化ui
        self.init_display() # 初始化显示
        # 必须给对象命名，否则无法被引用
        self.setObjectName("DataInterface")

    def init_display(self):
        '''初始化显示'''
        self.update_all()
        # 设置图标与调整大小
        self.reward_icon = cast(ImageLabel, self.findChild(ImageLabel, 'rewardiconLabel'))
        self.reward_icon.setImage(abspath_('res', 'reward.png'))
        self.reward_icon.setFixedSize(24, 24)
        self.habit_icon = cast(ImageLabel, self.findChild(ImageLabel, 'habiticonLabel'))
        self.habit_icon.setImage(abspath_('res', 'icons', 'work.png'))
        self.habit_icon.setFixedSize(24, 24)
        self.detail_icon = cast(ImageLabel, self.findChild(ImageLabel, 'detailiconLabel'))
        self.detail_icon.setImage(abspath_('res', 'icons', 'graph.png'))
        self.detail_icon.setFixedSize(24, 24)

    def update_all(self):
        '''更新总奖杯值、总打卡数、总兑换数、各数据界面'''
        self.update_reward()
        self.update_habit_completion()
        self.update_reward_completion()
        self.update_habit_data()
        self.update_reward_data()
        self.update_detail_data()

    def update_reward(self):
        '''更新总奖杯值'''        
        self.reward_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'rewardLabel'))
        user_reward = query_reward_val_by_user(CurUser().uid)
        self.reward_label.setText(str(user_reward))

    def update_habit_completion(self):    
        '''更新总习惯打卡次数'''    
        self.habitcpl_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'habitcplLabel'))
        user_cpl = query_habit_completion_all()
        user_cpl = [i for i in user_cpl if i['belong_user'] == CurUser().uid]
        self.habitcpl_label.setText(str(len(user_cpl)))

    def update_reward_completion(self): 
        '''更新总奖励兑换次数'''       
        self.rewardcpl_label = cast(StrongBodyLabel, self.findChild(StrongBodyLabel, 'rewardcplLabel'))
        user_cpl = query_reward_completion_all()
        user_cpl = [i for i in user_cpl if i['belong_user'] == CurUser().uid]
        self.rewardcpl_label.setText(str(len(user_cpl)))        

    def update_habit_data(self):
        '''更新习惯数据区域'''
        self.grid_layout = cast(QGridLayout, self.findChild(QGridLayout, 'gridLayout'))
        remove_widget_by_layout(self.grid_layout)
        # 查询数据
        data = query_habit_data()
        data = [i for i in data if i['belong_user'] == CurUser().uid]
        # 是当前用户的就创建并加入数据区域
        cur_row = 0
        cur_col = 0
        for i in data:
            frame = QFrame(self)    # 创建容器
            vlayout = QVBoxLayout(frame)    # 在容器上创建垂直布局，然后加入三个文字标签
            vlayout.addWidget(StrongBodyLabel(i['content']), alignment=Qt.AlignTop)
            vlayout.addWidget(BodyLabel('总打卡次数：' + str(i['completion'])), alignment=Qt.AlignTop)
            vlayout.addWidget(BodyLabel('总获得奖杯：' + str(i['total_earned'])), alignment=Qt.AlignTop)
            self.grid_layout.addWidget(frame, cur_row, cur_col)   # 在网格布局中添加新数据
            cur_col += 1
            if cur_col == 4:   # 列数达到4时换行
                cur_col = 0
                cur_row += 1
        
    def update_reward_data(self):
        '''更新奖励数据区域'''
        self.grid_layout = cast(QGridLayout, self.findChild(QGridLayout, 'gridLayout_2'))
        remove_widget_by_layout(self.grid_layout)
        # 查询数据
        data = query_reward_data()
        data = [i for i in data if i['belong_user'] == CurUser().uid]
        # 是当前用户的就创建并加入数据区域
        cur_row = 0
        cur_col = 0
        for i in data:
            frame = QFrame(self)    # 创建容器
            vlayout = QVBoxLayout(frame)    # 在容器上创建垂直布局，然后加入三个文字标签
            vlayout.addWidget(StrongBodyLabel(i['content']), alignment=Qt.AlignTop)
            vlayout.addWidget(BodyLabel('总实现次数：' + str(i['completion'])), alignment=Qt.AlignTop)
            vlayout.addWidget(BodyLabel('总消耗奖杯：' + str(i['total_consumed'])), alignment=Qt.AlignTop)
            self.grid_layout.addWidget(frame, cur_row, cur_col)   # 在网格布局中添加新数据
            cur_col += 1
            if cur_col == 4:   # 列数达到4时换行
                cur_col = 0
                cur_row += 1

    def update_detail_data(self):
        '''更新详细记录区域'''
        self.vlayout = cast(QVBoxLayout, self.findChild(QVBoxLayout, 'vlayout'))
        remove_widget_by_layout(self.vlayout)
        # 查询数据
        data = query_detail_data()
        data = [i for i in data if i['belong_user'] == CurUser().uid]
        # 是当前用户的就创建标签并加入数据区域
        for i in data:
            label = BodyLabel(self)
            # 组合标签显示内容
            msg = f"{i.get('completed_at')}"
            if i.get('type') == 'habit':
                # 是习惯完成记录
                msg += f" 完成习惯打卡 {i.get('content')} 🏆+{i.get('earned_reward')}"
                label.setTextColor(QColor(32, 81, 127))
            else:
                # 是奖励兑换记录
                msg += f" 兑换奖励 {i.get('content')} 🏆-{i.get('consume')}"
                label.setTextColor(QColor(15, 117, 88)) 
            label.setText(msg)       
            self.vlayout.addWidget(label, alignment=Qt.AlignTop)