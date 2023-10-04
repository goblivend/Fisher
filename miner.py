import pyautogui
import random as rd
import time


def mine(args):
    """
    Press left click and hold
    Then alternate @args.left and @args.right keys for a random amount of time between 0.1 and 0.8 seconds
    """
    pyautogui.mouseDown()
    try:
        while True :
            pyautogui.keyDown(args.left)
            time.sleep(rd.uniform(0.5, 0.8))
            pyautogui.keyUp(args.left)
            
            time.sleep(rd.uniform(0.0, 0.2))
            
            pyautogui.keyDown(args.right)
            time.sleep(rd.uniform(0.5, 0.8))
            pyautogui.keyUp(args.right)

    except KeyboardInterrupt:
        pyautogui.keyUp(args.left)
        pyautogui.keyUp(args.right)
        pyautogui.mouseUp()
        print('\nMining session is now over.')
        print('Have a nice day!')
    return

def launch_mine(args) :
    try:
        res = pyautogui.confirm(text='Press OK to start mining', title='Minecraft Miner')
        if res != 'OK' :
            print('Canceling Mining session')
            return
        time.sleep(1)
        mine(args)
    except KeyboardInterrupt :
        print('Cancelling Mining session')

def parser(sub) :
    miner_parser = sub.add_parser('miner',
            help='Mining automata for generators that require to go left-right (forward-backward..).\nDoes not handle your durability')

    miner_parser.add_argument('--left', '-l', default='a', metavar='key',
            help='The key you press to go left')
    miner_parser.add_argument('--right', '-r', default='d', metavar='key',
            help='The key you press to go right')
    miner_parser.add_argument('--length', '-L', default=5, type=int, metavar='n',
            help='The length of the mining area')

    miner_parser.set_defaults(fun=launch_mine)


if __name__ == "__main__":
    launch_mine(None)


