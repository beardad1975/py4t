# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------
最大層數 = 5
轉角 = 20
開始長度 = 100
長縮減率 = 0.7

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    tracer(0, 0)
        
def 遞迴(層, 長) :
    if 層 > 最大層數 :
        畫點(10, 'red')
        return
    
    向前(長)
    畫點(10, 'black')
    
    右轉(轉角)
    遞迴(層 + 1, 長 * 長縮減率)
    
    左轉(轉角 * 2)
    遞迴(層 + 1, 長 * 長縮減率)
    
    右轉(轉角)
    向後(長)
        
# 主程式 ----------------
初始設定()

for 數 in range(90+1) :
    筆跡清除()
    轉角 = 數 
    遞迴(1, 開始長度)
    update()    

完成()