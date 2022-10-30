# 🔰 海龜範例 - 海龜與樹

: ![執行截圖](fractal_tree.jpg)

--------------


<br/>

-------------------------------------

## 階段1: 程式結構

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=2&amp;end=129" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


📄 Py4t程式碼

```python
# 模組區 ----------
from 海龜模組 import *

# 全域變數 ----------

# 函式區 ----------

# 主程式 ----------


完成()
```

<br/><br/>

-------------------------------------

## 階段2: 單線遞迴

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=131&amp;end=491" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    
def 遞迴(層) :
    if 層 > 5 :
        畫點(10, 'red')
        return
    
    向前(50)
    畫點(10, 'black')
    右轉(20)
    
    遞迴(層 + 1)
    
    左轉(20)
    向後(50)
        
# 主程式 ----------------
初始設定()
遞迴(1)
完成()
```

<br/><br/>

-------------------------------------

## 階段3: 碎形樹

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=493&amp;end=976" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------
最大層數 = 5
轉角 = 20
開始長度 = 100
長縮減率 = 0.7

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    速度('fastest')	
        
def 遞迴(層, 長) :
    if 層 > 最大層數 :
        畫點(10, 'red')
        return
    
    向前(長)
    畫點(10, 'black')
    
    右轉(轉角)
    遞迴(層 + 1, 長 * 長縮減率)
    
    左轉(轉角 * 2)
    遞迴(層 + 1, 長 * 長縮減率)
    
    右轉(轉角)
    向後(長)
        
# 主程式 ----------------
初始設定()
遞迴(1, 開始長度)
完成()
```

<br/><br/>

-------------------------------------

## 階段4: 碎形動畫

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=978&amp;end=1180" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------
最大層數 = 5
轉角 = 20
開始長度 = 100
長縮減率 = 0.7

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    tracer(0, 0)
        
def 遞迴(層, 長) :
    if 層 > 最大層數 :
        畫點(10, 'red')
        return
    
    向前(長)
    畫點(10, 'black')
    
    右轉(轉角)
    遞迴(層 + 1, 長 * 長縮減率)
    
    左轉(轉角 * 2)
    遞迴(層 + 1, 長 * 長縮減率)
    
    右轉(轉角)
    向後(長)
        
# 主程式 ----------------
初始設定()

for 數 in range(90+1) :
    筆跡清除()
    轉角 = 數 
    遞迴(1, 開始長度)
    update()    

完成()
```

<br/><br/>

-------------------------------------

## 階段5: 樹與剪影

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=1182&amp;end=1645" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
# 模組區 ----------------
from 海龜模組 import *

# 全域變數 ----------------
最大層數 = 11
轉角 = 20
開始長度 = 300
長縮減率 = 0.7
開始寬度 = 40
寬縮減率 = 0.7

# 函式區 ----------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    tracer(50, 0)
    視窗設定(1000, 1000)
    畫筆顏色('black')
    停筆()
    走到(0,-500)
    bgpic('sunset1.gif')
        
def 遞迴(層, 長, 寬) :
    if 層 > 最大層數 :
        return
    
    下筆()
    畫筆尺寸(寬)
    向前(長)
    停筆()
    
    右轉(轉角)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    左轉(轉角 * 2)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    右轉(轉角)
    向後(長)
        
# 主程式 ----------------

初始設定()

遞迴(1, 開始長度, 開始寬度)    

完成()
```

<br/><br/>

-------------------------------------

## 階段6: 樹與混沌

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=1647&amp;end=2134" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
# 模組區 ---------------
from 海龜模組 import *
import random as 隨機

# 全域變數 ---------------
最大層數 = 11
開始長度 = 300
長縮減最小 = 0.6
長縮減最大 = 0.8
開始寬度 = 40
寬縮減率 = 0.7
轉角最小 = 10
轉角最大 = 40
夾角最小 = 30
夾角最大 = 70

# 函式區 ---------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    tracer(50, 0)
    視窗設定(1000, 1000)
    畫筆顏色('black')
    停筆()
    走到(0,-500)
    bgpic('sunset1.gif')

           
def 遞迴(層, 長, 寬) :
    if 層 > 最大層數 :
        return
    
    下筆()
    畫筆尺寸(寬)
    向前(長)
    停筆()
    
    轉角 = 隨機.randint(轉角最小,轉角最大)
    右轉(轉角)
    長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    夾角 = 隨機.randint(夾角最小,夾角最大)
    左轉(夾角)
    長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    右轉(夾角 - 轉角)
    向後(長)
    
# 主程式 ---------------
初始設定()

遞迴(1, 開始長度, 開始寬度)
update()

完成()
```

<br/><br/>

-------------------------------------

## 階段7: 樹與葉

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=2136&amp;end=2488" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
# 模組區 ---------------
from 海龜模組 import *
import random as 隨機

# 全域變數 ---------------
最大層數 = 11
開始長度 = 300
長縮減最小 = 0.6
長縮減最大 = 0.8
開始寬度 = 40
寬縮減率 = 0.7
轉角最小 = 10
轉角最大 = 40
夾角最小 = 30
夾角最大 = 70
葉直徑 = 6
葉層數 = 5

# 函式區 ---------------
def 初始設定() :
    左轉(90)
    速度('fastest')
    tracer(50, 0)
    視窗設定(1000, 1000)
    畫筆顏色('black')
    停筆()
    走到(0,-500)
    bgpic('sunset1.gif')
    隨機.seed(1)

def 葉() :
    畫點(葉直徑, 'black')
    for 數 in range(4) :
        向前(葉直徑 * 2)
        畫點(葉直徑, 'black')
        向後(葉直徑 * 2)
        右轉(90)
           
def 遞迴(層, 長, 寬) :
    if 層 > 最大層數 :
        return
    elif 層 > 最大層數 - 葉層數 :
        葉()
    
    下筆()
    畫筆尺寸(寬)
    向前(長)
    停筆()
    
    轉角 = 隨機.randint(轉角最小,轉角最大)
    右轉(轉角)
    長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    夾角 = 隨機.randint(夾角最小,夾角最大)
    左轉(夾角)
    長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
    遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
    
    右轉(夾角 - 轉角)
    向後(長)
    
# 主程式 ---------------
初始設定()
遞迴(1, 開始長度, 開始寬度)
update()
完成()
```

<br/><br/>


