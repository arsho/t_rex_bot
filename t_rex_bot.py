import pyautogui
import webbrowser
import time
import numpy

blocker_color_white_bg=(83,83,83)
blocker_color_black_bg=(172,172,172)
bg_color=(247,247,247)
white_color=(255,255,255)

url = "http://google.com"
webbrowser.open(url)
time.sleep(3)
# image size is 47x50
lx, ly, w, h = pyautogui.locateOnScreen("./images/t_rex.png")
ly += h
pyautogui.press("space")
time.sleep(2)
t_rex, _, w, h = pyautogui.locateOnScreen("./images/t_rex_head.png")
t_rex += w
time.sleep(4)
rx, ry, w, h = pyautogui.locateOnScreen("./images/hi.png")
ly, ry = ry, ly
# left, top, right, bottom, t_rex
print lx, ly, rx, ry, t_rex
time.sleep(2)
pyautogui.press("space")

def jump_if_blocked():
    im = pyautogui.screenshot(region=(lx,ly, rx-lx, ry-ly))
    w, h = im.size
    count = 0
    for i in xrange(t_rex - lx + 3, (rx-lx)/2):
        for j in xrange(0, h):
            if im.getpixel((i, j)) == blocker_color_white_bg or im.getpixel((i, j)) == blocker_color_black_bg:
                count += 1
    if count*2 > (rx-lx):
        pyautogui.press("space")

try:
    while True:
        jump_if_blocked()
except KeyboardInterrupt:
    print("\n")
