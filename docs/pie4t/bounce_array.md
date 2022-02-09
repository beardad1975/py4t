---
hide:
  - navigation
---

# 🔰 物理碰撞範例 - 彈性排列

--------------

## 階段1: 固定球數

--------------

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U9DAN6NbkbY?start=0&amp;end=240" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 建立物理舞台，寬度800，高度800。先產生1顆圓球，設定球的位置y為400(高度)，按住Ctrl 觀察座標(原點在左下角)。
: 產生10顆圓球，半徑為40。設定x位置是迴圈變數的80倍，設定遞增的彈性是迴圈變數除以10(恢復系數的上限為1)。

--------------

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

for 數 in range(10) :
    物體 = 新增圓球(40)
    物體.位置 = [數 * 80, 400]
    物體.彈性 = 數 / 10
    
模擬主迴圈()
```

--------------


## 階段2: 變數模式識別

--------------

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U9DAN6NbkbY?start=243&amp;end=406" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 改為20顆圓球後，其他數字會依球數改變，如直徑半徑會減半，彈性為迴圈變數除以球數。

: 接著模式識別，找出變數之間規律，建立球數、直徑、半徑變數，會使用到去掉小數的除法(//)，讓除相關變數保持整數。

--------------

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
球數 = 20
直徑 = 800 // 球數
半徑 = 直徑 // 2

for 數 in range(球數) :
    物體 = 新增圓球(半徑)
    物體.位置 = [數 * 直徑, 400]
    物體.彈性 = 數 / 球數
    
模擬主迴圈()
```

--------------

## 階段3: 不同波動變化

--------------

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U9DAN6NbkbY?start=408&amp;end=660" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 讓彈性的變化在0.8到1之間，做法是恢復係數由基本的0.8起跳，變化幅度上限為0.2。
: 測試不同的球數(勿過大)，如40顆或80顆
: 最後可試試彈性反向排列，由大到小(做法以最大值來減)；或是交錯排列，奇數球彈性正向排列，而偶數球彈性反向排列(利用%除法取餘數來判斷奇偶數)。

--------------

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
球數 = 80
直徑 = 800 // 球數
半徑 = 直徑 // 2

for 數 in range(球數) :
    物體 = 新增圓球(半徑)
    物體.位置 = [數 * 直徑, 400]
    if 數 % 2 == 0 :
        物體.彈性 = 0.8 + (球數 - 數) / 球數 * 0.2
    else :
        物體.彈性 = 0.8 + 數 / 球數 * 0.2
    
模擬主迴圈()
```

--------------
