from 視覺模組 import *

攝影機 = 設置影像擷取()

while True:
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    陣列 = 彩色轉灰階(陣列)
    
    陣列[:, ::50] = 255
    陣列[::50, :] = 255
    
    顯示影像(陣列)