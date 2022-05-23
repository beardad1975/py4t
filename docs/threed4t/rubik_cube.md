---
hide:
  - navigation
---

# 🔰 3D程式範例 - 魔術方塊

--------------

: ![魔術方塊](rubik_cube.jpg)

<br/>

## 階段1: 魔方模型


🎦 範例影片

: <iframe width="560" height="315" src="https://www.youtube.com/embed/depPHSCWvcA?start=0&amp;end=400" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 模擬3D模組 import *

for z in range(3) :
    for y in range(3) :
        for x in range(3) :            
            物體 = 新增6面貼圖方塊()
            物體.材質貼圖 = '魔方6面.png'
            物體.位置 = [x,y,z]
                           
模擬主迴圈()
```

: 註: 材質貼圖檔需匯入並修改。

<br/><br/>

--------------------------

## 階段2: 單層轉動


🎦 範例影片

: <iframe width="560" height="315" src="https://www.youtube.com/embed/depPHSCWvcA?start=403&amp;end=736" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 模擬3D模組 import *

旋轉中心 = 新增物體()

for z in [-1, 0, 1] :
    for y in [-1, 0, 1] :
        for x in [-1, 0, 1] :            
            方塊 = 新增6面貼圖方塊()
            方塊.材質貼圖 = '魔方6面.png'
            方塊.位置 = [x,y,z]
            if y == 1:
                方塊.親代 = 旋轉中心

def 當更新時(dt):
    旋轉中心.旋轉y += 0.5
    
模擬主迴圈()
```

: 註: 材質貼圖檔需匯入並修改。

