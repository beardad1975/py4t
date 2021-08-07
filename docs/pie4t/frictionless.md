# 🔰 物理碰撞範例 - 無摩擦力

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584272762?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="frictionless.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

### 🏷️ 原理說明

無摩擦力的世界，按滑鼠左鍵會新增方塊

<sup><sub>💬物理模組輔助功能，按住Ctrl鍵時，可利用滑鼠右鍵新增地形；按住Alt鍵時，可利用滑鼠右鍵移除地形</sub></sup>

--------------

### 📄 Py4t程式碼

```python
from 物理模組 import *

舞台 = 物理引擎(800,800)

def 按下滑鼠時(x, y):
    物體 = 新增方塊()
    物體.位置 = [x, y]
    物體.摩擦 = 0
    
模擬主迴圈()
```

--------------

### 💻 執行截圖

![執行截圖](frictionless.jpg)


