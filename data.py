'''
Written by Denver Conger
modified by Brandon Short

github.com/DenverConger
github.com/bshort95

conda activate SAI
pip install pydirectinput
pip install pyautogui
pip install pillow
'''
import cv2
import numpy as np
import pyautogui
import keyboard
from PIL import ImageGrab
import time
import pydirectinput
import os
i1 = 0
i2 = 0
i3 = 0
# function that returns the location of the emulator screen, 
def locate():
    # add 2 screenshots of the upper right and upper left corners to a folder
    
    emulatortop = pyautogui.locateOnScreen('Notepad.png')
    emulatorbottom = pyautogui.locateOnScreen('Notepad2.png')
    if emulatortop == None:
        print("could not find emulator top, please make sure the top is showing \n or update the 'Notepad.png' file in the screen_capture_imgs folder")
    else:
        print(emulatortop)
    
    if emulatorbottom == None:
        print("could not find emulator bottom, please make sure the top is showing \n or update the 'Notepad2.png' file in the screen_capture_imgs folder")        
    else:
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
    locate_data = top_x,top_y,bottom_w,bottom_h,img_h,img_w 
    return locate_data

# print(bottom_r)

def screen(locate_data):
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


def automate_opening():

    button = pyautogui.locateOnScreen('File.png')
    button7point = pyautogui.center(button)


    button7x, button7y = button7point
    pyautogui.click(button7x, button7y)
    time.sleep(1)
    

    # button = pyautogui.locateOnScreen('rom.png')
    # button7point = pyautogui.center(button)
    # button7x, button7y = button7point
    pyautogui.click(button7x, button7y + 50)
    time.sleep(1)

    # button = pyautogui.locateOnScreen('kart.png')
    # button7point = pyautogui.center(button)
    button7x, button7y = button7point
    pyautogui.click(button7x + 240, button7y + 50)
    time.sleep(2)

    pydirectinput.press('enter')
    time.sleep(3)
    # This locate on screen should be a screenshot of just the grayed out emulator screen so it clicks on it
    # button = pyautogui.locateOnScreen('Notepad.png')
    # button7point = pyautogui.center(button)

    # button7x, button7y = button7point
    # pyautogui.click(button7x + 40, button7y + 40)
    # pyautogui.click(button7x + 40, button7y + 40)
    # pyautogui.click(button7x + 40, button7y + 40)
    # # We only want to locate the dimentions once
    # time.sleep(3)
    pydirectinput.press('enter')
    time.sleep(6)

    print("Enter Start 1")
    pydirectinput.press('enter')
    print("Start 1 pressed")
    time.sleep(3)

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

    pydirectinput.press('l')
    time.sleep(2)
#
automate_opening()
f = open('data_catalog.csv','w')
f.write('Filename,ClassId\n')
top_x,top_y,bottom_w,bottom_h,img_h,img_w = locate()
screen_locate = locate()
time.sleep(3)
while True:

    # while i <= 50:
    if keyboard.is_pressed('a'):
        frame = screen(screen_locate)
        # remember to add the rest of your path to the folders!
        

        if i1 % 5 == 0:
            isWritten = cv2.imwrite(f'datatest\\0\Left{i1}.png', frame)
        else:
            isWritten = cv2.imwrite(f'dataset\\0\Left{i1}.png', frame)
            
        f.write('Left' + str(i1) +'.png' + ',0\n')
        print(f"Photo Number a")
        i1 += 1
            

    if keyboard.is_pressed('d'):
        frame = screen(screen_locate)
        
        if i1 % 5 == 0:
            isWritten = cv2.imwrite(f'datatest\\1\Right{i2}.png', frame)
        else:
            isWritten = cv2.imwrite(f'dataset\\1\Right{i2}.png', frame)
        
        f.write('Right' + str(i2) +'.png' + ',1\n')
        print(f"Photo Number d")
        i2 += 1
    
    elif keyboard.is_pressed('w'):
        frame = screen(screen_locate)
        
        if i3 % 5 == 0:
            isWritten = cv2.imwrite(f'datatest\\2\Straight{i3}.png', frame)
        else:
            isWritten = cv2.imwrite(f'dataset\\2\Straight{i3}.png', frame)
        

        f.write('Straight' + str(i3) +'.png' + ',2\n')
        print(f"Photo Number w")
        i3 += 1
    


            # time.sleep(1)
    frame = screen(screen_locate)
    img = ImageGrab.grab(bbox=(top_x,top_y,img_h,img_w)) #x, y, w, h
    # img_np = np.array(img)
    # img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        # print(frame[100][175])
        # These frame coordinates go [y][x] starting from the top left
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break
f.close()

'''
Written by Denver Conger

github.com/DenverConger
'''