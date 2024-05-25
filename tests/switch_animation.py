import sys
from PySide6.QtWidgets import (QApplication, QDialog, QVBoxLayout, QPushButton, QStackedWidget, QLabel)
from PySide6.QtCore import QPropertyAnimation, QRect

class TransitionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置堆叠布局
        self.stack = QStackedWidget(self)
        self.layout = QVBoxLayout(self)

        # 创建两个界面
        self.page1 = QLabel("这是界面 1")
        self.page2 = QLabel("这是界面 2")

        # 添加界面到堆叠布局
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        # 按钮用于切换界面
        self.button = QPushButton("切换界面", self)
        self.button.clicked.connect(self.start_transition)

        self.layout.addWidget(self.stack)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.current_page = 0

    def start_transition(self):
        # 创建动画
        self.anim = QPropertyAnimation(self.stack, b"geometry")
        self.anim.setDuration(1000)  # 动画持续时间

        start_rect = self.stack.geometry()
        end_rect = QRect(-start_rect.width(), start_rect.y(), start_rect.width(), start_rect.height())

        # 设置动画起始和结束位置
        self.anim.setStartValue(start_rect)
        self.anim.setEndValue(end_rect)
        self.anim.finished.connect(self.switch_page)
        self.anim.start()

    def switch_page(self):
        # 切换界面
        self.current_page = 1 - self.current_page
        self.stack.setCurrentIndex(self.current_page)

        # 重置位置
        start_rect = self.stack.geometry()
        start_rect.moveLeft(self.width())
        self.stack.setGeometry(start_rect)

        # 从新位置开始动画返回
        self.anim.setDirection(QPropertyAnimation.Backward)
        self.anim.setStartValue(start_rect)
        end_rect = QRect(0, start_rect.y(), start_rect.width(), start_rect.height())
        self.anim.setEndValue(end_rect)
        self.anim.start()


app = QApplication(sys.argv)
dialog = TransitionDialog()
dialog.show()
sys.exit(app.exec())
