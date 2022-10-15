from 海龜模組 import *

速度('fastest')

def 葉(半徑, 角度) :
    開始填色()
    for 數 in range(2) :
        畫弧(半徑, 角度)
        左轉(180-角度)
    停止填色()
    
填充顏色('orange')
for 數 in range(12) :
    葉(200,100)
    左轉(30)

左轉(20)
填充顏色('red')
for 數 in range(12) :
    葉(150,100)
    左轉(30)

左轉(20)
填充顏色('white')
for 數 in range(12) :
    葉(100,100)
    左轉(30)
  
左轉(20)
填充顏色('yellow')
for 數 in range(12) :
    葉(50,100)
    左轉(30)

    
    
    


完成()
