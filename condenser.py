import pyautogui
import random as rd
import time

def condense(args):
    for _ in range(args.nb // 4) :
        for _ in range(4) :
            # shift click on good craft
            # shift click on result

        # Open command and execute previous to store

def launch_condense(args) :
    try:
        res = pyautogui.confirm(text='Press OK to start condensing', title='Minecraft condenser')
        if res != 'OK' :
            print('Canceling Condensing session')
            return
        time.sleep(1)
        condense(args)
    except KeyboardInterrupt :
        print('Cancelling Condensing session')

def parser(sub) :
    condenser_parser = sub.add_parser('condenser',
            help='condenser automata, needs you to have an empty inventory, as a last command `/stockall` and to select the last slot of yur inventory')

    condenser_parser.add_argument('--column', '-c', default='5', metavar='n', type=int,
            help='The column in the crafting book where the craft is located')
    condenser_parser.add_argument('--row', '-r', default='1', metavar='n', type=int,
            help='The row in the crafting book where the craft is located')
    condenser_parser.add_argument('--nb', '-n', default='5', metavar='n', type=int,
            help='The number of craft to do')
    condenser_parser.add_argument('--chat', '-C', default='rshift', metavar='key',
            help='The key you press to open the chat')

    condenser_parser.set_defaults(fun=launch_condense)


if __name__ == "__main__":
    launch_condense(None)
