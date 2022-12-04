from 聲音模組 import *
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

音源1 = 正弦波(220)
聲音1 = 音源1.轉成聲音(持續時間=20, 音量=-8.0)

音源2 = 白噪音()

聲音2 = 音源2.轉成聲音(持續時間=20, 音量=-8.0)

聲音3 = 聲音1.overlay(聲音2)




陣列1 = 聲音轉陣列(聲音1)
陣列2 = 聲音轉陣列(聲音2)
陣列3 = 聲音轉陣列(聲音3)

plt.subplot(2,1,1)
plt.plot(陣列3)

plt.title('弦波與白噪音 混合', fontsize=16)
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,3)
plt.plot(陣列1)
plt.xlabel('弦波', fontsize=16)
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.plot(陣列2, )
plt.xlabel('白噪音', fontsize=16)
plt.xticks([])
plt.yticks([])


plt.show()