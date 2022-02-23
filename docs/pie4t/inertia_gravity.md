---
hide:
  - navigation
---

# 🔰 物理碰撞範例 - 重力控制

--------------

## 階段1: 無重力狀態

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/I_i5OyGIObQ?start=0&amp;end=343" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 設定舞台寬為800，高為800，並先新增方塊

: 加入新增事件函式-按下滑鼠時，包含原本的新增方塊程式，並將物體設定為滑鼠位置

: 測試不同的重力加速度。設定重力向上(重力加速度[0,800])，再測試無重力(重力加速度[0,0])

: 設定方塊的角速度(每秒轉幾度)，先使用常數，再使用隨機模組，將角速度的數值隨機取數(-360~360)

📄 Py4t程式碼


```python
from 物理模組 import *
import random as 隨機

舞台 = 物理引擎(800,800)
舞台.重力 = [0, 0]

def 按下滑鼠時(x, y):
    物體 = 新增方塊()
    物體.位置 = [x, y]
    物體.角速度 = 隨機.randint(-360,360)
    
模擬主迴圈()
```



<br/><br/>

--------------


## 階段2: 重力搬運


🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/I_i5OyGIObQ?start=347&amp;end=667" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 使用事件處理函式-放開鍵盤時，裡面執行的是保持無重力狀態
，再來是事件處理函式按下鍵盤時，將重力都設為向下

: 按向上鍵重力向上，按向下鍵重力向下。再加入按向右鍵重力向右，按向左鍵重力向左

: 建立搬運地形，控制重力，將物體搬到不同的位置

📄 Py4t程式碼

```python
from 物理模組 import *
import random as 隨機

舞台 = 物理引擎(800,800)
舞台.重力 = [0, 0]

def 按下滑鼠時(x, y):
    物體 = 新增方塊()
    物體.位置 = [x, y]
    物體.角速度 = 隨機.randint(-360,360)
    
def 放開鍵盤時(按鍵, x, y):
    舞台.重力 = [0, 0]
    
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.UP :
        舞台.重力 = [0, 800]
    if 按鍵 == key.DOWN :
        舞台.重力 = [0, -800]
    if 按鍵 == key.RIGHT :
        舞台.重力 = [800, 0]
    if 按鍵 == key.LEFT :
        舞台.重力 = [-800, 0]
        
模擬主迴圈()

```

註：搬運地形需自行建立(操作如階段2影片)

