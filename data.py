'''
Written by Denver Conger

github.com/DenverConger

conda activate SAI
pip install pydirectinput
pip install pyautogui
pip install pillow

Remember to throw your first batch of laps into the test folder and name them on the test_classes.csv
'''

import cv2
import numpy as np
import pyautogui
import keyboard
from PIL import ImageGrab
import time
import pydirectinput
import os
from game import Game

i1 = 0
i2 = 0
i3 = 0
# # N
# def game.locate():
#     # add 2 screenshots of the upper right and upper left corners to a folder
#     emulatortop = pyautogui.locateOnScreen('Notepad.png')
#     emulatorbottom = pyautogui.locateOnScreen('Notepad_2.png')
#     print(emulatortop)
#     print(emulatorbottom)
#     # Pyautogui wants the coordinates of top left plus the width
#     top_x = emulatortop[0]
#     top_y = emulatortop[1]
#     bottom_h = emulatorbottom[1]+emulatorbottom[3]-emulatortop[1]
#     # print(bottom_b)
#     bottom_w = emulatorbottom[0]+emulatorbottom[2]-emulatortop[0]

#     # Pillow though wants the actual coordinates of all 4 corners so we need 2 arrays of pixels
#     img_h = emulatorbottom[1]+emulatorbottom[3]
#     img_w = emulatorbottom[0]+emulatorbottom[2]
#     locate_data = top_x+200,top_y+200,bottom_w-400,bottom_h-350,img_h-350,img_w-400 
#     return locate_data

# # print(bottom_r)

# def game.screen(locate_data):
#     top_x,top_y,bottom_w,bottom_h,img_h,img_w = locate_data
#     im = pyautogui.screenshot(region=(top_x,top_y,bottom_w,bottom_h))
#     # img = pyautogui.screenshot()

#     img_np = np.array(im) 
#     # # Convert RGB to BGR 
#     # open_cv_image = open_cv_image[:, :, ::-1].copy()
#     frame = img_np
#     frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
#     # (thresh, frame) = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
#     return frame


# def automate_opening():
#     os.startfile ("mupen64plus\mupen64plus\mupen64plus-gui.exe")
#     time.sleep(2)

#     button = pyautogui.locateOnScreen('file.png')
#     button7point = pyautogui.center(button)
    
#     button7x, button7y = button7point
#     pyautogui.click(button7x, button7y)


#     time.sleep(2)
#     button = pyautogui.locateOnScreen('rom.png')
#     button7point = pyautogui.center(button)
#     button7x, button7y = button7point
#     pyautogui.click(button7x, button7y)
#     time.sleep(2)

#     button = pyautogui.locateOnScreen('kart.png')
#     button7point = pyautogui.center(button)
#     button7x, button7y = button7point
#     pyautogui.click(button7x, button7y)
#     pydirectinput.press('enter')

#     # time.sleep(3)
#     # This game.locate on game.screen should be a screenshot of just the grayed out emulator game.screen so it clicks on it
#     # button = pyautogui.locateOnScreen('Notepad.png')
#     # button7point = pyautogui.center(button)

#     # button7x, button7y = button7point
#     # pyautogui.click(button7x + 40, button7y + 40)
#     # pyautogui.click(button7x + 40, button7y + 40)
#     # pyautogui.click(button7x + 40, button7y + 40)
#     # We only want to game.locate the dimentions once
#     time.sleep(3)
#     pydirectinput.press('enter')
#     time.sleep(6)

#     print("Enter Start 1")
#     pydirectinput.press('enter')
#     print("Start 1 pressed")
#     time.sleep(3)

#     print("Enter Start 2")
#     pydirectinput.press('enter')
#     print("Start 2 pressed")
#     time.sleep(3)

#     print("s pressing")
#     pydirectinput.press('s')
#     print("s pressed")
#     time.sleep(2)

#     pydirectinput.press('enter')
#     time.sleep(1)
#     pydirectinput.press('enter')
#     time.sleep(1)
#     pydirectinput.press('enter')
#     time.sleep(3)

#     pydirectinput.press('enter')
#     time.sleep(1)
#     pydirectinput.press('enter')
#     time.sleep(3)

#     pydirectinput.press('enter')
#     time.sleep(1)
#     pydirectinput.press('enter')
#     time.sleep(1)

#     pydirectinput.press('enter')
#     time.sleep(2)

#     pydirectinput.press('enter')
#     time.sleep(2)

#     pydirectinput.press('l')

game = Game()

game.automate_opening()
top_x,top_y,bottom_w,bottom_h,img_h,img_w = game.locate()
screen_locate = game.locate()
time.sleep(3)
while True:

    # while i <= 50:
    if keyboard.is_pressed('a'):
        frame = game.screen(screen_locate)
        # remember to add the rest of your path to the folders!
        isWritten = cv2.imwrite(f'training/1\Left{i1}.png', frame)
        print(f"Photo Number a")
        i1 += 1
    if keyboard.is_pressed('d'):
        frame = game.screen(screen_locate)
        isWritten = cv2.imwrite(f'training/2\Right{i2}.png', frame)
        print(f"Photo Number d")
        i2 += 1
    elif keyboard.is_pressed('w'):
        frame = game.screen(screen_locate)
        isWritten = cv2.imwrite(f'training/0\Straight{i3}.png', frame)
        print(f"Photo Number w")
        i3 += 1
    


            # time.sleep(1)
    frame = game.screen(screen_locate)
    img = ImageGrab.grab(bbox=(top_x,top_y,top_x+img_w, top_y+img_h)) #x, y, w, h
    img_np = np.array(img)
    # img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        # print(frame[100][175])
        # These frame coordinates go [y][x] starting from the top left
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0Xff == ord('q'):
        break


'''
Written by Denver Conger

github.com/DenverConger
'''