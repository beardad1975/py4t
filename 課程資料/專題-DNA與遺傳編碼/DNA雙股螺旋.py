from 模擬3D模組 import *

原點 = 新增物體()
DNA序列 = 'ACCCTAACCCTAACCCTCTGAAAGTGGACCTATCAGCAGGATGTGGGTGGGAGCAGATTAGAGAATAAAAGCAGACTGCCTGAGCCAGCAGTGGCAACCCA'

for 索引, 編碼 in enumerate(DNA序列):
    旋轉中心 = 新增物體()    
    旋轉中心.位置x = 索引 * 5
    旋轉中心.旋轉x = 索引 * 30
    旋轉中心.上層物件 = 原點
           
    核苷酸1 = 新增球體()
    核苷酸1.上層物件 = 旋轉中心
    核苷酸1.位置y = 10
    核苷酸1.縮放 = 7.5
    
    核苷酸2 = 新增球體()
    核苷酸2.上層物件 = 旋轉中心
    核苷酸2.位置y = -10
    核苷酸2.縮放 = 7.5
    核苷酸2.顏色 = color.orange

    鹼基1 = 新增球體()
    鹼基1.上層物件 = 旋轉中心
    鹼基1.縮放y = 10
    鹼基1.位置y = 5
    
    鹼基2 = 新增球體()
    鹼基2.上層物件 = 旋轉中心
    鹼基2.縮放y = 10
    鹼基2.位置y = -5
    鹼基2.顏色 = color.orange

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
    原點.旋轉x  +=  0.2
        
模擬主迴圈()