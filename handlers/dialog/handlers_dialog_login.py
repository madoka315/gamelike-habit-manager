from qfluentwidgets import LineEdit

from view.mainwindow import MainWindow
from db_models.user import User
from db_models.reward import Reward
from common.tools import TopInfoBar
from common.cur_user import CurUser
from config import PREPARED_REWARDS


def handler_login(self):
    '''login_button的槽函数'''
    input_user = self.findChild(LineEdit, 'lineEdit_usr').text().strip()  # 获取填写的用户名和密码
    input_password = self.findChild(LineEdit, 'lineEdit_pwd').text().strip()
    # 查询用户，验证登录
    db_user = User.select().where(User.username == input_user).first()
    if not db_user:
        # 用户不存在
        TopInfoBar.error(self, title='登录失败',content='用户不存在，请先注册')
    elif db_user.password == input_password:       
        # 用户存在，验证密码通过
        CurUser.set_user(db_user.id)   # 设置当前用户到系统中
        w = MainWindow()    # 创建主界面
        self.close()
        w.show()
    else:
        # 否则弹错误提示
        TopInfoBar.error(self, title='登录失败',content='用户名或密码错误') 


def handler_register(self):            
    '''register_button的槽函数'''
    user = self.findChild(LineEdit, 'lineEdit_usr').text().strip()
    password = self.findChild(LineEdit, 'lineEdit_pwd').text().strip()
    if user == '' or password == '':
        # 未填写完整
        TopInfoBar.warning(self, title='', content='请直接填写用户名密码再点击注册')
        return
    # 判重
    db_user = User.select().where(User.username == user).first()
    if db_user:
        TopInfoBar.error(self, title='注册失败', content='用户已被注册')
    # 通过检查，进行数据库插入
    else:
        new_user = User(username=user, password=password, reward=0)
        new_user.save()

        # 也插入一下奖励兑换的预设数据
        # 需要替换掉原始数据中的id和用户字段
        updated_rewards = []
        cur_id = len(Reward.select()) + 1
        for i in PREPARED_REWARDS:
            i = i.replace("NEWUSER", str(new_user.id))
            i = i.replace("ID", str(cur_id))
            updated_rewards.append(i)
            cur_id += 1  
        Reward.executes_with_foreign_keys_commit(updated_rewards)
        TopInfoBar.success(self, title='注册成功', content='可以点击登录了')            