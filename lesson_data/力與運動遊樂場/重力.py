from 物理模組 import *
舞台 = 物理引擎(800,800)
舞台.重力 = [0, 0]

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=30,高=20)
    物體.位置 = [0, 0]    
    向量 = [x, y]
    物體.施加衝力(向量)
    
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.UP :
        舞台.重力 = [0, 500]
    if 按鍵 == key.DOWN :
        舞台.重力 = [0, -500]
    if 按鍵 == key.RIGHT :
        舞台.重力 = [500, 0]
    if 按鍵 == key.LEFT :
        舞台.重力 = [-500, 0]
    
def 放開鍵盤時(按鍵, x, y):
    舞台.重力 = [0, 0]

模擬主迴圈()
