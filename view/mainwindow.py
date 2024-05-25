from qfluentwidgets import NavigationItemPosition, FluentWindow
from qfluentwidgets import FluentIcon as FIF
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon

from view.subinterfaces.interface_habit import HabitInterface
from view.subinterfaces.interface_reward import RewardInterface
from view.subinterfaces.interface_data import DataInterface
from view.subinterfaces.interface_about import AboutInterface
from view.subinterfaces.interface_settings import SettingsInterface
from handlers.mainwindow import handle_subinterface_changed
from common.tools import TopInfoBar, abspath_
from common.cur_user import CurUser


class MainWindow(FluentWindow):
    '''基于流畅窗口的主界面'''
    def __init__(self):
        super().__init__()
        # 创建子界面
        self.interface_habit = HabitInterface(self)
        self.reward_interface = RewardInterface(self)
        self.data_interface = DataInterface(self)
        self.settings_interface = SettingsInterface(self)
        self.about_interface =  AboutInterface(self)
        self.init_signals() # 初始化窗口切换的信号
        # 初始化导航条和窗口
        self.init_navigation()
        self.init_window()

    def init_navigation(self):
        # FluentWindow的子界面添加快捷方法
        self.addSubInterface(self.interface_habit, FIF.QUICK_NOTE, '自律习惯')
        self.addSubInterface(self.reward_interface, FIF.CAFE, '奖励兑换')
        
        self.addSubInterface(self.data_interface , FIF.PIE_SINGLE, '数据中心', NavigationItemPosition.BOTTOM)
        self.navigationInterface.addSeparator(NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.settings_interface, FIF.SETTING, '调试', NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.about_interface, FIF.QUESTION, '关于', NavigationItemPosition.BOTTOM)

    def init_signals(self):
        # 当子界面切换时触发
        self.stackedWidget.currentChanged.connect(self.on_sub_changed)

    def init_window(self):
        self.resize(900, 700)
        self.setWindowTitle('自律管理')
        self.setWindowIcon(QIcon(abspath_('res', 'logo.png')))
        # 设置允许侧边导航展开的最小窗口宽度
        self.navigationInterface.setMinimumExpandWidth(900)
        # 设置导航展开宽度
        self.navigationInterface.setExpandWidth(150)
        # 默认展开导航栏
        self.navigationInterface.expand(useAni=False)
        # 弹出提示
        TopInfoBar.success(self, '', f'欢迎回来！{CurUser().user}', duration=3000)

    @Slot(int)
    def on_sub_changed(self, index: int) -> None:
        '''主窗口子界面切换的槽函数'''
        return handle_subinterface_changed(self, index)         