from 模擬3D模組 import *

for z in range(3) :
    for y in range(3) :
        for x in range(3) :
            物體 = 新增6面貼圖方塊()
            物體.位置 = [x,y,z]
            物體.材質貼圖 = '魔方6面'
            
模擬主迴圈()
