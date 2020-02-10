import numpy as np

import pyautogui
import time


def main():
    x = 0
    while x < 4:
        pyautogui.screenshot("C:\\Users\\Katlic\\Pictures\\auto_screen_shots\\images" + str(x) + ".png")
        x += 1
        time.sleep(2)
    pass



if __name__ == '__main__':
    main()