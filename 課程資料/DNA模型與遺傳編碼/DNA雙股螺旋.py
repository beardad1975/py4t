from 模擬3D模組 import *

DNA序列 = 'ACCCTAACCCTAACCCTCTGAAAGTGGACCTATCAGCAGGATGTGGGTGGGAGCAGATTAGAGAATAAAAGCAGACTGCCTGAGCCAGCAGTGGCAACCCA' 
原點 = 新增物體()  
說明 = 新增文字('DNA簡易3D模型-人類X染色體片段',尺寸='小')
說明.位置y = -0.35

for 索引, 編碼 in enumerate(DNA序列):
    旋轉中心 = 新增物體()    
    旋轉中心.位置x = 索引 * 3
    旋轉中心.旋轉x = 索引 * 30
    旋轉中心.上層物件 = 原點
           
    核苷酸1 = 新增球體()
    核苷酸1.上層物件 = 旋轉中心
    核苷酸1.位置y = 10
    核苷酸1.縮放 = [6, 6, 6]
      
    核苷酸2 = 新增球體()
    核苷酸2.上層物件 = 旋轉中心
    核苷酸2.位置y = -10
    核苷酸2.縮放 = [6, 6, 6]
    核苷酸2.顏色 = 色彩.gray
    
    鹼基1 = 新增立方體()
    鹼基1.上層物件 = 旋轉中心
    鹼基1.縮放y = 8
    鹼基1.位置y = 5
    
    鹼基2 = 新增立方體()
    鹼基2.上層物件 = 旋轉中心
    鹼基2.縮放y = 7
    鹼基2.位置y = -5
    
    if 編碼 == 'A':
        鹼基1.顏色 = 色彩.green
        鹼基2.顏色 = 色彩.red
    elif 編碼 == 'T':
        鹼基1.顏色 = 色彩.red
        鹼基2.顏色 = 色彩.green
    elif 編碼 == 'C':
        鹼基1.顏色 = 色彩.blue
        鹼基2.顏色 = 色彩.yellow
    elif 編碼 == 'G':
        鹼基1.顏色 = 色彩.yellow
        鹼基2.顏色 = 色彩.blue
            
def 當更新時(dt):
    global 原點
    原點.旋轉x += 0.2
    
模擬主迴圈()