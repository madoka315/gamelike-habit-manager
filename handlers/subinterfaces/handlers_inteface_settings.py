import sys
import subprocess

from PySide6.QtWidgets import QApplication

from db_models.base import BaseModel
from common.tools import abspath_


def handler_switch_user():
    '''切换用户按钮的槽函数
    
    退出当前的app实例,在新进程中重启应用程序
    '''
    QApplication.instance().quit()
    # 使用系统的Python解释器和入口main的路径来重启应用
    python_executable = sys.executable
    entrance = abspath_('main.py')
    args = [python_executable, entrance]   
    # 在新进程中启动应用，相当于执行了python main.py
    subprocess.run(args)


def handler_fill_preset(self, index: int):
    '''预设语句切换的槽函数
    
    要根据切换的预设，填充输入框的内容
    '''
    presets = {
        0: "",
        1: "INSERT INTO user (id, username, password, reward) VALUES ( , '', '', );",  # 插入用户的SQL语句
        2: "UPDATE user SET password = '', reward =   WHERE username = '';",  # 更新用户的SQL语句
        3: "DELETE FROM user WHERE username = '';",  # 删除用户的SQL语句
        4: "INSERT INTO habit (id, belong_user_id, created_at, icon, content, reward, is_random_reward, habit_type, type_1_limit_times, type_1_limit_days) VALUES ( , , '', '', '', , , , , );",
        5: "UPDATE habit SET belong_user_id = , created_at = '', icon = '', content = '', reward = , is_random_reward = , habit_type = , type_1_limit_times = , type_1_limit_days =  WHERE id = ;",
        6: "DELETE FROM habit WHERE id = ;",
        7: "INSERT INTO reward (belong_user_id, icon, content, consume) VALUES ( , '', '', );",
        8: "UPDATE reward SET belong_user_id = , icon = '', content = '', consume =  WHERE id = ;",
        9: "DELETE FROM reward WHERE id = ;",
    }
    self.db_setting.edit.setPlainText(presets[index])


def handler_execute_sql(self):
    '''执行SQL语句的按钮的槽函数'''
    sql = self.db_setting.edit.toPlainText()    # 获取编辑框中的sql语句
    if sql == "":
        return
    try:
        print(sql)
        # 尝试执行sql语句
        BaseModel.executes_with_foreign_keys_commit([sql])
    except Exception as e:
        # 有报错就显示在编辑框中
        self.db_setting.edit.setPlainText("错误：" + str(e))
    else:
        self.db_setting.edit.setPlainText("执行成功")