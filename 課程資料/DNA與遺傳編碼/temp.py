from 模擬3D模組 import *    

原點 = 新增物體()
DNA序列 = 'ACCCTAACCCTAACCCTCTGAAAGTGGACCTATCAGCAGGATGTGGGTGGGAGCAGATTAGAGAATAAAAGCAGACTGCCTGAGCCAGCAGTGGCAACCCA'

for i, 編碼 in enumerate(DNA序列) :
    旋轉中心 = 新增物體()
    旋轉中心.旋轉z = 30 * i
    旋轉中心.位置z = 5 * i
    旋轉中心.親代 = 原點

    核苷酸 = 新增球體()
    核苷酸.顏色 = color.orange
    核苷酸.位置y = 10
    核苷酸.親代 = 旋轉中心
    核苷酸.縮放 = 7.5

    鹼基 = 新增球體()
    鹼基.顏色 = color.orange
    鹼基.位置y = 5
    鹼基.親代 = 旋轉中心
    鹼基.縮放y = 10

    核苷酸2 = 新增球體()
    核苷酸2.位置y = -10
    核苷酸2.親代 = 旋轉中心
    核苷酸2.縮放 = 7.5

    鹼基2 = 新增球體()
    鹼基2.位置y = -5
    鹼基2.親代 = 旋轉中心
    鹼基2.縮放y = 10

    if 編碼 == 'A' :
        鹼基.顏色 = color.green
        鹼基2.顏色 = color.red
    elif 編碼 == 'T' :
        鹼基.顏色 = color.red
        鹼基2.顏色 = color.green
    elif 編碼 == 'C' :
        鹼基.顏色 = color.blue
        鹼基2.顏色 = color.yellow
    elif 編碼 == 'G' :
        鹼基.顏色 = color.yellow
        鹼基2.顏色 = color.blue
    else :
        pass

def 當更新時(dt):
    原點.旋轉z  +=  0.2    

模擬主迴圈()
