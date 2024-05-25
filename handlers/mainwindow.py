def handle_subinterface_changed(self, index: int):
    '''主窗口子界面切换的槽函数'''
    if index == 0:
        # index为0，切换到了习惯界面，更新卡片区域
        self.interface_habit.update_card_area()
    if index == 1:
        # index为1，切换到了奖励界面，需要更新奖杯值的显示和卡片区域
        self.reward_interface.update_reward()
        self.reward_interface.update_card_area()
    if index == 2:  
        # index为2，切换到了数据界面，需要更新数据    
        self.data_interface.update_all()