from pprint import pprint
from time import sleep
import keyboard
import pyautogui
import win32api
import win32con

# RGB for hill: ( 41,  29,  20)
# 1 start of screen X:  752 Y:  776
# 2 end of screen  X: 1165 Y:  776
# 3 height of screen X:  752 Y:  926
# 4 width of screen X: 1165 Y:  926

x = 752
y = 776
width = 413
hight = 150

while keyboard.is_pressed('q') == False:
    pyautogui.FAILSAFE = True
    sleep(2.6)
    all_colors = []
    for ww in range(width):
        try:
            r, g, b = pyautogui.pixel(x + ww, y)
            all_colors.append([r, g, b])
        except:
            continue

    to_split = {}
    for i, j in enumerate(all_colors):
        r, g, b = j
        if r == 41 and g == 29 and b == 20:
            to_split.update({i: j})
    pprint(to_split)

    starting_index = int(list(to_split.keys())[0])

    first_cliff = None
    next_cliff = None
    for key in to_split:
        if int(key) == starting_index:
            starting_index  += 1
            first_cliff = (key, to_split[key])
        else:
            next_cliff = (key, to_split[key])
            break
    print(first_cliff)
    print(next_cliff)

    first_cliff_width = first_cliff[0]
    space_in_between = int(next_cliff[0]) - int(first_cliff[0])
    second_cliff_width = int(list(to_split.keys())[-1]) - next_cliff[0]
    stick_length = space_in_between + (second_cliff_width / 2)

    print(first_cliff_width)
    print(space_in_between)
    print(second_cliff_width)
    print(stick_length)

    pyautogui.moveTo(950, 415)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(space_in_between * 0.0032 + second_cliff_width * 0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # pyautogui.mouseDown(x=950, y=415, button='left')
    # sleep(space_in_between*0.0027)
    # pyautogui.mouseUp(x=950, y=415, button='left')
