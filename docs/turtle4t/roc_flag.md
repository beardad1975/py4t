# 🔰 海龜範例 - 畫出國旗

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/640407629?h=a713b31afe&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="roc_flag.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

利用正方形、星形與圓形，再善用海龜填色功能，就可以畫出青天白日滿地紅的國旗。程式中的國旗大小有保留倍率的變數，當使用者輸入不同的倍率時，就可以改變國旗的大小。

--------------

### 📄 Py4t程式碼

```python
# 需安裝py4t 0.9版以上
from 海龜模組 import *

# 初始設定
速度('fast')
視窗設定(1200, 800)
出發點x = -400
出發點y = 300

# 輸入倍率
倍率 = 輸入數字('輸入','請輸入國旗的倍率(1~8)',3,1,8)
倍率 = int(倍率)

def 紅地() :
    填充顏色(255,0,0)
    開始填色()
    for 數 in range(2) :
        向前(倍率*120)
        右轉(90)
        向前(倍率*80)
        右轉(90)
    停止填色()

def 藍天() :
    填充顏色(0,0,255)
    開始填色()
    for 數 in range(2) :
        向前(倍率*60)
        右轉(90)
        向前(倍率*40)
        右轉(90)
    停止填色()

def 光芒() :
    停筆()
    走到(出發點x + 倍率*15,出發點y - 倍率*20)
    下筆()
    
    左轉(15)
    
    畫筆顏色(255,255,255)
    填充顏色(255,255,255)
    開始填色()
    
    for 數 in range(12) :
        向前(倍率*30)
        右轉(150)
    停止填色()
    
def 白日():
    停筆()
    走到(出發點x + int(倍率*30.5),出發點y-倍率*20)
    下筆()
    畫點(倍率*17, [0,0,255])
    畫點(倍率*15, [255,255,255])

def 國旗():
    停筆()
    走到(出發點x,出發點y)
    下筆()
    紅地()    
    藍天()
    光芒()
    白日()

# 主程式
國旗()
隱藏游標()
完成()

```

--------------

### 💻 執行截圖

![執行截圖](roc_flag.jpg)


