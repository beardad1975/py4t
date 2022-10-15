from 海龜模組 import *
from itertools import cycle
速度('fastest')
停筆()

顏色陣列 = ['red','white','pink','white','orange','white','green','white',]
顏色循環 = cycle(顏色陣列)

def 色塊(邊長):
    填充顏色(next(顏色循環))    
    開始填色()
    for 數 in range(5) :
        向前(邊長)
        右轉(180-180/5)
    停止填色()
    
for 數 in range(300, 0, -4) :
    色塊(數*3)
    右轉(360/5)    

完成()
