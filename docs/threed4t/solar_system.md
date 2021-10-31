# 🔰 3D範例 - 太陽系

--------------

### 🎦 範例影片

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/640791564?h=a28b42497e&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="solor_system.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

球體的3d模型，加上太陽系星球的材質貼圖，看起來就像個星球。調整球體的尺寸、中心點偏移與旋轉，就可以實做出簡易的太陽系公轉，把學習到的知識實踐出來，是不是很有趣呢！(由君毅中學林老師 提供)

--------------

### 📄 Py4t程式碼

本範例程式的執行需配合星球的貼圖，下載連結：🔗[程式及貼圖檔](solar_system.zip)

```python
#由君毅中學林老師 提供
from 模擬3D模組 import *
舞台 = 模擬3D引擎(800,500)

#太陽
太陽 = 新增球體()
太陽.材質貼圖 = '太陽'
太陽.縮放 = 5

#地球
地球 = 新增球體()
地球.材質貼圖 = '地球'
地球.縮放 = 1
地球.中心點偏移 = [0,0,4]
中心 = 新增物體()
地球.上層物件 = 中心
中心.旋轉z = 23.5

#火星
火星 = 新增球體()
火星.材質貼圖 = '火星'
火星.縮放 = 0.7
火星.中心點偏移 = [4,0,5]

#木星
木星 = 新增球體()
木星.材質貼圖 = '木星'
木星.縮放 = 2
木星.中心點偏移 = [0,0,3]

#星空
星空 = 新增內面貼圖球體()
星空.材質貼圖 = '星空'
星空.縮放 = 500

#公轉自轉
def 當更新時(時間差):
    太陽.旋轉y  -=  0.05    
    地球.旋轉y  -=  2
    火星.旋轉y -= 1.3
    木星.旋轉y  -=  1

模擬主迴圈()

```

--------------

### 💻 執行截圖

![執行截圖](solar_system.jpg)


