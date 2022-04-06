---
hide:
  - navigation
---

# 🔰 星形相關國旗 - 越南國旗

## 階段1: 紅色長方形

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/KL5OYhQZq-E?start=2&amp;end=173" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(800, 600)

填充顏色('red')
開始填色()
for 數 in range(2) :
    向前(300)
    左轉(90)
    向前(200)
    左轉(90)    
停止填色()

完成()
```

<br/><br/>

--------------

## 階段2: 黃色5角星形

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/KL5OYhQZq-E?start=175&amp;end=404" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(800, 600)

填充顏色('red')
開始填色()
for 數 in range(2) :
    向前(300)
    左轉(90)
    向前(200)
    左轉(90)    
停止填色()

停筆()
走到(90,120)
下筆()

填充顏色('yellow')
畫筆顏色('yellow')
開始填色()
for 數 in range(5) :
    向前(120)
    右轉(180 - 180 / 5)    
停止填色()

隱藏游標()

完成()

```

<br/><br/>
