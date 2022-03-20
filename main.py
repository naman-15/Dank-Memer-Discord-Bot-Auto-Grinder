import pyautogui
import keyboard
import time
import random

you = True
x,y = pyautogui.size()

def main():
    time.sleep(2)
    
    x2 = 30 / 100 * x
    y2 = 90/100 *y
    pyautogui.click(x2,y2)
    
    keyboard.write('pls pm')
    keyboard.press_and_release('enter')

    time.sleep(3)
    
    list1 = [1, 2, 3, 4, 5]
    number = random.choice(list1)
    if number == 1:
        x1 = 55/100 *x
        y1 = 83/100 *y
    elif number == 2:
        x1 = 45/100 *x
        y1 = 83/100 *y
    elif number == 3 :
        x1 = 40/100 *x
        y1 = 83/100 *y
    elif number == 4:
        x1 = 35/100 *x
        y1 = 83/100 *y
    elif number == 5:
        x1 = 30/100 *x
        y1 = 83/100 *y
    else:
        print("Problem")
    
    pyautogui.click(x1, y1)
    
    pyautogui.click(x2,y2)
    
    time.sleep(10)

    keyboard.write('pls crime')
    keyboard.press_and_release('enter')
    
    list2 = [1, 2, 3]
    number = random.choice(list2)
    if number == 1:
        x3 = 30/100 *x
        y3 = 83/100 *y
    elif number == 2:
        x3 = 35/100 *x
        y3 = 83/100 *y
    elif number == 3 :
        x3 = 40/100 *x
        y3 = 83/100 *y
    else:
        print("Problem")
    time.sleep(3)  
    pyautogui.click(x3, y3 )

    pyautogui.click(x2,y2)
    time.sleep(10)

    keyboard.write('pls scout')
    keyboard.press_and_release('enter')
    
    list3 = [1, 2, 3]
    number = random.choice(list3)
    if number == 1:
        x4 = 30/100 *x
        y4 = 83/100 *y
    elif number == 2:
        x4 = 35/100 *x
        y4 = 83/100 *y
    elif number == 3 :
        x4 = 40/100 *x
        y4 = 83/100 *y
    else:
        print("Problem")
    time.sleep(3)  
    pyautogui.click(x4, y4 )
    pyautogui.click(x2,y2)
    time.sleep(10)
    
    keyboard.write('pls beg')
    keyboard.press_and_release('enter')
    time.sleep(10)
    keyboard.write('pls hunt')
    keyboard.press_and_release('enter')
    time.sleep(10)
    keyboard.write('pls fish')
    keyboard.press_and_release('enter')
    time.sleep(10)
while you == True:
    main()
