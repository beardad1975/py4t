from 海龜模組 import *
速度('fastest')
停筆()

for 數 in range(300) :
    向前(數/5)
    右轉(360/36)
    
    亮度 = 數 % 255
    if 亮度 % 3 == 0:
        填充顏色('red')
    elif 亮度 % 3 == 1:
        填充顏色('orange')
    else:
        填充顏色('pink')
    
    開始填色()
    畫圓(數/10)
    停止填色()
    
完成()
