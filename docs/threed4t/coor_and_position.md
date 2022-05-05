---
hide:
  - navigation
---

# 🔰 3D程式範例 - 空間座標與位置

--------------

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/xnP4PEybUJ0?start=2&amp;end=390" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼


```python
from 模擬3D模組 import *

物體 = 新增立方體()
物體.位置x = 1
物體.位置y = 2
物體.位置z = 3

物體2 = 新增球體()
物體2.位置 = [-1,-2,-3]

模擬主迴圈()
```