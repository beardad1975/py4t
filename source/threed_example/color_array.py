from 模擬3D模組 import *

for x in range(10) :
    for y in range(x) :
        物體 = 新增立方體()
        物體.位置 = [x,y,0]
        物體.顏色 = 色彩.hsv(x*30+ y*5, 1, 1)
        
模擬主迴圈()
