"""
存放玩家端设置
"""


class Settings:
    def __init__(self):
        # 窗口
        self.screen = (798, 532)  # 屏幕大小(x,y) 勿动
        self.lightBG = True  # 背景为亮色(True) 反之为暗色(False)
        self.bg_color = (226, 226, 226) if self.lightBG else (29, 29, 29)

        # 几个简短信息
        self.buttonRect = (65, 65)
        self.buttonColor = (0, 0, 0)
        self.jackpot_point = (920, 60)

        self.buttons = {
            "menu": {
                (34, 34): (2, 3),
                (760, 33): (2,4),
                (760, 98): (2,5),
                (760, 163): (2,6),
                (760, 228): (2,7),
                (760, 293): (2,8),
            },
            "collections": {(34, 34): (2,3)},
        }
        self.petpet_stats = {
            0:(2,9),
            1:(2,10),
            2:(2,11),
            3:(5,5),
            4:(5,6),
            5:(5,7),
            6:(5,8),
            7:(5,9),
            8:(5,10),
            9:(5,11)
        }