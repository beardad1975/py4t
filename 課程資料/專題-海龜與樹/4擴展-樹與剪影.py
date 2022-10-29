# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------
最大層數 = 9
開始長度 = 300
開始寬度 = 30

轉角 = 30
長縮減率 = 0.7
寬縮減率 = 0.7

剪影色 = 'black'

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    視窗設定(1000, 1000)
    畫筆顏色(剪影色)
    停筆()
    走到(0,-500)
    tracer(50, 0)
    bgpic('sunset1.gif')
        
def 遞迴(層, 長, 寬) :
    if 層 > 最大層數 :
#         畫點(10, 'red')
        return
    
    下筆()
    畫筆尺寸(寬)
    向前(長)
    停筆()
#     畫點(10, 'black')
    
    右轉(轉角)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    左轉(轉角 * 2)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    右轉(轉角)
    向後(長)
        
# 主程式 ----------------

初始設定()

遞迴(1, 開始長度, 開始寬度)    

完成()
