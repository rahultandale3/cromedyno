import pyautogui
from PIL import Image,ImageGrab
from numpy import asarray
import  time

def ss():
    img = ImageGrab.grab()
    return img

def hit(key):
    pyautogui.keyDown(key)

if  __name__=="__main__":
    time.sleep(2)
    img=ss()
    data=img.load()
    print(asarray(img))
    for i in range(200,250):
        for j in range(396, 470):
               data[i,j]=0
    for i in range(175,225):
        for j in range(310, 396):
            data[i,j]=170

    img.show()
