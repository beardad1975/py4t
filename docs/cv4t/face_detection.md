# 🔰 影像範例 - 看見人臉


: ![看見人臉](face_detection.jpg)

<br/>

-------------------------------------

## 看見人臉

🎦 範例影片

: <iframe width="560" height="315" src="https://www.youtube.com/embed/TUb_CzM2PjI?start=2&amp;end=348" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 視覺模組 import *

攝影機 = 設置影像擷取(後端='DSHOW')
偵測器 = 設置FaceDetection()

while True :
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    顯示影像(陣列)
    
    結果 = 偵測器.process(陣列)
    if 結果:
        標記Face(陣列, 結果)
        臉 = 取出Face(結果)
        畫出文字(image=陣列,
             text=str(臉.score),
             pos=臉.bottom_left)        
        顯示影像(陣列, 視窗名稱='Image 2')
```

<br/><br/>

-------------------------------------