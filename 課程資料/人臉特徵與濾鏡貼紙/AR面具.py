from 視覺模組 import *

攝影機 = 設置影像擷取(後端='DSHOW')
偵測器 = 設置FaceMesh()
png陣列 = 讀取png影像('white_mask.png')
面具臉型 = 讀取面具臉型('white_mask.csv', png陣列)

while True :
    陣列 = 擷取影像(攝影機)
    陣列 = 左右翻轉(陣列)
    顯示影像(陣列)
    
    結果 = 偵測器.process(陣列)
    if 結果:
        #標記FaceMesh(陣列, 結果)
        轉換png陣列 = 面具transform(
            來源影像=png陣列,
            臉型對應=面具臉型,
            目標影像=陣列,
            偵測結果=結果)
        貼上png(陣列,轉換png陣列)
        
        顯示影像(陣列, 視窗名稱='Image 2')  