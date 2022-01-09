# 🔰 物理碰撞範例 - 彈跳吧！圓球

### 🎦 範例影片

<iframe width="896" height="504" src="https://www.youtube.com/embed/Bd2KNTtAxlY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 🏷️ 重點說明

: 首先建立物理舞台(寬800, 高800)，產生圓球(指定半徑)，設定位置，按住Ctrl 可以觀察座標(原點在左下角)

: 先產生10顆圓球，設定x位置並設定彈性，讓球排成一列，再設定y位置，讓球有不同高低位置。

: 在產生20顆圓球過程中，辨別數字之間的關係，建立球數、直徑、半徑變數。

: 最後的變數，讓奇數球、偶數球有不同的彈性。

--------------

### 📄 Py4t程式碼

```python
from 物理模組 import *
舞台 = 物理引擎(800,800)
球數 = 50
直徑 = 800 // 球數
半徑 = 直徑 // 2

for 數 in range(球數) :
    物體 = 新增圓球(半徑)
    物體.位置 = [數 * 直徑, 數 * 直徑]
    if 數 % 2 == 0 :
        物體.彈性 = 0.9

模擬主迴圈()

```

--------------




