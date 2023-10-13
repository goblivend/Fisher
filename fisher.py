import pyautogui
from PIL import Image
from PIL import ImageChops
import time

TESTING=True
ICON = Image.open('exercises/icon.png')
ICON_RANGE = (1872, 79, 1916, 123)
TITLE_RANGE = (720, 440, 1300, 500)
BAR_RANGE = (0, 0, 0, 0)
BAR_RANGE_1 = (748, 563, 1196, 564)
BAR_RANGE_2 = (620, 563, 1324, 564)
FISHING_RANGE = (700, 200, 1300, 600)
DURA_PIXEL = (913, 1021) #(913, 1021)
COLORS = {
  (255, 0, 0) : (253, 64, 54), # red
  (255, 165, 0) : (255, 164, 73), # orange
  (255, 255, 0) : (255, 202, 76), # yellow
  (0, 255, 64) : (52, 242, 80), # green
  (0, 255, 255) : (52, 242, 213), # aqua
  (30, 144, 255) : (82, 132, 218), # blue
  (128, 0, 255) : (201, 108, 255), # purple
}
EXERCISES = {
  (253, 64, 54) : 'Finding red', # red
  (255, 164, 73) : 'Finding orange', # orange
  (255, 202, 76) : 'Finding yellow', # yellow
  (52, 242, 80) : 'Finding green',
  (52, 242, 213) : 'Finding aqua',
  (82, 132, 218) : 'Finding blue',
  (201, 108, 255): 'Finding purple',
}
global cause
cause = ''
counter=1
enoughDura = True

def get_screen() :
  # Either screen or load premade example  (random one for later test)
  # if TESTING :
    # return Image.open('exercises/get_orange_ko.png')
  # else :
    return pyautogui.screenshot()

def is_low_durability(sc) :
  return sc.getpixel(DURA_PIXEL) == (0, 0, 0)


def is_biting(sc):
  # is slowness icon on (one or two pixels might be enough)
  icon = sc.crop(ICON_RANGE)
  # diff = ImageChops.difference(ICON, icon)
  # return all((0,0,0) == pixel for pixel in diff.getdata())
  pixels = [
     (0, 0),
     (10, 0),
     (0, 10)
  ]
  return all(ICON.getpixel(pixel) == icon.getpixel(pixel) for pixel in pixels)

def get_title(sc) :
  global cause
  global BAR_RANGE
  for pixel in sc.crop(TITLE_RANGE).getdata() :
    if pixel in COLORS :
      BAR_RANGE = BAR_RANGE_1
      return COLORS[pixel]
  BAR_RANGE = BAR_RANGE_2
  return (52, 242, 80) # green

def colorToFetch(sc) :
  # Get color of title
  color_to_find = get_title(sc)

  if TESTING :
    global cause
    cause += str(EXERCISES[color_to_find]) + ', status '

  return color_to_find

def get_cursor(sc) :
  for x in range(BAR_RANGE[0], BAR_RANGE[2]) :
    # print(sc.getpixel((x, BAR_RANGE[1])))
    if sc.getpixel((x, BAR_RANGE[1])) == (70, 71, 98) :
      return (x, BAR_RANGE[1])
  return (None, None)

def diff_color(color1, color2) :
  return abs(color1[0] - color2[0]) + abs(color1[1] - color2[1]) + abs(color1[2] - color2[2])

def validate_fishing(sc) :
  global cause
  for pixel in sc.crop(FISHING_RANGE).getdata() :
    if diff_color(pixel, (206, 41, 41))  < 20:
      # if TESTING :
      #   cause += ' already fishing'
      return
  # if TESTING :
  #   cause += ' because not fishing, clicking'
  pyautogui.click(button='right')
  time.sleep(2)


def catchfish(sc, color) :
  global cause
  global enoughDura
  (x, y) = get_cursor(sc)
  i = 0
  while x is not None and y is not None :
    if sc.getpixel((x, y-1)) == color :
      if TESTING :
        cause += '[OK]'
      pyautogui.click(button='right')
      enoughDura = not is_low_durability(sc)
      time.sleep(0.3)
      return sc
    sc = get_screen()
    (x, y) = get_cursor(sc)
    i += 1
    if i % 20 == 0 :
      if not is_biting(sc) :
        return sc

  if x is None or y is None:
    if TESTING :
      cause += ' no cursor, '
    return sc
  return sc

def fish() :
  global cause
  sc = get_screen()
  if not is_biting(sc) :
    validate_fishing(sc)
    return sc

  color = colorToFetch(sc)
  return catchfish(sc, color)

def fishing() :
    global enoughDura
    global counter
    try:
        enoughDura = not is_low_durability(get_screen())
        # start loop
        while enoughDura :
          cause = ''
          sc = fish()
          if cause != '' :
            print(cause)
          counter += 1
        print('Low durability, stop fishing')
    except KeyboardInterrupt :
        print('\nFishing session is now over.')
        print('Have a nice day!')
    return

def launch_fish(args) :
    try:
        res = pyautogui.confirm(text='Press OK to start fishing', title='Minecraft Fisher')
        if res != 'OK' :
            print('Canceling Fishing session')
            return
        time.sleep(1)
        fishing()
    except KeyboardInterrupt :
        print('Cancelling Fishing session')

def parser(sub) :
    fisher_parser = sub.add_parser('fisher',
            help='A Fishing automata that detects if you are fishing by analysing the screen, will stop when low durability')

    fisher_parser.set_defaults(fun=launch_fish)

if __name__ == '__main__' :
    launch_fish(None)
