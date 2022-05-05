---
hide:
  - navigation
---

# 🔰 3D程式範例 - 魔方方塊

--------------

: ![魔術方塊](rubik_cube.jpg)

<br/>

🎦 範例影片

: 建構中

📄 Py4t程式碼

```python
from 模擬3D模組 import *

for z in range(3) :
    for y in range(3) :
        for x in range(3) :            
            物體 = 新增6面貼圖方塊()
            物體.材質貼圖 = '魔方6面.png'
            物體.位置 = [x,y,z]
                           
模擬主迴圈()
```

: 註: 材質貼圖檔需匯入並修改。