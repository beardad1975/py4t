from 模擬3D模組 import *

for z in range(5) :
    for y in range(5) :
        for x in range(5) :            
            if (x + y + z) % 2  !=  0 :
                物體 = 新增6面貼圖方塊()
                物體.位置 = [x,y,z]
                           
模擬主迴圈()
