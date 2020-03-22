#Automatically plays the Dino game @ http://www.trex-game.skipser.com/


from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayButn = (480, 410)
    dinosaur = (264, 434 )
    # x coor is where dino should start to jump
    #y coor is the lowest obstacle. 433 lowest cacti
def restartGame():
    pyautogui.click(Coordinates.replayButn)
    pyautogui.keyDown("down")

def pressSpace():
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp("space")
    pyautogui.keyDown("down")


# (335,438)________
#       |          |
#       |    box   |
#       |          |
#       |__________| (355,449)
#x1,y1 = 335, 435
#x2,y2 = ,355,446


def imageGrab():
    box = (Coordinates.dinosaur[0]+60, Coordinates.dinosaur[1],
           Coordinates.dinosaur[0]+150, Coordinates.dinosaur[1]+5 )
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors ())
    print(a.sum())
    return(a.sum())

def main():
    restartGame()
    while True:
        if(imageGrab() != 697):
            pressSpace()
            time.sleep(0.02)
main()
