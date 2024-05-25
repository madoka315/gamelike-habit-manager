from datetime import datetime

from qfluentwidgets import MessageBox

from db_models.user import User
from db_models.reward import RewardCompletion
from handlers.subinterfaces.handlers_interface_reward import query_reward_val_by_user
from common.cur_user import CurUser
from common.tools import TopInfoBar


def handler_reward_complete(self):
    '''兑换奖励按钮的槽函数
    
    1.验证是否足够兑换
    2.兑换成功后增加兑换记录、减少用户奖杯
    3.进行提示，更新界面
    '''
    interface = self.parent().parent().parent().parent()    # 获得父界面
    consume = self.content.get('consume')
    if query_reward_val_by_user(CurUser().uid) < consume:
        TopInfoBar.error(interface, '兑换失败', '奖杯不足，加油完成自律习惯吧')
        return

    # 二次确认
    msg = MessageBox('请确认', f"确认兑换{self.content.get('content')}吗？", interface)
    if msg.exec():
        # 更新用户的奖杯
        User.update(reward=User.reward - consume).where(User.id == CurUser().uid).execute()
        # 增加兑换记录
        RewardCompletion(
            belong_reward=self.content.get('id'),
            belong_user=CurUser().uid, 
            completed_at=datetime.now().strftime('%Y-%m-%d')
            ).save()

        TopInfoBar.success(interface, '兑换成功', f"恭喜你，兑换成功{self.content.get('content')}", duration=3000)
        interface.update_reward()
        interface.update_card_area()
    else:
        TopInfoBar.warning(interface, '提示', '取消了操作')    