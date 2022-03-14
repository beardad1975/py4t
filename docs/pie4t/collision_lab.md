---
hide:
  - navigation
---

# 🔰 專題範例 - 物理撞擊實驗室 

--------------

## 階段1: 程式結構

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=2&amp;end=260" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


🏷️ 重點說明

: 匯入物理模組，並模擬主迴圈到程式最後，設定舞台寬800高800

: 建立程式的基本結構，先以print替代實際的程式碼。在按下滑鼠時會'發射'；
按下鍵盤時有多種情形，如果按鍵是向左鍵會設置障礙物'柱'，如果是向右鍵會設置障礙物'牆'，
如果是向上鍵則會設置障礙物'金字塔'


📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
            
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
    if 按鍵 == key.RIGHT :
        print('牆')
    if 按鍵 == key.UP :
        print('金字塔')

def 按下滑鼠時(x, y):
    print('發射')

模擬主迴圈()
```




<br/><br/>

--------------


## 階段2: 發射撞擊物

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=263&amp;end=378" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 新增圓球，半徑為20，開始的位置在[0, y]，可以依滑鼠高度從左向右射出。

: 設定衝力從左向右發射[800, 0]，因有重力的影響，所以增加一些上升速度(200)，讓子彈不要太快掉落，最後將圓球速度加快至速度2000

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
    if 按鍵 == key.RIGHT :
        print('牆')
    if 按鍵 == key.UP :
        print('金字塔')

def 按下滑鼠時(x, y):
    print('發射')
    物體 = 新增圓球(半徑=20)
    物體.位置 = [0, y]
    向量 = [2000, 200]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

<br/><br/>

--------------



## 階段3: 障礙物-柱

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=380&amp;end=590" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 定義柱函式(參數為滑鼠座標x, y)，加入呼叫柱函式(引數 x, y)

: 柱函式的內容為新增方塊(寬高均20)，位置設為滑鼠座標(x, y)，再加上迴圈(重複10次)，
迴圈變數改為直(加進變數清單)，依迴圈變數「直」，在位置y增加高度的倍數


📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]
        
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
    if 按鍵 == key.UP :
        print('金字塔')

def 按下滑鼠時(x, y):
    print('發射')
    物體 = 新增圓球(半徑=20)
    物體.位置 = [0, y]
    向量 = [2000, 200]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

<br/><br/>

--------------



## 階段4: 障礙物-牆

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=595&amp;end=722" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 在柱函式的基礎上，再定義牆函式，
呼叫牆函式(引數為滑鼠座標x, y)

: 原有柱程式再加上新迴圈並重複10次，迴圈變數改為「橫」(加進變數清單)，依迴圈變數橫，在位置x增加，寬度的倍數


📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]

def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')

def 按下滑鼠時(x, y):
    print('發射')
    物體 = 新增圓球(半徑=20)
    物體.位置 = [0, y]
    向量 = [2000, 200]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

<br/><br/>

--------------



## 階段5: 障礙物-金字塔

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=725&amp;end=886" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 在函式牆的基礎上定義金字塔函式，並呼叫金字塔函式(引數 x, y)

: 先做出樓梯形狀，內層迴圈次數，依照變數橫．再將樓梯左右反向，內層的迴圈次數，以最大值10減去。最後做出金字塔，每往上一層，橫排方塊就會往右半個寬度(依變數直) 


📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]

def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]

def 金字塔(x, y) :
    for 橫 in range(10) :
        for 直 in range(10 - 橫) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫 + 10 * 直, y + 20 * 直]

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')
        金字塔(x, y)

def 按下滑鼠時(x, y):
    print('發射')
    物體 = 新增圓球(半徑=20)
    物體.位置 = [0, y]
    向量 = [2000, 200]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

<br/><br/>

--------------



## 階段6: 實驗組與對照組

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=888&amp;end=1014" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 新增地面的地形在高度400之處，實驗組(上方)高度是大於400，對照組(下方)則是高度不大於400

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]

def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]

def 金字塔(x, y) :
    for 橫 in range(10) :
        for 直 in range(10 - 橫) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫 + 10 * 直, y + 20 * 直]

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')
        金字塔(x, y)

def 按下滑鼠時(x, y):
    print('發射')
    
    if y > 400 :
        print('實驗組')
        物體 = 新增圓球(半徑=20)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
    else :
        print('對照組')
        物體 = 新增圓球(半徑=20)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)

模擬主迴圈()
```

