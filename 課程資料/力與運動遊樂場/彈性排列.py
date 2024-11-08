from 物理模組 import *

舞台 = 物理引擎(800,800)
球數 = 60
直徑 = 800 // 球數
半徑 = 直徑 // 2

for 數 in range(球數):
    物體 = 新增圓球(半徑)
    物體.位置 = [數 * 直徑, 400]
    if 數 % 2 == 0:
        物體.彈性 = 0.8 + 數 / 球數 * 0.2
    else:
        物體.彈性 = 0.8 + (球數-數) / 球數 * 0.2
    
模擬主迴圈()
