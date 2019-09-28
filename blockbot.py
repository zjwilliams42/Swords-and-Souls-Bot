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