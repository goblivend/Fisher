import pyautogui
import random as rd
import time


def mine():
    """
    Press left click and hold
    Then alternate 'A' and 'D' keys for a random amount of time between 0.1 and 0.8 seconds
    """
    pyautogui.alert(text='Press OK to start mining', title='Minecraft Miner', button='OK')
    time.sleep(1)
    pyautogui.moveTo(None, 0, 0.5)
    pyautogui.mouseDown()
    try:
        while True :
            pyautogui.keyDown('a')
            time.sleep(rd.uniform(0.5, 0.8))
            pyautogui.keyUp('a')
            time.sleep(rd.uniform(0.0, 0.2))
            pyautogui.keyDown('d')
            time.sleep(rd.uniform(0.5, 0.8))

            pyautogui.keyUp('d')
    except KeyboardInterrupt:
        pyautogui.keyUp('a')
        pyautogui.keyUp('d')
        pyautogui.mouseUp()
    return


if __name__ == "__main__":
    mine()
