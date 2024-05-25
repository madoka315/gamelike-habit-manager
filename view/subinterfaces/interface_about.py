from typing import cast

from PySide6.QtWidgets import QFrame
from qfluentwidgets import ImageLabel

from ui.interface_about_ui import Ui_Frame
from common.tools import abspath_


class AboutInterface(QFrame, Ui_Frame):
    '''关于子界面'''
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)  # 初始化UI
        self.init_display()

    def init_display(self):
        '''初始化显示'''
        # 设置logo
        logo_label = cast(ImageLabel, self.findChild(ImageLabel, 'logoLabel'))
        logo_label.setImage(abspath_('res', 'logo.png'))
        logo_label.setFixedSize(64, 64)