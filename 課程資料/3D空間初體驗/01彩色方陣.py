from 模擬3D模組 import *

for y in range(10) :
    for x in range(10-y) :
        物體 = 新增立方體()
        物體.位置x = x
        物體.位置y = y
        物體.顏色 = 色彩.hsv(x*36+y*3.6, 1, 1)
            
模擬主迴圈()
