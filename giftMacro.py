from ppadb.client import Client
from PIL import Image
import numpy
import time
import cv2
import mss
import random
import pyautogui

sct = mss.mss()

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
device = devices[0]

gift_count = 0

while True:
    start = time.time()

    #scrcpy: xs350 ys200
    #OpenCV: xc700 yc420-20

    #e.g. red: xc224 yc260-20 -> RGB(BGR) print(img[240][224])
    #To make sure that img[240][224] gives the right RGB(BGR) value: width height xs112 ys120 -> Confirm that img[240][224] is out of bounds, while print(img[239][223]) gives the same RGB(BGR) value.

    scr = sct.grab({
        'left': 0,
        'top': 450,
        'width': 350, #xs350 red112 blue130 yellow182 kakao299 background315
        'height': 200 #ys200 red120 blue147 yellow139 kakao27 background113
    })
    img = numpy.array(scr)
    ""
    cv2.namedWindow('Computer Vision', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Computer Vision', 350, 200)
    cv2.imshow('Computer Vision', img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
    ""
    #print(img[240][224]) #img[yc][xc]
    #print(img[294][260])
    #print(img[278][364])
    #print(img[54][598])
    #print(img[226][630])
    pixel_red = int(img[240][224][0:1]) #xc224 yc260-20
    pixel_blue = int(img[294][260][0:1]) #xc260 yc314-20
    pixel_yellow = int(img[278][364][0:1]) #xc364 yc298-20
    pixel_kakao = int(img[54][598][0:1]) #xc598 yc74-20
    pixel_background = int(img[226][630][0:1]) #xc630 yc246-20

    print("")
    if 33-5<pixel_red<39+5 and 187-5<pixel_blue<191+5 and 7-5<pixel_yellow<9+5 and 50-5<pixel_kakao<50+5 and 38-5<pixel_background<38+5:
        print("선착순 발견! 고고!")
        pyautogui.click(190, 740)
        end_first = time.time()
        print(end_first - start)
        pyautogui.click(190, 740)
        end_second = time.time()
        print(end_second - start)
        pyautogui.click(190, 740)
        end_third = time.time()
        print(end_third - start)
        
        print(pixel_red) #33~39
        print(pixel_blue) #187~191
        print(pixel_yellow) #7~9
        print(pixel_kakao) #50
        print(pixel_background) #38

        time.sleep(8)
        
        image = device.screencap()
        with open('scrsht_result.png', 'wb') as f:
            f.write(image)
        image = Image.open('scrsht_result.png')
        image = numpy.array(image, dtype=numpy.uint8)
        
        pixel_1 = int(image[813][392][0:1])
        pixel_2 = int(image[813][392][1:2])
        pixel_3 = int(image[813][392][2:3])
        pixel_4 = int(image[923][363][0:1])
        pixel_5 = int(image[923][65][1:2])
        pixel_6 = int(image[923][200][1:2])
        pixel_7 = int(image[550][65][1:2])

        if 255-5<pixel_1 and 151-5<pixel_2<151+5 and 112-5<pixel_3<112+5 and 143-5<pixel_4<143+5:
            print("노치쓰")
            device.shell('input touchscreen tap 1010 150')
            
            print(pixel_1) #255
            print(pixel_2) #151
            print(pixel_3) #112
            print(pixel_4) #143
            
        if (pixel_5 != pixel_6) and 235-5<pixel_7<235+5:
            print("바다쓰!!")
            gift_count += 1
            device.shell('input touchscreen tap 1010 150')
            device.shell('input touchscreen tap 540 2200')
            random_msg = random.randint(1, 3)
            if random_msg == 1:
                device.shell("input text 'dhkdn!!%srkatkgkqslek!'")
            else:
                device.shell("input text 'dhdP!!%srkatkgkqslek!'")
            device.shell('input touchscreen tap 1010 1470')
            device.shell('input keyevent 4')
            
            print(pixel_5)
            print(pixel_6)
            print(pixel_7) #235
         
        while True:
            image = device.screencap()
            with open('scrsht_return.png', 'wb') as f:
                f.write(image)
            image = Image.open('scrsht_return.png')
            image = numpy.array(image, dtype=numpy.uint8)
            
            pixel_a = int(image[2191][475][0:1])
            pixel_b = int(image[2191][954][0:1])
        
            print("톡방으로 돌아가는 중")
            print(pixel_a) #45
            print(pixel_b) #45
        
            if 45-5<pixel_a<45+5 and 45-5<pixel_b<45+5:
                break
            else:
                device.shell('input keyevent 4')
                time.sleep(2)

    else:
        print("선착순 기다리는 중")
        end = time.time()
        print(end - start)
        
        print(pixel_red) #33~39
        print(pixel_blue) #187~191
        print(pixel_yellow) #7~9
        print(pixel_kakao) #50
        print(pixel_background) #38
    
    print("받은 선착순 수:", gift_count)
