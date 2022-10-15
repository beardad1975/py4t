from 海龜模組 import *
from itertools import cycle
顏色陣列 = ['pink','white','orange']
顏色循環 = cycle(顏色陣列)
速度('fastest')   

for 數 in range(255) :
    停筆()
    向前(數/5)
    下筆()

    填充顏色(next(顏色循環)) 
    開始填色()
    畫圓(數/10)
    停止填色()
    
    右轉(10)    

完成()
