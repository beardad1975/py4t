# 🔰 影像範例 - AR面具(多種切換)


: ![AR面具(多種切換)](ar_mask_switch.jpg)

<br/>

-------------------------------------

## AR面具(多種切換)

🎦 Demo影片

: <iframe width="560" height="315" src="https://www.youtube.com/embed/a4KKPwdfslw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br/>
<br/>

📄 Py4t程式碼

* 說明1：[程式所需檔案](ar_mask_switch.zip)，下載後需將檔案解壓縮，在與程式相同的資料夾
* 說明2：使用空白鍵切換

```python
from 視覺模組 import *
import itertools

攝影機 = 設置影像擷取(後端='DSHOW')
偵測器 = 設置FaceMesh()
面具清單 = [None]
已換 = False

png陣列 = 讀取png影像('anonymous.png')
面具臉型 = 讀取面具臉型('anonymous.csv', png陣列)
面具清單.append((png陣列, 面具臉型))

png陣列 = 讀取png影像('white_mask.png')
面具臉型 = 讀取面具臉型('white_mask.csv', png陣列)
面具清單.append((png陣列, 面具臉型))

png陣列 = 讀取png影像('opera_red.png')
面具臉型 = 讀取面具臉型('opera_red.csv', png陣列)
面具清單.append((png陣列, 面具臉型))

png陣列 = 讀取png影像('anime.png')
面具臉型 = 讀取面具臉型('anime.csv', png陣列)
面具清單.append((png陣列, 面具臉型))

面具循環 = itertools.cycle(面具清單)
面具項目 = next(面具循環)

while True :
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    結果 = 偵測器.process(陣列)
    if 結果 :
        已換 = False
        if 面具項目:
            特徵清單 = 取出Landmarks(結果)
            轉換png陣列 = 面具transform(
               來源影像=面具項目[0],
               臉型對應=面具項目[1],
               目標影像=陣列,
               偵測結果=結果)
            貼上png(陣列,轉換png陣列)
    elif not 結果 and not 已換:
        面具項目 = next(面具循環)
        已換 = True
    
    顯示影像(陣列)
```