註：地形需自行新增

<br/><br/>

--------------



## 階段7: 撞擊測試

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=1016&amp;end=1267" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 不同結構的撞擊測試，撞擊柱、牆、金字塔等障礙物

: 不同高度的撞擊測試，以高及低的位置撞擊

: 不同圓球大小的撞擊測試

: 不同密度的撞擊測試，先將方塊的新增程式都加入密度為1，以密度0.1圓球撞擊測試，以密度10圓球撞擊測試

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]
        物體.密度 = 1

def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]
            物體.密度 = 1

def 金字塔(x, y) :
    for 橫 in range(10) :
        for 直 in range(10 - 橫) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫 + 10 * 直, y + 20 * 直]
            物體.密度 = 1

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')
        金字塔(x, y)

def 按下滑鼠時(x, y):
    print('發射')
    
    if y > 400 :
        print('實驗組')
        物體 = 新增圓球(半徑=60)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
        物體.密度 = 10
    else :
        print('對照組')
        物體 = 新增圓球(半徑=60)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
        物體.密度 = 1

模擬主迴圈()
```

<br/><br/>

--------------



## 階段8: 慢動作

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=1269&amp;end=1415" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 新增鍵盤放開時的事件函式，慢動作不成立，恢復成正常動作

: 在鍵盤按下時的事件函式，新增如果按下空白鍵，慢動作就會成立

: 準備慢動作的測試，對照組正常撞擊，實驗組會有慢動作撞擊(按住空白鍵時)

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]
        物體.密度 = 1

def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]
            物體.密度 = 1

def 金字塔(x, y) :
    for 橫 in range(10) :
        for 直 in range(10 - 橫) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫 + 10 * 直, y + 20 * 直]
            物體.密度 = 1

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')
        金字塔(x, y)
    if 按鍵 == key.SPACE :
        舞台.慢動作 = True

def 放開鍵盤時(按鍵, x, y):
    舞台.慢動作 = False

def 按下滑鼠時(x, y):
    print('發射')
    
    if y > 400 :
        print('實驗組')
        物體 = 新增圓球(半徑=60)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
        物體.密度 = 10
    else :
        print('對照組')
        物體 = 新增圓球(半徑=60)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
        物體.密度 = 1

模擬主迴圈()
```

<br/><br/>

--------------



## 階段9: 子彈射擊

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/dIjMzArPjqI?start=1417&amp;end=1521" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


🏷️ 重點說明

: 準備子彈射擊，此模擬難度較高，易失敗

: 將速度增加至100000，障礙物需置於球瞬間抵達位置

: 測試，對照組正常速度射擊，實驗組高速射擊

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 柱(x, y) :
    for 直 in range(10) :
        物體 = 新增方塊(寬=20,高=20)
        物體.位置 = [x, y + 20 * 直]
        物體.密度 = 1
        
def 牆(x, y) :
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫, y + 20 * 直]
            物體.密度 = 1
            
def 金字塔(x, y) :
    for 橫 in range(10) :
        for 直 in range(10 - 橫) :
            物體 = 新增方塊(寬=20,高=20)
            物體.位置 = [x + 20 * 橫 + 10 * 直, y + 20 * 直]
            物體.密度 = 1

def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.LEFT :
        print('柱')
        柱(x, y)
    if 按鍵 == key.RIGHT :
        print('牆')
        牆(x, y)
    if 按鍵 == key.UP :
        print('金字塔')
        金字塔(x, y)
    if 按鍵 == key.SPACE :
        舞台.慢動作 = True

def 放開鍵盤時(按鍵, x, y):
    舞台.慢動作 = False

def 按下滑鼠時(x, y):
    print('發射')
    
    if y > 400 :
        print('實驗組')
        物體 = 新增圓球(半徑=10)
        物體.位置 = [0, y]
        向量 = [100000, 200]
        物體.施加衝力(向量)
        物體.密度 = 1
    else :
        print('對照組')
        物體 = 新增圓球(半徑=10)
        物體.位置 = [0, y]
        向量 = [2000, 200]
        物體.施加衝力(向量)
        物體.密度 = 1

模擬主迴圈()
```

<br/><br/>

--------------

