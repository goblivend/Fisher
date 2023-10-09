import pyautogui
import random as rd
import time


def takeABreak(t: int) :
    print('Taking a', t, 's break')
    pyautogui.mouseUp()
    time.sleep(t)
    pyautogui.mouseDown()

def takeBreaks(args) :
    chances = args.break_chances
    times = args.break_times
    for i in range(len(chances)) :
        if chances[i] == 0 : 
            continue
        if rd.randint(0, chances[i]) == 0 :
            takeABreak(rd.uniform(times[2*i], times[2*i+1]))

def mine(args):
    """
    Press left click and hold
    Then alternate @args.left and @args.right keys for a random amount of time between 0.1 and 0.8 seconds
    """
    pyautogui.mouseDown()
    start = time.time()
    try:
        while True :
            if args.time > 0 and time.time() - start > args.time :
                print('Mined for {} seconds'.format(time.time() - start))
                raise KeyboardInterrupt
            takeBreaks(args)

            pyautogui.keyDown(args.left)
            time.sleep(rd.uniform(0.5, 0.8))
            pyautogui.keyUp(args.left)

            time.sleep(rd.uniform(0.0, 0.2))
            takeBreaks(args)
            pyautogui.keyDown(args.right)
            time.sleep(rd.uniform(0.5, 0.8))
            pyautogui.keyUp(args.right)

    except KeyboardInterrupt:
        pyautogui.keyUp(args.left)
        pyautogui.keyUp(args.right)
        pyautogui.mouseUp()
        # Display the time spent mining with hours, minutes and seconds
        print('\nMining session is now over, after {} hours, {} minutes and {} seconds'.format(
            int((time.time() - start) // 3600),
            int(((time.time() - start) // 60) % 60),
            int((time.time() - start) % 60)))
        print('Have a nice day!')
    return

def validate_breaks(args) :
    if len(args.break_times) != 2 * len(args.break_chances) :
        print('Invalid size of `--break-time` {}, compared to `--break-chances` {}'.format(len(args.break_times), len(args.break_chances)))
        return false

    valid = True
    for i in range(len(args.break_chances)) :
        min_time = args.break_times[2*i]
        max_time = args.break_times[2*i+1]
        if max_time < min_time :
            print('Breaks: {}th break has wrong timings min [{}] is higher than max [{}]'.format(i, min_time, max_time))
            valid = False
    return valid

def launch_mine(args) :
    if not validate_breaks(args) :
        return

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
    miner_parser.add_argument('--time', '-t', default=-1, type=int, metavar='n',
        help='Time to mine in seconds (-1 for infinite)')
    miner_parser.add_argument('--break-chances', '-b', default=[], type=int, metavar='n', nargs='*',
            help='Chances to take a break while mining: matching --breack-time times (0 for none, must be half of --break-times length)')
    miner_parser.add_argument('--break-times', '-T', default=[], type=float, metavar='n', nargs='*', 
        help='Bounds of breaks, must be twice as big as --break-chances (1 min and 1 max per chance)')
    




    miner_parser.set_defaults(fun=launch_mine)


if __name__ == "__main__":
    launch_mine(None)
