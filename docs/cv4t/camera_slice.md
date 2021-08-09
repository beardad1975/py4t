# 🔰 視覺範例 - 影像格線

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584294680?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="camera_slice.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

在每一張取影的攝影機影像中，先將影像轉成灰階，再利用多維陣列的切片功能，在直向與橫向兩個方向中，每隔50點就畫一條白線(顏色值255)，就做出了影像格線的效果。

<sup><sub>💬電腦上需要有視訊攝影機</sub></sup>

--------------

### 📄 Py4t程式碼

```python
from 視覺模組 import *

攝影機 = 設置影像擷取()

while True:
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    陣列 = 彩色轉灰階(陣列)
    
    陣列[:, ::50] = 255
    陣列[::50, :] = 255
    
    顯示影像(陣列)
```

--------------

### 💻 執行截圖

![執行截圖](camera_slice.jpg)


