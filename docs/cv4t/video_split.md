# 🔰 聲音範例 - 視訊分割


: ![視訊分割](video_split.jpg)

<br/>

-------------------------------------

## 視訊分割

🎦 範例影片


<iframe width="560" height="315" src="https://www.youtube.com/embed/KtVq_qbH3aA?start=0&amp;end=639" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 視覺模組 import *

攝影機 = 設置影像擷取()
陣列 = 擷取影像(攝影機)
print(陣列.shape)
高 = 陣列.shape[0]
寬 = 陣列.shape[1]
分割點y = 高 // 2
分割點x = 寬 // 2

while True :
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    顯示影像(陣列, 視窗名稱='all')
    
    顯示影像(陣列[:分割點y, :分割點x], 視窗名稱='1')
    顯示影像(陣列[:分割點y, 分割點x:], 視窗名稱='2')
    顯示影像(陣列[分割點y:, :分割點x], 視窗名稱='3')
    顯示影像(陣列[分割點y:, 分割點x:], 視窗名稱='4')
```

<br/><br/>

-------------------------------------