from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy
from qfluentwidgets import (PrimaryPushSettingCard, ExpandGroupSettingCard, PlainTextEdit, ComboBox,
                            PushButton, BodyLabel, SettingCardGroup, FluentIcon as FIF)

from handlers.subinterfaces.handlers_inteface_settings import *
from common.cur_user import CurUser


class DBSettingCard(ExpandGroupSettingCard):
    '''数据库调试设置卡片'''
    def __init__(self, parent=None):
        super().__init__(FIF.SETTING, "数据库调试", "手动调试数据库", parent)

        # 提交按钮
        self.btn = PushButton("提交")
        self.btn_label = BodyLabel("提交SQL")

        # 预设语句
        self.auto_label = BodyLabel("自动填充")
        self.auto_comboBox = ComboBox()
        self.auto_comboBox.addItems(["请选择", "插入用户", "更新用户", "删除用户",
                                     "插入习惯", "更新习惯", "删除习惯",
                                     "插入奖励条目", "更新奖励条目", "删除奖励条目"
                                     ])

        # 填写框
        self.edit = PlainTextEdit()

        # 调整内部布局
        self.viewLayout.setContentsMargins(0, 0, 0, 0)
        self.viewLayout.setSpacing(0)

        # 添加各组件到设置卡中
        self.add(self.auto_label, self.auto_comboBox)
        self.add(self.btn_label, self.btn)
        self.add(None, self.edit)

    def add(self, label, widget):
        '''创建组件到设置卡，没有标签label说明是编辑框'''
        w = QWidget()
        layout = QHBoxLayout(w) # 创建水平布局
        layout.setContentsMargins(48, 12, 48, 12)   # 设置组件间距
        if label is None:
            w.setFixedHeight(150)
            layout.addWidget(widget)
        else:
            # 标签和按钮/下拉框都有，则按普通设置卡的样式调整
            w.setFixedHeight(60)    # 设置固定高度
            layout.addWidget(label) 
            layout.addStretch(1)    # 设置标签权重，以便内部组件靠右
            layout.addWidget(widget)

        # 添加组件到设置卡
        self.addGroupWidget(w)


class SettingsInterface(QFrame):
    '''调试子界面
    
    这个类由于只用组件库的组件即可，所以没有手动创建ui文件
    '''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.init_display() # 初始化显示
        self.init_signals() # 初始化信号
        # 必须设置全局唯一对象名称
        self.setObjectName("settingsInterface")

    def init_display(self):
        '''初始化显示'''
        self.vlayout = QVBoxLayout(self) # 创建垂直布局
        self.vlayout.setContentsMargins(20, 20, 20, 20) # 设置内容间距
        # 创建用户设置卡片
        self.user_setting = PrimaryPushSettingCard(
            text='用户切换',
            icon=FIF.PEOPLE,
            title='当前登录的用户',
            content=f'用户名：{CurUser().user}',
            parent=self  
            )
        # 创建数据库调试卡片
        self.db_setting = DBSettingCard(self)
        # 依次添加到卡片组中
        self.settings = SettingCardGroup('')
        self.settings.addSettingCard(self.user_setting)
        self.settings.addSettingCard(self.db_setting)
        self.vlayout.addWidget(self.settings, alignment=Qt.AlignTop)
        
    def init_signals(self):
        '''初始化信号'''
        self.user_setting.clicked.connect(self.switch_user) # 点击切换用户的信号
        self.db_setting.auto_comboBox.currentIndexChanged.connect(self.fill_preset) # 切换预设的信号
        self.db_setting.btn.clicked.connect(self.execute_sql)   # 提交SQL语句按钮的信号

    @Slot(bool)
    def switch_user(self):
        '''切换用户按钮的槽函数'''
        return handler_switch_user()
    
    @Slot(int)
    def fill_preset(self, index: int):
        '''预设语句切换的槽函数'''
        return handler_fill_preset(self, index)
    
    @Slot(bool)
    def execute_sql(self):
        '''执行SQL语句的槽函数'''
        return handler_execute_sql(self)