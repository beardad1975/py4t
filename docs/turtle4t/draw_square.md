# 🔰 海龜範例 - 畫出正方形

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584282405?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="draw_square.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

正方形有4個邊及4個角。當我們利用for迴圈重複4次，讓海龜重複前進與轉直角的動作，即可畫出正方形

--------------

### 📄 Py4t程式碼

```python
from 海龜模組 import *

for 數 in range(4) :
    向前(200)
    右轉(90)
```

--------------

### 💻 執行截圖

![執行截圖](draw_square.jpg)


