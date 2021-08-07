# 🔰 視覺範例 - 攝影機


### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584293552?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="camera.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

### 🏷️ 原理說明

設置完攝影機後，在while迴圈內，不斷的擷取影像，並顯示影像，就會產生攝影機程式。利用左右翻轉的功能讓影像變成鏡像功能，在體驗時會更加順暢。

<sup><sub>💬電腦上需要有視訊攝影機</sub></sup>

--------------

### 📄 Py4t程式碼

```python
from 視覺模組 import *

攝影機 = 設置影像擷取()

while True:
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    
    顯示影像(陣列)
    print(陣列)
    
```

--------------

### 💻 執行截圖

![執行截圖](camera.jpg)


