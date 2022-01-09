# 🔰 物理碰撞範例 - 力與斜面

--------------

## 階段1: 新增球與斜面

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=2&amp;end=302" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 匯入物理模組、模擬主迴圈並設定舞台(寬1200 高800)。

: 新增事件函式按下滑鼠時，新增圓球並圓球設定在滑鼠的x, y位置。

: 建立地面，先按住Ctrl鍵不放，按滑鍵右鍵可以決定地面的起點與終點)；刪除地面，先按住Alt鍵不放，按滑鼠右鍵可以決定要刪除的地面。建立3個，不同斜度的地面(右邊較高)，準備來做模擬實驗。

📄 Py4t程式碼


```python
from 物理模組 import *
舞台 = 物理引擎(1200,800)

def 按下滑鼠時(x, y):
    物體 = 新增圓球(半徑=25)
    物體.位置 = [x, y]
    
模擬主迴圈()
```

註：地形需自行建立(操作如階段1影片)

<br/><br/>

--------------

## 階段2: 速度比較

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=303&amp;end=339" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 先將時間暫停時(按住Ctrl不放)，將3顆球置於斜面頂端，模擬出來的結果大致是，傾斜度越大，球到底部的速度越快。


📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(1200,800)

def 按下滑鼠時(x, y):
    物體 = 新增圓球(半徑=25)
    物體.位置 = [x, y]
    
模擬主迴圈()
```

註1：程式與階段1相同
註2：地形需自行建立(操作如階段1影片)

<br/><br/>

--------------



## 階段3: 摩擦力

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=341&amp;end=504" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 改為新增方塊，並固定寬與高，於時間暫停時(按住Ctrl不放)，將3個方塊置於斜面，模擬結果大致是，傾斜度越小，移動的距離越短。

: 同時降低方塊摩擦係數，會造成摩擦力變小，於時間暫停時(按住Ctrl不放)，將3個方塊置於斜面，模擬結果大致是，摩擦力變小時，移動的距離都會變長。

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(1200,800)

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=50,高=50)
    物體.位置 = [x, y]
    物體.摩擦 = 0.2
    
模擬主迴圈()
```

註：地形需自行建立(操作如階段1影片)

## 階段4: 施力

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=505&amp;end=633" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 在方塊上施加力量，將施力方向改為向右(x為正數)，在時間暫停時(按住Ctrl不放)，將3方塊置於地面，之後試著增加施力看看

: 模擬結果大致是，傾斜度越小時，方塊移動的長度越長。

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(1200,800)

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=50,高=50)
    物體.位置 = [x, y]
    物體.摩擦 = 0.2
    
    向量 = [800, 0]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

註：地形需自行建立(操作如階段1影片)