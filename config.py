# 数据库路径
DB_PATH = 'data/data.db'

# 登录窗提示语
TIPS = [
    "千里之行，始于足下。——老子",
    "滴水穿石，是因其坚韧不拔、锲而不舍。——约翰·伍登",
    "成功就是简单的事情重复做。——陈安之",
    "不是因为有希望才去坚持，而是因为坚持了才有希望。——阿甘正传",
    "伟大的作品不是靠力量，而是靠坚持来完成的。——塞缪尔·约翰逊",
    "耐心和持久胜过激烈和狂热。——拉·封丹",
    "罗马不是一天建成的，成功也不是一蹴而就的。——谚语",
    "习惯若不是最好的仆人，便就是最差的主人。——艾门斯",
    "成功是一系列小决定积累的结果。——罗伯特·清崎"
]

# ============================================================================

# 数据库预设数据
PREPARED_EXECUTES = [
"INSERT INTO user VALUES (1, 'admin', 'admin', 0)",

"INSERT INTO habit VALUES (1, 1, '2024-05-07', 'water.png', '喝水', 100, 0, 0, NULL, NULL)",
"INSERT INTO habit VALUES (2, 1, '2024-05-01', 'write.png', '学习', 233, 0, 1, 5, 7)",
"INSERT INTO habit VALUES (3, 1, '2024-05-08', 'sun.png', '晒太阳', 99, 1, 1, 1, 1)",

"INSERT INTO reward VALUES (1, 1, 'drink.png', '一杯奶茶', 1000)",
"INSERT INTO reward VALUES (2, 1, 'game.png', '玩一局游戏', 1000)",
"INSERT INTO reward VALUES (3, 1, 'chips.png', '吃麦当劳', 2000)",
"INSERT INTO reward VALUES (4, 1, 'sweets.png', '去吃甜品', 2000)",
"INSERT INTO reward VALUES (5, 1, 'coat.png', '一件新衣服', 5000)",
"INSERT INTO reward VALUES (6, 1, 'gift.png', '一个一直想买的小礼物', 5000)",
"INSERT INTO reward VALUES (7, 1, 'map.png', '奖励自己出去旅行', 10000)"
]

PREPARED_REWARDS = [
"INSERT INTO reward VALUES (ID, NEWUSER, 'drink.png', '一杯奶茶', 1000)",
"INSERT INTO reward VALUES (ID, NEWUSER, 'game.png', '玩一局游戏', 1000)",
"INSERT INTO reward VALUES (ID, NEWUSER, 'chips.png', '吃麦当劳', 2000)",
"INSERT INTO reward VALUES (ID, NEWUSER, 'sweets.png', '去吃甜品', 2000)",
"INSERT INTO reward VALUES (ID, NEWUSER, 'coat.png', '一件新衣服', 5000)",
"INSERT INTO reward VALUES (ID, NEWUSER, 'gift.png', '一个一直想买的小礼物', 5000)",
"INSERT INTO reward VALUES (ID, NEWUSER, 'map.png', '奖励自己出去旅行', 10000)",
]