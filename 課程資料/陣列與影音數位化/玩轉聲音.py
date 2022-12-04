from 聲音模組 import *
import matplotlib.pyplot as plt

聲音1 = 開啟wav檔('個人一小步.wav')

聲音2 = 開啟wav檔('小提琴聲音.wav')

聲音 = 聲音1.overlay(聲音2)

play(聲音)
聲音.儲存wav檔('音訊處理.wav')

陣列 = 聲音轉陣列(聲音)
plt.plot(陣列)
plt.show()