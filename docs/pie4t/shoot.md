---
hide:
  - navigation
---

# 🔰 物理碰撞範例 - 射擊場

--------------

## 階段1: 發射子彈

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/tz9ODYd_WEs?start=2&amp;end=198" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


🏷️ 重點說明

: 設定舞台的寬為800，高為800。新增事件函式-按下鍵盤時，並在裡面新增圓球，球從左邊發射，開始位置設為(0, y)，這樣就可以按空白鍵(或任意鍵)發射，依滑鼠高度由左方射出。可調整圓球半徑及速度(勿過大)，
增加一些上升速度(y軸)，讓子彈產生一些弧度，不要太快掉落。

: 按空白鍵發射子彈，依滑鼠高度，從左方射出

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, y]
    物體.速度 = [3000, 300]
                
模擬主迴圈()
```




<br/><br/>

--------------


## 階段2: 方塊標靶

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/tz9ODYd_WEs?start=201&amp;end=274" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 新增事件函式-按下滑鼠時，區塊裡的程式為新增方塊(寬高30)，並將位置設為滑鼠的座標 x , y

: 按下滑鼠時，會產生方塊標靶。

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, y]
    物體.速度 = [3000, 300]

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=30,高=30)
    物體.位置 = [x, y]

模擬主迴圈()
```

<br/><br/>

--------------

#### ▪️ 直排標靶

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/tz9ODYd_WEs?start=276&amp;end=356" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 將原本的新增方塊，加上新迴圈，迴圈變數建議改為「直」，並加進變數清單。

: 將迴圈重複10次，依迴圈變數增加高度(位置的y坐標)。

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, y]
    物體.速度 = [3000, 300]

def 按下滑鼠時(x, y):
    for 直 in range(10) :
        物體 = 新增方塊(寬=30,高=30)
        物體.位置 = [x, y + 直 * 30]
        
模擬主迴圈()
```

<br/><br/>

--------------

#### ▪️ 方陣標靶

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/tz9ODYd_WEs?start=358&amp;end=435" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 再加上新迴圈，將迴圈變數改為「橫」，加進變數清單。

: 重複10次，依迴圈變數增加寬度(位置的x坐標)。

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, y]
    物體.速度 = [3000, 300]

def 按下滑鼠時(x, y):
    for 橫 in range(10) :
        for 直 in range(10) :
            物體 = 新增方塊(寬=30,高=30)
            物體.位置 = [x + 橫 * 30, y + 直 * 30]
              
模擬主迴圈()
```

<br/><br/>

--------------

#### ▪️ 金字塔形標靶

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/tz9ODYd_WEs?start=437&amp;end=549" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 先做出樓梯形(直角三角形)，將內層迴圈次數，依外層的迴圈變數變化

: 再將樓梯形左右相反，把內層迴圈次數，以最大值(10)減去

: 最後做出金字塔形，每往上一層(依變數直)，橫排方塊就往右半個寬度

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, y]
    物體.速度 = [3000, 300]

def 按下滑鼠時(x, y):
    for 橫 in range(10) :
        for 直 in range(10-橫) :
            物體 = 新增方塊(寬=30,高=30)
            物體.位置 = [x + 橫 * 30 + 直 * 30/2, y + 直 * 30]
              
模擬主迴圈()
```

<br/><br/>

--------------

## 階段3: 射擊測試


🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/tz9ODYd_WEs?start=551&amp;end=703" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 設定密度，球為1，方塊為1

: 測試下列不同密度組合並觀察

: (1)設定密度球為1，方塊為10，(2)設定密度球為10，方塊為1，(3)設定密度球為100，方塊為1

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)

def 按下鍵盤時(按鍵, x, y):
    物體 = 新增圓球(半徑=5)
    物體.位置 = [0, y]
    物體.速度 = [3000, 300]
    物體.密度 = 10
    
def 按下滑鼠時(x, y):
    for 橫 in range(10) :
        for 直 in range(10-橫) :
            物體 = 新增方塊(寬=30,高=30)
            物體.位置 = [x + 橫 * 30 + 直 * 30/2, y + 直 * 30]
            物體.密度 = 1
            
模擬主迴圈()
```