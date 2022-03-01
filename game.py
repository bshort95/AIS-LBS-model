import cv2
import numpy as np
import pyautogui
import keyboard
from PIL import ImageGrab
import time
import pydirectinput
import os

class Game():
    def __init__(self) -> None:
        self._locate_data = 0, 0, 0, 0, 0, 0

    
    def _set_locate(self) -> None:
        emulatortop = pyautogui.locateOnScreen('img/top_left.png')
        emulatorbottom = pyautogui.locateOnScreen('img/bottom_right.png')
        print(emulatortop)
        print(emulatorbottom)
        # Pyautogui wants the coordinates of top left plus the width
        top_x = emulatortop[0]
        top_y = emulatortop[1]
        bottom_h = emulatorbottom[1]+emulatorbottom[3]-emulatortop[1]
        # print(bottom_b)
        bottom_w = emulatorbottom[0]+emulatorbottom[2]-emulatortop[0]

        # Pillow though wants the actual coordinates of all 4 corners so we need 2 arrays of pixels
        img_h = emulatorbottom[1]+emulatorbottom[3]
        img_w = emulatorbottom[0]+emulatorbottom[2]
        self._locate_data = top_x,top_y,bottom_w,bottom_h,img_h,img_w


    def locate(self) -> tuple:
        # add 2 screenshots of the upper right and upper left corners to a folder 
        return self._locate_data

    def get_coordinates(self):
        top_x,top_y,bottom_w,bottom_h,img_h,img_w = self._locate_data

        x_offset = bottom_w*0.8
        y_offset = bottom_h*0.54

        frame = pyautogui.screenshot(region=(top_x+x_offset,top_y+y_offset,bottom_w-x_offset,bottom_h-y_offset))
        cv2.imshow("frame", np.array(frame))

    def screen(self, locate_data):
        top_x,top_y,bottom_w,bottom_h,img_h,img_w = locate_data
        im = pyautogui.screenshot(region=(top_x,top_y,bottom_w,bottom_h))
        # img = pyautogui.screenshot()

        img_np = np.array(im) 
        # # Convert RGB to BGR 
        # open_cv_image = open_cv_image[:, :, ::-1].copy()
        frame = img_np
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        # (thresh, frame) = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)
        return frame


    def automate_opening(self) -> None:
        os.startfile ("mupen64plus\mupen64plus\mupen64plus-gui.exe")
        time.sleep(2)

        button = pyautogui.locateOnScreen('img/file.png')
        button7point = pyautogui.center(button)
        
        button7x, button7y = button7point
        pyautogui.click(button7x, button7y)


        time.sleep(2)
        button = pyautogui.locateOnScreen('img/rom.png')
        button7point = pyautogui.center(button)
        button7x, button7y = button7point
        pyautogui.click(button7x, button7y)
        time.sleep(2)

        button = pyautogui.locateOnScreen('img/kart.png')
        button7point = pyautogui.center(button)
        button7x, button7y = button7point
        pyautogui.click(button7x, button7y)
        pydirectinput.press('enter')

        # time.sleep(3)
        # This locate on screen should be a screenshot of just the grayed out emulator screen so it clicks on it
        # button = pyautogui.locateOnScreen('Notepad.png')
        # button7point = pyautogui.center(button)

        # button7x, button7y = button7point
        # pyautogui.click(button7x + 40, button7y + 40)
        # pyautogui.click(button7x + 40, button7y + 40)
        # pyautogui.click(button7x + 40, button7y + 40)
        # We only want to locate the dimentions once
        
        time.sleep(3)
        pydirectinput.press('enter')
        time.sleep(6)

        print("Enter Start 1")
        pydirectinput.press('enter')
        print("Start 1 pressed")
        time.sleep(3)

        self._set_locate()

        print("Enter Start 2")
        pydirectinput.press('enter')
        print("Start 2 pressed")
        time.sleep(3)

        print("s pressing")
        pydirectinput.press('s')
        print("s pressed")
        time.sleep(2)

        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(3)

        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(3)

        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)

        pydirectinput.press('enter')
        time.sleep(2)

        pydirectinput.press('enter')
        time.sleep(2)

        # pydirectinput.press('l')