from 海龜模組 import *
from itertools import cycle
顏色陣列 = ['orange','red','yellow','pink',]
顏色循環 = cycle(顏色陣列)

速度('fastest')   
for 數 in range(250) :
    顏色 = next(顏色循環)
    填充顏色(顏色)
    停筆()
    
    向前(數/5)
    下筆()
    
    開始填色()
    畫圓(數/20)
    停止填色()
    
    右轉(10)    

完成()
