# 模組區 ----------------
from 海龜模組 import *
import random as 隨機

# 全域變數 ----------------
最大層數 = 12
開始長度 = 200
開始寬度 = 20

轉角最小 = 10
轉角最大 = 40
夾角最小 = 30
夾角最大 = 60
長縮減最小 = 0.7
長縮減最大 = 0.8
寬縮減最小 = 0.65
寬縮減最大 = 0.75
花直徑 = 5
葉直徑 = 14
葉層數 = 7
隨機種子 = 22 #55 #88 # 888 # 777 4321

花色陣列 = ['#ff0b03', '#f77c99', '#ffc9d6',]
葉色陣列 = ['#3cba1a','#00fc3f','#d9fa48',]  

# 函式區 ----------------
def 初始設定() :
    隨機.seed(隨機種子)
    左轉(90)
    速度('fastest')
    視窗設定(1000, 800)
    畫筆顏色('#825e09')
    背景顏色('#bbf2fc')
    停筆()
    走到(0,-400)
    tracer(0, 0)

def 花() :
    花色 = 隨機.choice(花色陣列)
    for 數 in range(4) :
        畫點(花直徑, 花色)
        向前(花直徑)
    向後(花直徑 * 4)
    
def 葉() :
    葉色 = 隨機.choice(葉色陣列)
    畫點(葉直徑, 葉色)
    for 數 in range(4) :   
        向前(葉直徑)
        畫點(葉直徑, 葉色)            
        向後(葉直徑)    
        左轉(90)
    
def 遞迴(層, 長, 寬) :
    if 層 > 最大層數 :
        花()
        return
    elif 250 < 方向() <290 :
        return
    elif 層 > 最大層數 - 葉層數  :
        葉()
    
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