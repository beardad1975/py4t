# 模組區 ----------------
from 海龜模組 import *
import random as 隨機

# 全域變數 ----------------
最大層數 = 11
開始長度 = 300
開始寬度 = 30

轉角最小 = 10
轉角最大 = 40
夾角最小 = 30
夾角最大 = 70
長縮減最小 = 0.6
長縮減最大 = 0.8
寬縮減最小 = 0.65
寬縮減最大 = 0.85

剪影色 = 'black'

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    視窗設定(1000, 1000)
    畫筆顏色(剪影色)
    隱藏游標()
    停筆()
    走到(0,-500)
    tracer(100, 0)
    bgpic('sunset1.gif')
        
def 遞迴(層, 長, 寬) :
    if 層 > 最大層數 :
        return
    
    下筆()
    畫筆尺寸(寬)
    向前(長)
    停筆()

    轉角 = 隨機.randint(轉角最小,轉角最大)
    右轉(轉角)
    長縮減率 = 隨機.uniform(長縮減最大, 長縮減最小)
    寬縮減率 = 隨機.uniform(寬縮減最大, 寬縮減最小)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    夾角 = 隨機.randint(夾角最小,夾角最大)
    左轉(夾角)
    長縮減率 = 隨機.uniform(長縮減最大, 長縮減最小)
    寬縮減率 = 隨機.uniform(寬縮減最大, 寬縮減最小)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    右轉(夾角 - 轉角)
    向後(長)
        
# 主程式 ----------------

初始設定()

遞迴(1, 開始長度, 開始寬度)    

完成()
