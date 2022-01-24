# 🔰 物理碰撞範例 - 慣性與重力

--------------

## 階段1: 慣性運動

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/8STo6dA7uyQ?start=0&amp;end=247" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 將物理舞台設定為寬800，高800，並設定重力為[0,0]，即為無重力狀態
: 新增事件函式按下滑鼠時，在其中新增方塊(指定寬高)，位置設定於0, 0(左下角)，施加衝力，並設定施力向量[x, y] ，即會隨滑鼠位置改變力的方向
: 刪除地面的地形(按住Alt鍵不放時，滑鼠右鍵刪除地面)

: 在操作時，當滑鼠離原點(左下)越近，獲得的衝力越小；越遠越大。模擬結果會呈現慣性定律，當外力為0時，靜者恆靜，動者恆動，作等速直線運動


📄 Py4t程式碼


```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
舞台.重力 = [0, 0]

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=30,高=20)
    物體.位置 = [0, 0]
    向量 = [x, y]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

註：地形需自行刪除(操作如階段1影片)

<br/><br/>

--------------

## 階段2: 拋體運動


🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/8STo6dA7uyQ?start=250&amp;end=348" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 改變重力方向為[0, -800] (向下)，看看物體運動的方向。再將重力改為[-800, 0]向左，再觀察看看。

: 模擬結果，物體原本因慣性定律的等速直線運動，再加上重力後，就會呈現拋體運動

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
舞台.重力 = [0, -800]

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=30,高=20)
    物體.位置 = [0, 0]
    向量 = [x, y]
    物體.施加衝力(向量)
    
模擬主迴圈()
```

註：地形需自行刪除(操作如階段1影片)

<br/><br/>

--------------



## 階段3: 重力搬運


🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/8STo6dA7uyQ?start=350&amp;end=677" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

🏷️ 重點說明

: 將重力改回無重力狀態。加入事件處理函式，當按了向下鍵時，重力會改為向下，並建立籃子地形(按住Ctrl鍵)，操作物體看看

: 接著再加入其他方向鍵的操作來改變重力的方向(注意if縮排需相同)，並完成4個方向的籃子地形。加入新的事件處理函式，當放開按鍵時，恢復成無重力，這樣一來改變重力方向需長按方向鍵，可以避免重力變化太快，不易操作。到這邊就可以使用重力來搬移物體

📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
舞台.重力 = [0, 0]

def 按下滑鼠時(x, y):
    物體 = 新增方塊(寬=30,高=20)
    物體.位置 = [0, 0]
    向量 = [x, y]
    物體.施加衝力(向量)
    
def 按下鍵盤時(按鍵, x, y):
    if 按鍵 == key.DOWN :
        舞台.重力 = [0, -800]
    if 按鍵 == key.UP :
        舞台.重力 = [0, 800]
    if 按鍵 == key.RIGHT :
        舞台.重力 = [800, 0]
    if 按鍵 == key.LEFT :
        舞台.重力 = [-800, 0]
            
def 放開鍵盤時(按鍵, x, y):
    舞台.重力 = [0, 0]
    
模擬主迴圈()
```

註：籃子地形需自行建立(操作如階段3影片)

