from 物理模組 import *

舞台 = 物理引擎(800,500)

def 按下滑鼠時(x, y):
    for 序 in range(10):        
        物體 = 新增方塊(寬=30,高=30)
        物體.位置 = [x, y+序*30]
        
def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, 250]
    物體.質量 = 25
    向量 = [x*15, (y-250)*15]
    物體.施加衝力(向量)
    
模擬主迴圈()
