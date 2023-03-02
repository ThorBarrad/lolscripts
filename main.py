import win32api
import win32con
import cv2
import pyautogui
import numpy as np

import threading
import time


class CollectorBuyer:
    def where_is_collector(self):
        # use cv2 to detect "collector" on the screen, returns the position of "collector"

        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        # img = cv2.imread("./Images/temp/2.png")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        template = cv2.imread("./Images/items/Black Cleaver.png")
        # template = cv2.imread("./Images/items/The Collector.png")
        # template = cv2.imread("./Images/items/Banshee's Veil.png")
        # template = cv2.imread("./Images/items/Sterak's Gage.png")
        template = cv2.resize(template, (48, 48))
        template_ = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(img_gray, template_, cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        cv2.rectangle(img, max_loc, (max_loc[0] + 48, max_loc[1] + 48), (0, 0, 255), 2)
        return max_loc[0] + 24, max_loc[1] + 24

    def buy_collector(self):
        # press "p" to open store and doubleClick target position to purchase "collector"

        # win32api.keybd_event(80, 0x19, 0, 0)
        # win32api.keybd_event(80, 0x19, win32con.KEYEVENTF_KEYUP, 0)
        # x_, y_ = win32api.GetCursorPos()
        x, y = self.where_is_collector()
        print(x, y)
        win32api.SetCursorPos([x, y])
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        return


class ControllerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.collector_buyer = CollectorBuyer()

    def run(self):
        while True:
            if win32api.GetAsyncKeyState(ord("T")) == -32767:
                self.collector_buyer.buy_collector()
            # time.sleep(0.1)


if __name__ == "__main__":
    my_collector_buyer = ControllerThread()
    my_collector_buyer.start()
