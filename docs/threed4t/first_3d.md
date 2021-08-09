# 🔰 3D範例 - 3D方塊

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584289430?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="first_3d.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

建立一個3D立方體模型物體，可以改變物體的顏色，也可以利用下方的攝影機視角操作方式來觀看，按下Ctrl鍵可以切換顯示座標格線。

![3D視角](3d_manual.jpg)

--------------

### 📄 Py4t程式碼

下方程式的第1行及第9行，為3D框架程式的必要部分。

```python
from 模擬3D模組 import *

物體 = 新增立方體()
物體.顏色 = 色彩.orange

模擬主迴圈()
```

--------------

### 💻 執行截圖

![執行截圖](first_3d.jpg)


