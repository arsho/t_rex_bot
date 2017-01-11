import pyautogui
import webbrowser
import time
def get_pixel_colour(i_x, i_y):
    im = pyautogui.screenshot()
    return im.getpixel((i_x, i_y))

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
time.sleep(8)
rx, ry, w, h = pyautogui.locateOnScreen("./images/hi.png")
ly, ry = ry, ly
# left, top, right, bottom, t_rex
print lx, ly, rx, ry, t_rex
time.sleep(2)
pyautogui.press("space")
im = pyautogui.screenshot(region=(lx,ly, rx-lx, ry-ly))
im.show()

dragon_x=505
dragon_y=247
bird_x=495
bird_y=225
black_color=(83,83,83)
bg_color=(247,247,247)
white_color=(255,255,255)
#pyautogui.moveTo((dragon_x,dragon_y))
pyautogui.moveTo((bird_x,bird_y))
start = time.time()
try:
    while True:
        c = get_pixel_colour(dragon_x, dragon_y)
        end = time.time()
        print(end - start)
        if c!=bg_color and c!=white_color:
            end = time.time()
            print(end - start)
            print("1. Dragon found")
            pyautogui.press("space")
            continue
        c=get_pixel_colour(bird_x,bird_y)
        if c!=bg_color and c!=white_color:
            end = time.time()
            print(end - start)
            print("2. Bird found")
            pyautogui.press("space")
            continue
        c = get_pixel_colour(dragon_x, dragon_y-2)
        if c!=bg_color and c!=white_color:
            end = time.time()
            print(end - start)
            print("3. Dragon found")
            pyautogui.press("space")
            continue
        c = get_pixel_colour(dragon_x+2, dragon_y)
        if c!=bg_color and c!=white_color:
            end = time.time()
            print(end - start)
            print("4. Dragon found")
            pyautogui.press("space")
            continue

except KeyboardInterrupt:
    print("\n")
