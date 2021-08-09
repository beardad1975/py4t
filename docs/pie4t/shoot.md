# 🔰 物理碰撞範例 - 射擊測試

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584276116?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="shoot.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

利用事件處理函式裡的for迴圈，可以一次就增加10個一排的方塊，再將每一顆發射的小球，給予高質量與高衝力，就模擬出子彈的效果。
下方的程式，利用滑鼠右鍵新增一排方塊，按任意鍵盤按鍵會射向滑鼠，請體驗一下射擊測試的有趣物理模擬。

<sup><sub>💬物理模組輔助功能，按住Ctrl鍵時，可利用滑鼠右鍵新增地形；按住Alt鍵時，可利用滑鼠右鍵移除地形</sub></sup>

--------------

### 📄 Py4t程式碼

```python
from 物理模組 import *

舞台 = 物理引擎(800,500)

def 按下滑鼠時(x, y):
    for 數 in range(10):        
        物體 = 新增方塊(寬=30,高=30)
        物體.位置 = [x, y+數*30]
        
def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, 250]
    物體.質量 = 25
    向量 = [x*15, (y-250)*15]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

--------------

### 💻 執行截圖

![執行截圖](shoot.jpg)


