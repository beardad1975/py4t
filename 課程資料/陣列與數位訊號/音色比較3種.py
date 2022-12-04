from 聲音模組 import *
import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


聲音1 = 開啟wav檔('鋼琴聲音.wav')

聲音2 = 開啟wav檔('小提琴聲音.wav')

聲音3 = 開啟wav檔('個人一小步.wav')

陣列1 = 聲音轉陣列(聲音1[:5000])
陣列2 = 聲音轉陣列(聲音2[:5000])
陣列3 = 聲音轉陣列(聲音3[:5000])

plt.subplot(2,1,1)
plt.plot(陣列3)

plt.title('人聲 波形', fontsize=16)
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,3)
plt.plot(陣列1)
plt.xlabel('鋼琴 波形', fontsize=16)
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.plot(陣列2, )
plt.xlabel('小提琴 波形', fontsize=16)
plt.xticks([])
plt.yticks([])


plt.show()