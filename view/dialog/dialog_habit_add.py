import os
from typing import cast

from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QColor
from qfluentwidgets import (MessageBoxBase, ComboBox, SwitchButton, FlowLayout, ElevatedCardWidget, 
                            ImageLabel, themeColor)

from ui.dialog_habit_add_ui import Ui_dialog_habit_add
from handlers.dialog.handlers_dialog_habit_add import *
from common.tools import abspath_


class IconCard(ElevatedCardWidget):
    '''添加弹窗中的图标卡片'''
    clicked = Signal(str)  # 添加自定义的点击信号

    def __init__(self, parent=None, icon_path: str=None):
        super().__init__(parent)
        self.icon_path = icon_path 
        self.is_selected = False    # 是否选中

        self.setFixedSize(64, 64)   # 设置卡片大小
        self.vlayout = QVBoxLayout(self)    # 创建垂直布局
        self.icon_label = ImageLabel(self)      # 创建图标标签
        self.icon_label.setImage(icon_path)
        self.icon_label.setFixedSize(36, 36)
        self.vlayout.addWidget(self.icon_label, alignment=Qt.AlignHCenter)

        self.overload_bgcolor() # 重写关于卡片背景颜色的方法，便于展示选中状态

    def set_selected(self, selected: bool):
        '''设置卡片选中状态'''
        if selected:
            self.is_selected = True
        else:
            self.is_selected = False
        self._updateBackgroundColor()  # 手动更新一下背景色

    def mouseReleaseEvent(self, e):
        '''重写鼠标事件，使得点击图标时触发自定义的点击信号'''
        self.clicked.emit(self.icon_path)        

    def overload_bgcolor(self):
        def bgcolor():
            return QColor(themeColor()) if self.is_selected else QColor(255, 255, 255)
        self._normalBackgroundColor = bgcolor
        self._hoverBackgroundColor = bgcolor
        self._pressedBackgroundColor = bgcolor


class HabitAddDialog(MessageBoxBase, Ui_dialog_habit_add):
    '''基于MessageBoxBase的习惯条目添加弹窗'''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.icon_cards = []    # 存储已有图标卡片，方便改变样式
        self.icon_card_paths = []   # 存储已有图标路径
        self.selected_icon_card = -1    # 记录选中的图标索引，-1表示没选过

        self.container = QWidget(self)   
        self.setupUi(self.container) # 需要一个容器来初始化ui
        self.viewLayout.addWidget(self.container)    # 然后将容器添加到已经提供的viewLayout中

        self.init_display()
        self.init_signals()

    def init_display(self):
        '''初始化显示内容'''
        # 图标区域
        self.scr_widget = self.findChild(QWidget, 'scrollAreaWidgetContents')
        self.flow_layout = FlowLayout(self.scr_widget)
        for root, dirs, files in os.walk(abspath_('res', 'icons')):
            # 遍历图标，创建图标卡片
            for file in files:
                path = os.path.join(root, file) # 图标的绝对路径
                card = IconCard(self, path)
                card.clicked.connect(self.on_icon_card_clicked)
                self.icon_cards.append(card)
                self.icon_card_paths.append(path)
                self.flow_layout.addWidget(card)
        # 设置周期预设
        self.combo_box = cast(ComboBox, self.findChild(ComboBox, 'comboBox'))
        self.combo_box.addItems(['无限循环', '每天', '每周', '每月', '每年'])
        # 设置默认关闭奖励随机
        self.switch_button = cast(SwitchButton, self.findChild(SwitchButton, 'switchButton'))
        self.switch_button.setChecked(False)
        # 设置按钮的字
        self.yesButton.setText('确认添加')
        self.cancelButton.setText('取消')

    def init_signals(self):
        '''初始化信号'''
        self.combo_box.currentIndexChanged.connect(self.on_period_presets_changed)
        self.accepted.connect(self.on_accepted)
        self.yesButton.clicked.disconnect() # 默认的确认函数会直接关掉弹窗，为了验证数据等，所以要覆盖掉
        self.yesButton.clicked.connect(self.on_accepted)

    @Slot(int)
    def on_period_presets_changed(self, index):
        '''周期预设下拉框的槽函数'''
        return handler_period_presets_changed(self, index)
    
    @Slot(str)
    def on_icon_card_clicked(self, icon_path: str):
        '''图标卡片的槽函数'''
        return handler_icon_card_clicked(self, icon_path)
    
    @Slot()
    def on_accepted(self):
        '''确认按钮的槽函数'''
        return handler_accepted(self)