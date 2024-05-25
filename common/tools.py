import os

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLayout
from qfluentwidgets import InfoBar
from qfluentwidgets.components.widgets.info_bar import InfoBarPosition


# === Widgets === #
class TopInfoBar(InfoBar):
    '''顶层弹窗的InfoBar'''
    @classmethod
    def error(cls, parent, title, content, orient=Qt.Horizontal, isClosable=True, duration=1000, position=InfoBarPosition.TOP):
        return super().error(title, content, orient, isClosable, duration, position, parent)
    
    @classmethod
    def warning(cls, parent, title, content, orient=Qt.Horizontal, isClosable=True, duration=1000, position=InfoBarPosition.TOP):
        return super().warning(title, content, orient, isClosable, duration, position, parent)
    
    @classmethod
    def success(cls, parent, title, content, orient=Qt.Horizontal, isClosable=True, duration=1000, position=InfoBarPosition.TOP):
        return super().success(title, content, orient, isClosable, duration, position, parent)


# ===CommonMethods=== #
def abspath_(*args) -> str:
    '''得到某资源绝对路径'''
    # 项目根目录路径
    proj_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
            ))
    # 依次拼接参数中的路径
    result = proj_root
    for arg in args:
        if type(arg) is not str:
            raise TypeError('参数必须是str')
        result = os.path.join(result, arg)
    return result


def remove_widget_by_layout(layout: QLayout):
    '''移除某个布局下的所有子控件'''
    # 遍历Layout，去除旧的组件
    for index in reversed(range(layout.count())):
        widget_to_rm = layout.itemAt(index).widget()
        if widget_to_rm:    # 找到布局内组件的实例
            layout.removeWidget(widget_to_rm)
            widget_to_rm.deleteLater()  # qt提供的安全地安排组件删除的方法


if __name__ == '__main__':
    print(abspath_('res', 'logo.png'))