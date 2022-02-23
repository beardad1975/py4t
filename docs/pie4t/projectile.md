---
hide:
  - navigation
---

# 🔰 物理碰撞範例 - 噴射拋體

--------------

## 階段1: 拋體運動


🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/UgJ6ed8H03Q?start=2&amp;end=192" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


🏷️ 重點說明

: 設定舞台的寬度800，高度800，並移除預除地形(按住alt鍵，滑鼠右鍵移除)

: 新增事件函式-按下滑鼠時，新增圓球(指定半徑)，設定位置螢幕左下角(0, 0)，最後設定速度向量為滑鼠的 x, y

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下滑鼠時(x, y):
    物體 = 新增圓球(半徑=20)
    物體.位置 = [0, 0]
    物體.速度 = [x, y]

模擬主迴圈()
```

<br/><br/>

--------------

## 階段2: 連續噴射


🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/UgJ6ed8H03Q?start=193&amp;end=383" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


🏷️ 重點說明

: 將球的位置修改為400, 0(螢幕中間下方)，並修改速度 (x-400 ,y)，以及速度整個變為2倍。
事件處理函式修改成-拖曳滑鼠時，來產生噴射效果。


📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 拖曳滑鼠時(x, y, dx, dy):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [400, 0]
    物體.速度 = [(x - 400) * 2, y * 2]
    
模擬主迴圈()

```

<br/><br/>

