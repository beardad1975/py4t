# 🔰 海龜範例 - 花樣圓圈


: ![迴轉線條](circle_zentangle.jpg)

<br/>

-------------------------------------

## 階段1: 圓圈與角度迭代

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/78-cLvZuqTA?start=2&amp;end=196" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
速度('fastest')

for 數 in range(36) :
    畫圓(100)
    右轉(360 / 36)
    
完成()
```

<br/><br/>

-------------------------------------

## 階段2: 半徑迭代

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/78-cLvZuqTA?start=200&amp;end=262" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
速度('fastest')

for 數 in range(100) :
    畫圓(數 * 2)
    
完成()
```

<br/><br/>

-------------------------------------

## 階段3: 灰階迭代與循環

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/78-cLvZuqTA?start=266&amp;end=443" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
速度('fastest')

for 數 in range(256) :
    灰階 = 數 * 4 % 256
    畫筆顏色(灰階,灰階,灰階)
    畫圓(數 * 2)
    
完成()
```

<br/><br/>

-------------------------------------

## 階段4: 玩轉禪繞

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/78-cLvZuqTA?start=447&amp;end=623" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 海龜模組 import *
速度('fastest')

for 數 in range(256) :
    灰階 = 數 * 2 % 256
    畫筆顏色(灰階,灰階,灰階)
    畫圓(數 * 2)
    右轉(360 / 6)
    
完成()
```

<br/><br/>