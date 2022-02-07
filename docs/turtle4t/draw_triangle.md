---
hide:
  - navigation
---

# 🔰 海龜範例 - 畫出正三角形

--------------

### 🎦 示範影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/5vxxz9MCqUw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

--------------

### 🏷️ 重點說明

正三角形的內角為60度，但海龜轉彎的角為外角，所以需轉180-60，再重複3次就完成

--------------

### 📄 Py4t程式碼

```python
from 海龜模組 import *

for 數 in range(3) :
    向前(100)
    右轉(180-60)
```

--------------

### 💻 執行截圖

![執行截圖](draw_triangle.jpg)


