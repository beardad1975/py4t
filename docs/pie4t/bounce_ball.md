# 🔰 物理碰撞範例 - 球的彈性

--------------

## 階段1: 新增圓球

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/sIAgw3FryX8?start=1&amp;end=128" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 先儲存檔案，檔名為「球的彈性」，先顯示物理模組後，才會有相關的便利貼出現。

: 必要的程式有：匯入物理模組(開頭)，模擬主迴圈(最後)，增加「按下滑鼠時」的事件處理函式，並在函式內加上「新增圓球」，最後將增加的圓球物體位置，設定為滑鼠位置

📄 Py4t程式碼

```python
from 物理模組 import *

def 按下滑鼠時(x, y):
    物體 = 新增圓球()
    物體.位置 = [x, y] 

模擬主迴圈()
```

<br/><br/>

--------------

## 階段2: 恢復係數

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/sIAgw3FryX8?start=131&amp;end=251" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 設定球的彈性，數字代表的是球的恢復係數。

: 分別實驗不同的恢復係數，0是最差彈性，0.75模擬的是籃球彈性，1是模擬彈性碰撞(理想值，現實中很難出現)


📄 Py4t程式碼

```python
from 物理模組 import *

def 按下滑鼠時(x, y):
    物體 = 新增圓球()
    物體.位置 = [x, y]
    物體.彈性 = 0.75 

模擬主迴圈()
```

<br/><br/>

--------------


## 階段3: 超強彈性體

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/sIAgw3FryX8?start=253&amp;end=410" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 複製新增球的程式，來產生2顆球(注意區塊縮排)，並讓2顆球一高一低(控制y座標)，接著設定低的是小球，高的是大球(球的半徑)，就完成超強彈性體。


📄 Py4t程式碼

```python
from 物理模組 import *

def 按下滑鼠時(x, y):
    物體 = 新增圓球(5)
    物體.位置 = [x, y + 60]
    物體.彈性 = 1
    
    物體 = 新增圓球(20)
    物體.位置 = [x, y]
    物體.彈性 = 1    

模擬主迴圈()
```
