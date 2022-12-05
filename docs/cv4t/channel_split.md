# 🔰 聲音範例 - 通道分離


: ![通道分離](channel_split.jpg)

<br/>

-------------------------------------

## 通道分離

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/kd3NUcxbMd0?start=0&amp;end=475" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


📄 Py4t程式碼

```python
from 視覺模組 import *

陣列 = 讀取影像彩色('olympic.jpg')
print(陣列)
print(陣列.shape)
顯示影像(陣列, 視窗名稱='1')
等待按鍵(500)

陣列b = 陣列.copy()
陣列b[:, :, 1] = 0
陣列b[:, :, 2] = 0
顯示影像(陣列b, 視窗名稱='b')
等待按鍵(500)

陣列g = 陣列.copy()
陣列g[:, :, 0] = 0
陣列g[:, :, 2] = 0
顯示影像(陣列g, 視窗名稱='g')
等待按鍵(500)

陣列r = 陣列.copy()
陣列r[:, :, 0] = 0
陣列r[:, :, 1] = 0
顯示影像(陣列r, 視窗名稱='r')
等待按鍵()
```

<br/><br/>

-------------------------------------