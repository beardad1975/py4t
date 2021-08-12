# 🔰 海龜範例 - 畫出碎形樹

--------------

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/584287679?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="fractal.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

--------------

### 🏷️ 原理說明

碎形的每個部分都是整體縮小後的形狀。碎形在數學中是一種抽象的物體，用於描述自然界中存在的事物。

這個程式先定義一個遞迴函式「樹枝」，此函式需有一個終止條件(層為0)，主要做的事是向右分枝、向左分枝及後退。遞迴函式會不斷的呼叫自己(層引數需一直遞減至0為止)，在這個例子中，利用遞迴不斷的畫出分枝的樹枝。

定義了完整的「樹枝」函式，只需要執行一次，就會以遞迴的形式畫出碎形樹了。

--------------

### 📄 Py4t程式碼

```python
from 海龜模組 import *

縮減 = 0.8
角度 = 30  

def 樹枝(長, 層):
    if 層 == 0:
        return
        
    向前(長)
   
    右轉(角度)
    樹枝(長*縮減, 層-1)
    
    左轉(角度 * 2)
    樹枝(長*縮減, 層-1)
    
    右轉(角度)
    向後(長)

設定方向(90)
速度('fastest')

樹枝(層=7, 長 =100) 

```

--------------

### 💻 執行截圖

![執行截圖](fractal_tree.jpg)

