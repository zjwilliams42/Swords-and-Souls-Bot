from mss import mss
import pyautogui
import time
import numpy

def start(seconds, task):
    screen = list(getScreenLocation())
    print(screen)
    for sec in range(seconds):

        fps = 0
        sct = mss()
        last_time = time.time()

        monitor = {"top": screen[1], "left": screen[0], "width": 800, "height": 600}

        while time.time() - last_time < 1:
            frame = numpy.array(sct.grab(monitor), dtype=numpy.uint8)[..., [2, 1, 0]]
            
            cooldowns = task(screen, frame)
            fps += 1

        sct.close()
        print(fps)

def getScreenLocation():
    input ("Press enter when mouse is over the top-left corner of the game.")
    return pyautogui.position()

def attack(screen, frame):
    pixel = [tuple(frame[220][335]), tuple(frame[220][338])]
    if pixel[0] != (151, 114, 71) or pixel[1] != (151, 114, 71):
        pyautogui.press('up')

    pixel = [tuple(frame[360][335]), tuple(frame[360][338])]
    if pixel[0] != (167, 111, 74) or pixel[1] != (167, 111, 74):
        pyautogui.press('right')

    pixel = [tuple(frame[430][335]), tuple(frame[430][338])]
    if pixel[0] != (146, 103, 67) or pixel[1] != (146, 103, 67):
        pyautogui.press('down')

    pixel = [tuple(frame[340][50]), tuple(frame[335][50])]
    if pixel[0] != (195, 134, 96) or pixel[1] != (195, 134, 96):
        pyautogui.press('left')

start(600, attack)