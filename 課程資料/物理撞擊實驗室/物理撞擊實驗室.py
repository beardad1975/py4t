from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y):
    print('柱')
    for 直 in range(10) :
        物體 = 新增方塊(20, 20)
        物體.位置 = [x, y+ 直*20]
        物體.密度 = 1

def 牆(x, y):
    print('牆')
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(20, 20)
            物體.位置 = [x + 橫*20, y + 直*20]
            物體.密度 = 1

def 金字塔(x, y):
    print('金字塔')
    for 橫 in range(10) :
        for 直 in range(10-橫) :
            物體 = 新增方塊(20, 20)
            物體.位置 = [x+ 橫*20+直*20/2, y+ 直*20]
            物體.密度 = 1

def 按下滑鼠時(x, y):
    print('發射')
    if y > 400:
        print('實驗組 撞擊不同結構')
        物體 = 新增圓球(20)
        物體.位置 = [0, y]
        物體.密度 = 1
        物體.速度 = [2000, 200]
    else:
        print('對照組')
        物體 = 新增圓球(20)
        物體.位置 = [0, y]
        物體.密度 = 1
        物體.速度 = [2000, 200]
        
            
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.UP :
        金字塔(x, y)    
    if 按鍵 == key.LEFT :
        柱(x, y)        
    if 按鍵 == key.RIGHT :
        牆(x, y)    
    if 按鍵 == key.SPACE :
        print('慢..動..作..')
        舞台.慢動作 = True
        
           
def 放開鍵盤時(按鍵, x, y):
    if 按鍵 == key.SPACE :
        舞台.慢動作 = False
        
模擬主迴圈()