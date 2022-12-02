# 🔰 聲音範例 - 聲音訊號


: ![聲音訊號](sound_signal.jpg)

<br/>

-------------------------------------

## 聲音訊號

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/-BMUwYRELw4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

📄 Py4t程式碼

```python
from 聲音模組 import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

音源 = 正弦波(440, 取樣率=44100)
聲音 = 音源.轉成聲音()
聲音 = 聲音.fade_in(100)
play(聲音)

陣列 = 聲音轉陣列(聲音)
陣列 = 陣列[0:441]
print(陣列)
print(陣列.shape)

plt.title('聲波圖(0.01秒)', fontsize=20)
plt.xlabel('聲音取樣', fontsize=18)
plt.ylabel('響度量化', fontsize=18)
plt.plot(陣列, '.')
plt.show()
```

<br/><br/>

-------------------------------------