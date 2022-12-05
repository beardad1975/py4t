# 🔰 影像範例 - 灰階點陣


: ![灰階點陣](grayscale_pixel.jpg)

<br/>

-------------------------------------

## 灰階點陣

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/vC0rJwPXcQY?start=0&amp;end=581" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


📄 Py4t程式碼

```python
import numpy as np
import matplotlib.pyplot as plt

陣列 = np.zeros([10,10])
陣列 = 陣列.astype('uint8')

for x in range(10) :
    for y in range(10) :
        陣列[y, x] = 255 - y * 20 - x * 20            

print(陣列)
print(陣列.dtype)

plt.imshow(陣列, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.show()
```

<br/><br/>

-------------------------------------