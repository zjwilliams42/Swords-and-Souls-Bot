from mss import mss
from PIL import Image
import pyautogui
import time
import numpy
import cv2
import multiprocessing


def block():
    top = 500
    left = 1320
    print("block.")
    for sec in range(60000):
        # 100x150 windowed mode
        mon = {"top": top, "left": left, "width": 100, "height": 150}

        fps = 0
        sct = mss()
        last_time = time.time()

        while time.time() - last_time < 1:
            img = sct.grab(mon)
            pixels = list( zip(img.raw[2::4], img.raw[1::4], img.raw[0::4]) )

            apple = (153,39,41)
            found_apples = []
            appleat = (0,0)
            for i, pixel in enumerate(pixels):
                if i >= appleat[0] and i <= appleat[1]:
                    continue
                if pixel == apple:
                    appleat = (i, i + 2020)
                    found_apples.append(i)

            found_pixels_coords = [divmod(index, img.width) for index in found_apples]
            #for pixel in found_pixels_coords:
            if len(found_pixels_coords) > 0:
                pixel = found_pixels_coords[0]
                pyautogui.moveTo(pixel[1]+left, pixel[0]+top)
               
            fps += 1
        print(fps)

        sct.close()

def attack():
    up_pos = [1228, 526]
    up_color = (171,128,76)
    mid_pos = [1228, 628]
    mid_color = (171,128,76)
    dwn_pos = [1228, 705]
    dwn_color = (134, 95, 62)
    print("attack.")
    for sec in range(60000):
        print(str(pyautogui.position()))
        # 1x1 windowed mode
        up_mon = {"top": up_pos[1], "left": up_pos[0], "width": 5, "height": 1}
        mid_mon = {"top": mid_pos[1], "left": mid_pos[0], "width": 5, "height": 1}
        dwn_mon = {"top": dwn_pos[1], "left": dwn_pos[0], "width": 5, "height": 1}
        
        fps = 0
        sct = mss()
        last_time = time.time()

        while time.time() - last_time < 1:

            img = sct.grab(up_mon)
            pixel = list( zip(img.raw[2::4], img.raw[1::4], img.raw[0::4]) )[0]
            if pixel != up_color:
                pyautogui.press('up')
            
            img = sct.grab(mid_mon)
            pixel = list( zip(img.raw[2::4], img.raw[1::4], img.raw[0::4]) )[0]
            if pixel != mid_color:
                pyautogui.press('right')

            img = sct.grab(dwn_mon)
            pixel = list( zip(img.raw[2::4], img.raw[1::4], img.raw[0::4]) )[0]
            if pixel != dwn_color:
                pyautogui.press('down')
               
            fps += 1
        print(fps)

        sct.close()

attack()
