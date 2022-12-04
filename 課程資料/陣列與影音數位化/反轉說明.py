from 聲音模組 import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


聲音1 = 開啟wav檔('鋼琴聲音.wav')

聲音2 = 聲音1.reverse()


陣列1 = 聲音轉陣列(聲音1)
陣列2 = 聲音轉陣列(聲音2)

plt.subplot(1,2,1)
plt.plot(陣列1)
plt.title('原本音訊', fontsize=18)


plt.subplot(1,2,2)
plt.plot(陣列2)
plt.title('反轉音訊', fontsize=18)

plt.show()