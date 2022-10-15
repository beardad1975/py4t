from 海龜模組 import *
速度('fastest')

for 數 in range(500) :
    亮度 = 數*3 % 255
    畫筆顏色(亮度,亮度,亮度)
    
    畫圓(數)
    右轉(360/6)
    
完成()
