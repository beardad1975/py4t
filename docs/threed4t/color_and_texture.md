---
hide:
  - navigation
---

# 🔰 3D程式範例 - 顏色與材質貼圖

--------------

🎦 範例影片

: <iframe width="560" height="315" src="https://www.youtube.com/embed/WwzIwKTmgfU?start=2&amp;end=416" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 模擬3D模組 import *

物體 = 新增箭頭()
物體.位置x = -2
物體.顏色 = color.rgb(255,255,0)

物體2 = 新增立方體()
物體2.材質貼圖 = '火焰.mp4'

模擬主迴圈()
```

: 註: 材質貼圖檔需先匯入至同一資料夾