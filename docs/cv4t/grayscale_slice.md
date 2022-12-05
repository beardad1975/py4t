# 🔰 聲音範例 - 灰階切片


: ![聲音處理](grayscale_slice.jpg)

<br/>

-------------------------------------

## 灰階切片

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/okx9rlfdDs8?start=0&amp;end=586" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


📄 Py4t程式碼

```python
from 視覺模組 import *

陣列 = 讀取影像灰階('kirun.jpg')
print(陣列)
print(陣列.shape)
顯示影像(陣列)
等待按鍵(500)

陣列[:, :200] = 調整亮度(陣列[:, :200], 50)
顯示影像(陣列)
等待按鍵(500)

陣列[:, 200:400] = 模糊(陣列[:, 200:400], 核心=10)
顯示影像(陣列)
等待按鍵(500)

陣列[:, 400:600] = 255 - 陣列[:, 400:600]
顯示影像(陣列)
等待按鍵(500)

陣列[:, 600:] = Canny邊緣偵測(陣列[:, 600:])
顯示影像(陣列)
等待按鍵()
```

<br/><br/>

-------------------------------------