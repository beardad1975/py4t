# 🔰 海龜範例 - 畫出螺旋形

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584285903?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="spiral.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

利用for迴圈重複多次(300次)，海龜每次轉動的角度只有一些些(10)，並讓向前的步數越來越長(跟著數改變)，但是因為形狀會變的很巨大，所以把向前的長度縮小尺度(小10倍)，就可以畫出螺旋形了

--------------

### 📄 Py4t程式碼

```python
from 海龜模組 import *

速度(0)
開始填色()

for 數 in range(300):
    print(數)
    向前( 數/10 )
    右轉(10)

停止填色()

隱藏海龜()
```

--------------

### 💻 執行截圖

![執行截圖](spiral.jpg)


