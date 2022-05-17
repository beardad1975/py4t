---
hide:
  - navigation
---

# 🔰 3D程式範例 - 3軸縮放與旋轉

--------------

🎦 範例影片

: <iframe width="560" height="315" src="https://www.youtube.com/embed/PSL2Pi5_MTs?start=2&amp;end=354" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 模擬3D模組 import *

物體 = 新增立方體線框()
物體.縮放x = 2
物體.縮放y = 5
物體.縮放z = 10

def 當更新時(dt):
    物體.旋轉z += 1
    
模擬主迴圈()
```