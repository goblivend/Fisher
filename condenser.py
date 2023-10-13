import pyautogui
import random as rd
import time

FIRST_CRAFT_POS = (684, 444)
SLOT_SIZE = (51, 51)
RESULT_POS = (1201, 448)
EMPTY_SLOT_COLOR = (139, 139, 139)

def randomize(pos) :
    return (rd.randint(0, 30)-15 + pos[0], rd.randint(0, 30)-15 + pos[1])

def get_pos(r, c) :
    return (FIRST_CRAFT_POS[0]+SLOT_SIZE[0]*c,
            FIRST_CRAFT_POS[1]+SLOT_SIZE[1]*r)

def shiftClickOn(pos) :
    pyautogui.moveTo(pos[0], pos[1], rd.uniform(0.05, 0.07))
    print('shift clicking on', pos, pyautogui.position())
    pyautogui.keyDown('shift')
    pyautogui.click(button='left')
    pyautogui.keyUp('shift')

def runPrevCmd(args) :
    pyautogui.press(args.chat)
    time.sleep(0.1)
    pyautogui.typewrite('/stockall', interval=0.01)
    time.sleep(0.1)
    pyautogui.press('enter')

def condense(args):
    print('Starting condensing')
    for _ in range(args.nb) :
        pyautogui.click(button='right')
        for _ in range(args.craftPerBatch) :
            print('crafting')
            # shift click on good craft
            shiftClickOn(randomize(get_pos(args.row, args.column)))
            # if nothing in result runcmd and return
            if pyautogui.screenshot().getpixel(RESULT_POS) == EMPTY_SLOT_COLOR :
                runPrevCmd(args)
                print('No more item')
                return
            # shift click on result
            shiftClickOn(randomize(RESULT_POS))
        # Open command and execute previous to store
        pyautogui.press('9')
        runPrevCmd(args)

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

    condenser_parser.add_argument('--column', '-c', default='0', metavar='n', type=int,
            help='The column in the crafting book where the craft is located')
    condenser_parser.add_argument('--row', '-r', default='0', metavar='n', type=int,
            help='The row in the crafting book where the craft is located')
    condenser_parser.add_argument('--nb', '-n', default='1', metavar='n', type=int,
            help='The number of craft batch to do')
    condenser_parser.add_argument('--batch', '-b', default='4', metavar='n', type=int, dest='craftPerBatch',
            help='The number of crafts per batch to do')
    condenser_parser.add_argument('--chat', '-C', default='t', metavar='key',
            help='The key you press to open the chat input')

    condenser_parser.set_defaults(fun=launch_condense)


if __name__ == "__main__":
    launch_condense(None)
