# 🔰 3D範例 - 彩色螺旋

### 🎦 範例影片


<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584291964?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="color_spiral.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

### 🏷️ 原理說明

利用for迴圈，沿著x軸，產生30個長方體，除了顏色的變化以外，並利用「當更新時」的事件處理函式來改變角度。

30個長方體有一個共同的上層物件(中心)，造成只要旋轉中心，就會全部一起旋轉，產生動態的彩色螺旋。


--------------

### 📄 Py4t程式碼

```python
from 模擬3D模組 import *

中心 = 新增物體()

for x in range(30) :
    物體 = 新增立方體()
    物體.位置x = x
    物體.縮放y = 5
    物體.旋轉x = x * 10    
    物體.顏色 = 色彩.hsv(x*10, 1, 1)
    物體.上層物件 = 中心
    
def 當更新時(時間差):
    中心.旋轉x  +=  2
      
模擬主迴圈()
```

--------------

### 💻 執行截圖

![執行截圖](color_spiral.jpg)


