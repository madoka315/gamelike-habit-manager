from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QPixmap, Qt
import sys

from common.tools import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        # 创建 QLabel 并加载图像
        self.label = QLabel(self)
        pixmap = QPixmap(abspath_('res', 'logo.png'))  # 替换为你的图像路径
        self.label.setPixmap(pixmap)
        
        # 设置 QLabel 的大小策略，允许它调整大小
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        
        # 设置对齐方式以居中图像
        self.label.setAlignment(Qt.AlignCenter)
        
        # 创建一个垂直布局，并将 QLabel 添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())