import pyautogui
from PIL import Image,ImageGrab
# from numpy import  asarray
import  time

def hit(key):
    pyautogui.keyDown(key)
# def draw():
#     for i in range(34.45):
#         for i in range(45,65)
#
def iscolid(data):
    for i in range(350, 400):
        for j in range(400, 425):
            if data[i, j]<150 :
                return True
    return False


if __name__=="__main__":
    print("game will start in 5 sec")
    time.sleep(5)
    hit("up")
    while True :
       img = ImageGrab.grab().convert('L')
       data=img.load()
       if iscolid(data):
           hit("up")

    # print(asarray(img))
    #    for i in range(300,415):
    #       for j in range(425, 475):
    #         data[i,j]=100

    # img.show()
