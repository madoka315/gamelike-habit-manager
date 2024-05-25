from PySide6.QtWidgets import QApplication

from view.dialog.dialog_login import LoginDialog
from common.initdb import init_db
from common.tools import abspath_
from config import DB_PATH


if __name__ == '__main__':
    db = abspath_(DB_PATH) # 数据库绝对路径
    init_db(db)   # 初始化数据库
    app = QApplication()
    dialog = LoginDialog()  # 创建登录对话框
    dialog.show() 
    app.exec()