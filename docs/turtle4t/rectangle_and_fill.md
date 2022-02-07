---
hide:
  - navigation
---


# 🔰 海龜範例 - 長方形及填色

--------------

### 🎦 示範影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/xL_e-SZklWo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

--------------

### 🏷️ 原理說明

畫出長邊及短邊，再重複2次完成長方形

在畫線之前，先開始填色，畫完形狀後，再停止填色。另外也可以設定填充顏色以及畫線顏色。

--------------

### 📄 Py4t程式碼

```python
from 海龜模組 import *

畫筆顏色('red')
填充顏色('yellow')

開始填色()
for 數 in range(2) :
    向前(100)
    右轉(90)
    向前(50)
    右轉(90)
停止填色()
```

--------------

### 💻 執行截圖

![執行截圖](rectangle_and_fill.jpg)


