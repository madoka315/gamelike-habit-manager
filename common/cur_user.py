from PySide6.QtWidgets import QApplication

from db_models.user import User


class CurUser():
    '''app当前用户属性管理'''
    def __init__(self) -> None:
        pass

    @property
    def uid(self) -> int:
        '''返回当前登录的用户id'''
        if __name__ == '__main__':
            return 1
        return QApplication.instance().property('loggedInUser')
    
    @property
    def user(self) -> str:
        '''返回当前登录的用户名'''
        user = User.select().where(User.id == self.uid).first()
        return user.username

    @staticmethod
    def set_user(uid: int):
        '''设置当前登录的用户id'''
        QApplication.instance().setProperty('loggedInUser', uid)


if __name__ == '__main__':
    a = CurUser().user
    print(a)
