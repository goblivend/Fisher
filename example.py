import pyautogui
import PIL.Image

testing=True

def get_screen() :
  # Either screen or load premade example  (random one for later test)
  if testing :
    # for test: print(filename, end=': ')

def is_biting(sc: PIL.Image):
  # is slowness icon on (one or two pixels might be enough)
  # return sc.crop((...))
  return True

def get_title(sc) :
  # for pixel in area :
  #   if pixel in colors :
  #     return pixel
  # might try superpose different exercises to check if one pixel could get it completely

def colorToFetch(sc) :
  # Get color of title
  title_color = get_title(sc)
  
  if testing : 
    print(exercises[title_color], end=', status: ')
  
  return green if title_color == white else title_color 

def get_cursor(sc) :
  #for pixel in line : # cursor top in color line
  #  if pixel == black :
  #    return pos

def validate_fishing(sc) :
  for pixel in fishing_area :
    if pixel == red : 
      if testing :
        print(' already fishing')
      return
  if testing :
    print(' because not fishing, clicking')
  else :
    click()


def fish() :
  sc = get_screen()
  if not is_biting(sc) :
    if testing :
      print('notBiting', end='')
    validate_fishing(sc)
    return

  color = colorToFetch(sc)

  (x, y) = get_cursor(sc)

  if sc.pixel((x, y+1)) == color :
    
    if testing :
      print('[OK]') # add colors might help visualise
    else :
      click()
    return
  if testing :
    print('[KO]')


if __name__ == '__main__' :
    # sleep for 2/3s for time to switch
    # start loop
    while True :
      fish()
      # sleep a bit (ex: 300ms)
