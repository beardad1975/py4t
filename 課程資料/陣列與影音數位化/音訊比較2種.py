from 聲音模組 import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

音源1 = 正弦波(220)
聲音1 = 音源1.轉成聲音(持續時間=40, 音量=-8.0)
聲音1 = 聲音1.fade_in(20)


音源2 = 正弦波(220)
聲音2 = 音源2.轉成聲音(持續時間=40, 音量=-8.0)
聲音2 = 聲音2.fade_out(20)

陣列1 = 聲音轉陣列(聲音1)
陣列2 = 聲音轉陣列(聲音2)

plt.subplot(1,2,1)
plt.plot(陣列1)
plt.title('淡入', fontsize=18)


plt.subplot(1,2,2)
plt.plot(陣列2)
plt.title('淡出', fontsize=18)

plt.show()