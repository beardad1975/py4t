# 🔰 3D範例 - 彩色方陣

--------------

### 🎦 範例影片


<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584290650?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="color_array.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

利用雙層for迴圈，沿著x軸與y軸方向，內層迴圈的次數會外層迴圈的索引改變，造成樓梯形狀的效果。

顏色的部份，將不同的索引值帶入到HSV的顏色設定，產生了彩色方陣


--------------

### 📄 Py4t程式碼

```python
from 模擬3D模組 import *

for x in range(10) :
    for y in range(x) :
        物體 = 新增立方體()
        物體.位置 = [x,y,0]
        物體.顏色 = 色彩.hsv(x*30+ y*5, 1, 1)
        
模擬主迴圈()
```

--------------

### 💻 執行截圖

![執行截圖](color_array.jpg)


