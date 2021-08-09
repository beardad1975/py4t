# 🔰 物理碰撞範例 - 操控重力

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584278505?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="gravity.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

重力是一種加速度，會影響重力場中的每個物體，當我們改變重力加速度的向量(左右及上下)，就可以像魔法師一樣，讓物體飛起來。下方的程式利用滑鼠左鍵新增物體，一開始的重力是零，會像在太空中的物體。當使用上下左右鍵操控重力時，物體受到不同重力的影響。

<sup><sub>💬物理模組輔助功能，按住Ctrl鍵時，可利用滑鼠右鍵新增地形；按住Alt鍵時，可利用滑鼠右鍵移除地形</sub></sup>

--------------

### 📄 Py4t程式碼

```python
from 物理模組 import *
from random import randint

舞台 = 物理引擎(800,800)
舞台.重力 = [0, 0]

def 按下滑鼠時(x, y):
    物體 = 新增方塊()
    物體.位置 = [x, y]
    物體.速度 = [randint(-100,100), randint(-100,100)]
    物體.角速度 = randint(-100,100)
        
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.UP :
        舞台.重力 = [0, 800]
    if 按鍵 == key.DOWN :
        舞台.重力 = [0, -800]
    if 按鍵 == key.RIGHT :
        舞台.重力 = [800, 0]
    if 按鍵 == key.LEFT :
        舞台.重力 = [-800, 0]

def 放開鍵盤時(按鍵, x, y):
    舞台.重力 = [0, 0]
    
模擬主迴圈()
```

--------------

### 💻 執行截圖

![執行截圖](gravity.jpg)


