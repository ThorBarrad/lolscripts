import win32api
import win32con

import threading
import time

# 说明书:
# 按"T"键以启动脚本
# 按"C"或"B"键以停止脚本
# 按"Y"键开启脚本3秒钟(方便无限火力雪人3s无限e;龙王w+q秒喷)


# 总控制
active = False

# 技能释放间隔
spellCastInterval = 0.1

# 技能参数:castTime为按住时间(一次按多长时间后松手),castActive为是否启动该键
config = [
    {"keyId": "Q", "keyValue1": 81, "keyValue2": 0x10, "castTime": 0.1, "castActive": True},
    {"keyId": "W", "keyValue1": 87, "keyValue2": 0X11, "castTime": 0, "castActive": False},
    {"keyId": "E", "keyValue1": 69, "keyValue2": 0x12, "castTime": 0, "castActive": False},
    {"keyId": "R", "keyValue1": 82, "keyValue2": 0x13, "castTime": 0, "castActive": False},
    {"keyId": "T", "keyValue1": 84, "keyValue2": 0x14, "castTime": 0, "castActive": False},
    {"keyId": "2", "keyValue1": 50, "keyValue2": 0x03, "castTime": 0, "castActive": False},
]


class ExecutorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if not active:
                time.sleep(spellCastInterval)
                continue

            for item in config:
                if item["castActive"]:
                    win32api.keybd_event(item["keyValue1"], item["keyValue2"], 0, 0)
                    time.sleep(item["castTime"])
                    win32api.keybd_event(item["keyValue1"], item["keyValue2"], win32con.KEYEVENTF_KEYUP, 0)
                    # time.sleep(spellCastInterval)


class ControllerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global active
        while True:
            if win32api.GetAsyncKeyState(ord("T")) == -32767:
                active = True
            elif win32api.GetAsyncKeyState(ord("C")) == -32767 or win32api.GetAsyncKeyState(ord("B")) == -32767:
                active = False
            elif win32api.GetAsyncKeyState(ord("W")) == -32767:
                active = True
                time.sleep(3)
                active = False


thread1 = ControllerThread()
thread2 = ExecutorThread()
thread1.start()
thread2.start()
while True:
    pass
