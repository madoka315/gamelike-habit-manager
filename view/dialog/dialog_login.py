from typing import cast
import random

from PySide6.QtCore import Slot
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import ImageLabel

from ui.login_ui import Ui_Dialog
from common.tools import abspath_
from handlers.dialog.handlers_dialog_login import *
from config import TIPS


class LoginDialog(FramelessWindow, Ui_Dialog):
    '''基于FramelessWindow类的登录弹窗'''
    def __init__(self, parent=None):
        super().__init__(parent)
        # 为自身初始化ui。继承了Ui类因此可以直接setupUi(self)，相当于Ui_Dialog.setupUi(self)
        self.setupUi(self)  
        # 设置标题
        self.setTitleBar(StandardTitleBar(self))
        self.setWindowTitle('Welcome~ 😀')
        # 设置label的图像为logo，并设置大小
        # findChild是在自身中寻找名为logo_label的控件
        label = cast(ImageLabel, (self.findChild(ImageLabel, 'logo_label')))
        label.setImage(abspath_('res', 'logo.png'))
        label.scaledToHeight(64)
        # 设置随机名言提示
        self.label.setText(random.choice(TIPS))

    @Slot(bool)
    def login(self):
        '''login_button的槽函数'''
        return handler_login(self)   

    @Slot(bool)
    def register(self):
        '''register_button的槽函数'''
        return handler_register(self)     