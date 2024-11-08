from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]
        物體.密度 = 1

def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]
            物體.密度 = 1

def 金字塔(x, y) :
    for 橫 in range(10) :
        for 直 in range(10 - 橫) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫 + 10 * 直, y + 20 * 直]
            物體.密度 = 1

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')
        金字塔(x, y)
    if 按鍵 == key.SPACE :
        舞台.慢動作 = True

def 放開鍵盤時(按鍵, x, y):
    舞台.慢動作 = False

def 按下滑鼠時(x, y):
    print('發射')

    if y > 400 :
        print('實驗組')
        物體 = 新增圓球(半徑=10)
        物體.位置 = [0, y]
        向量 = [100000, 200]
        物體.施加衝力(向量)
        物體.密度 = 1
    else :
        print('對照組')
        物體 = 新增圓球(半徑=10)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
        物體.密度 = 1

模擬主迴圈()
