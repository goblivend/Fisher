import pyautogui
import random as rd
import time

FIRST_CRAFT_POS = (684, 444)
SLOT_SIZE = (51, 51)
RESULT_POS = (1201, 448)
EMPTY_SLOT_COLOR = (139, 139, 139)

def randomize(pos) :
    return (rd.randint(10)-5 + pos[0], 
            rd.randint(10)-5 + pos[1])

def get_pos(r, c) :
    return (FIRST_CRAFT_POS[0]+SLOT_SIZE[0]*c,
            FIRST_CRAFT_POS[1]+SLOT_SIZE[1]*r)

def shiftClickOn(pos) :
    pyautogui.moveTo(pos[0], pos[1], rd.uniform(0.1, 0.3), pyautogui.easeInOutQuad)
    pyautogui.keyDown('shift')
    pyautogui.click(button=left)
    pyautogui.keyDown('shift')

def runPrevCmd() :
    pyautogui.press(args.cmd)
    pyautogui.press('up')
    pyautogui.press('enter')

def condense(args):
    for _ in range(args.nb // args.craftPerBatch) :
        for _ in range(args.craftPerBatch) :
            # shift click on good craft
            shiftClickOn(randomize(get_pos(args.row, args.column)))
            # if nothing in result runcmd and return
            if pyautogui.screenshot().getpixel(RESULT_POS) == EMPTY_SLOT_COLOR :
                runDevCmd()
                print('No more item')
                return
            # shift click on result
            shiftClickOn(randomie(RESULT_POS))
        # Open command and execute previous to store
        runPrevCmd()

def launch_condense(args) :
    try:
        res = pyautogui.confirm(text='Press OK to start condensing', title='Minecraft condenser')
        if res != 'OK' :
            print('Canceling Condensing session')
            return
        time.sleep(1)
        pyautogui.press(args.cmd)
        pyautogui.typewrite('stockall', interval=rd.uniform(0.1, 0.2))
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
            help='The number of craft batch to do')
    condenser_parser.add_argument('--batch', '-b', default='4', metavar='n', type=int, dest='craftPerBatch',
            help='The number of crafts per batch to do')
    condenser_parser.add_argument('--cmd', '-C', default='shiftright', metavar='key',
            help='The key you press to open the cmd input')

    condenser_parser.set_defaults(fun=launch_condense)


if __name__ == "__main__":
    launch_condense(None)
