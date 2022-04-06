---
hide:
  - navigation
---

# 🔰 圓形相關國旗 - 日本國旗

## 階段1: 白色長方形3:2

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/KIVH9CxhiT4?start=0&amp;end=150" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(800, 600)

for 數 in range(2) :
    向前(300)
    左轉(90)
    向前(200)
    左轉(90)    

完成()
```

<br/><br/>

--------------

## 階段2: 紅色實心圓

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/KIVH9CxhiT4?start=152&amp;end=303" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(800, 600)

for 數 in range(2) :
    向前(300)
    左轉(90)
    向前(200)
    左轉(90)    

停筆()
走到(300 / 2, 200 / 2)
下筆()
畫點(200 * 3 / 5, 'red')
隱藏游標()

完成()

```

<br/><br/>

