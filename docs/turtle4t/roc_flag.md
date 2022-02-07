---
hide:
  - navigation
---

# 🔰 專題範例 - 中華民國國旗

--------------

## 階段1: 程式結構

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=3&amp;end=281" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


--------------

🏷️ 重點說明

: 先儲存檔案，並匯入海龜模組。

: 此階段先寫出程式的主要結構，每個函式會先印出該函式的名稱作為代表。

: 先定義函式「主程式」，印出順序名稱，先呼叫主程式。

: 接著再逐一定義函式，紅地、青天、光芒、白日，並印出該函式的名稱。最後在主程式中呼叫其餘4個函式，印出的文字1~5行，就代表著程式的主要流程。

--------------

📄 Py4t程式碼

```python
from 海龜模組 import *

def 紅地() :
    print('2.紅地')
    
def 青天() :
    print('3.青天')

def 光芒() :
    print('4.光芒')

def 白日() :
    print('5.白日 ')

def 主程式() :
    print('1.主程式')
    紅地()
    青天()
    光芒()
    白日()
    
主程式()
```



<br/><br/><br/>

--------------


## 階段2: 紅地與青天

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=283&amp;end=483" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



--------------

🏷️ 重點說明

: 接下來實作紅地與青天

: 紅地是一個長方形，寬高的比例為120:80，完成長方形後，填上紅色

: 青天也是長方形，寬高的比例為60:40，完成長方形後，填上藍色

--------------

📄 Py4t程式碼

```python
from 海龜模組 import *

def 紅地() :
    print('2.紅地')
    填充顏色('red')
    開始填色()
    for 數 in range(2) :
        向前(120)
        右轉(90)
        向前(80)
        右轉(90)
    停止填色()
    
def 青天() :
    print('3.青天')
    填充顏色('blue')
    開始填色()
    for 數 in range(2) :
        向前(60)
        右轉(90)
        向前(40)
        右轉(90)
    停止填色()

def 光芒() :
    print('4.光芒')

def 白日() :
    print('5.白日 ')

def 主程式() :
    print('1.主程式')
    紅地()
    青天()
    光芒()
    白日()
    
主程式()

```



<br/><br/><br/>

--------------


## 階段3: 光芒

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=486&amp;end=718" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



--------------

🏷️ 重點說明

先加快海龜速度，隱藏游標，以方便後續的測試與結果

先把海龜移至光芒起點座標(15, -20)，移動時不畫線(停筆、移動、下筆)

接下來畫12角星形，長為29，角度依公式為180-360/12，重複12次初步完成星形線條。
畫筆顏色與填充顏色都設為白色。

畫出來的星形需再調整角度(提前左轉15度)，就會對齊整點鐘方向。

--------------

📄 Py4t程式碼

```python
from 海龜模組 import *
速度('fast')
隱藏游標()

def 紅地() :
    print('2.紅地')
    填充顏色('red')
    開始填色()
    for 數 in range(2) :
        向前(120)
        右轉(90)
        向前(80)
        右轉(90)
    停止填色()
    
def 青天() :
    print('3.青天')
    填充顏色('blue')
    開始填色()
    for 數 in range(2) :
        向前(60)
        右轉(90)
        向前(40)
        右轉(90)
    停止填色()

def 光芒() :
    print('4.光芒')
    停筆()
    走到(15, -20)
    下筆()
    
    左轉(15)
    
    畫筆顏色('white')
    填充顏色('white')
    開始填色()
    for 數 in range(12) :
        向前(29)
        右轉(180-360/12)
    停止填色()

def 白日() :
    print('5.白日 ')

def 主程式() :
    print('1.主程式')
    紅地()
    青天()
    光芒()
    白日()
    
主程式()
```



<br/><br/><br/>

--------------


## 階段4: 白日

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=721&amp;end=853" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



--------------

🏷️ 重點說明

先將移至白日的開始圓心座標(30, -20)，移動時不畫線(停筆、移動、下筆)。

畫出實心圓，直徑為17，顏色為藍色。再畫出小一點的實心圓，直徑15，顏色白色。完成了有青圈的白日

--------------

📄 Py4t程式碼

```python
from 海龜模組 import *
速度('fast')
隱藏游標()

def 紅地() :
    print('2.紅地')
    填充顏色('red')
    開始填色()
    for 數 in range(2) :
        向前(120)
        右轉(90)
        向前(80)
        右轉(90)
    停止填色()
    
def 青天() :
    print('3.青天')
    填充顏色('blue')
    開始填色()
    for 數 in range(2) :
        向前(60)
        右轉(90)
        向前(40)
        右轉(90)
    停止填色()

def 光芒() :
    print('4.光芒')
    停筆()
    走到(15, -20)
    下筆()
    
    左轉(15)
    
    畫筆顏色('white')
    填充顏色('white')
    開始填色()
    for 數 in range(12) :
        向前(29)
        右轉(180-360/12)
    停止填色()

def 白日() :
    print('5.白日 ')
    停筆()
    走到(30 , -20 )
    下筆()
    
    畫點(17 ,'blue' )
    畫點(15 , 'white')

def 主程式() :
    print('1.主程式')
    紅地()
    青天()
    光芒()
    白日()
    
主程式()

```



<br/><br/><br/>

--------------

## 階段5: 縮放倍率

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=855&amp;end=1054" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



--------------

🏷️ 重點說明

使用較大的視窗，將視窗設定寬1200、高800。

建立倍率變數，長度、座標移動相關的數都需要乘上倍率(縮放時會一起變化)


--------------

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(1200, 800)
速度('fast')
隱藏游標()

倍率 = 7

def 紅地() :
    print('2.紅地')
    填充顏色('red')
    開始填色()
    for 數 in range(2) :
        向前(120 * 倍率)
        右轉(90)
        向前(80 * 倍率)
        右轉(90)
    停止填色()   
    
def 青天() :
    print('3.青天')
    填充顏色('blue')
    開始填色()
    for 數 in range(2) :
        向前(60 * 倍率)
        右轉(90)
        向前(40 * 倍率)
        右轉(90)
    停止填色()
    
def 光芒() :
    print('4.光芒')
    停筆()
    走到(15 * 倍率 , -20 * 倍率)
    下筆()
    
    左轉(15)
    
    畫筆顏色('white')
    填充顏色('white')
    開始填色()
    for 數 in range(12) :
        向前(29 * 倍率)
        右轉(180-360/12)
    停止填色()
    
def 白日() :
    print('5.白日')
    停筆()
    走到(30 * 倍率, -20 * 倍率)
    下筆()
    
    畫點(17 * 倍率,'blue' )
    畫點(15 * 倍率, 'white')
    

def 主程式() :
    print('1.主程式') 
    紅地()
    青天()
    光芒()
    白日()    
    
主程式()
```



<br/><br/><br/>

--------------


## 階段6: 座標平移

🎦 範例影片


<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=1057&amp;end=1239" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


--------------

🏷️ 重點說明

將起點改至左上角。建立變數，起點x為-500，起點y為300

主程式於一開始，就將海龜移至新起點(移動不畫線)

因應起點移位，每個與座標移動有相關的數，都需要分別加上起點x與起點y

--------------

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(1200, 800)
速度('fast')
隱藏游標()

倍率 = 7

起點x = -500
起點y = 300

def 紅地() :
    print('2.紅地')
    填充顏色('red')
    開始填色()
    for 數 in range(2) :
        向前(120 * 倍率)
        右轉(90)
        向前(80 * 倍率)
        右轉(90)
    停止填色()   
    
def 青天() :
    print('3.青天')
    填充顏色('blue')
    開始填色()
    for 數 in range(2) :
        向前(60 * 倍率)
        右轉(90)
        向前(40 * 倍率)
        右轉(90)
    停止填色()
    
def 光芒() :
    print('4.光芒')
    停筆()
    走到(15 * 倍率 + 起點x , -20 * 倍率 + 起點y)
    下筆()
    
    左轉(15)
    
    畫筆顏色('white')
    填充顏色('white')
    開始填色()
    for 數 in range(12) :
        向前(29 * 倍率)
        右轉(180-360/12)
    停止填色()
    
def 白日() :
    print('5.白日')
    停筆()
    走到(30 * 倍率 + 起點x , -20 * 倍率 + 起點y)
    下筆()
    
    畫點(17 * 倍率,'blue' )
    畫點(15 * 倍率, 'white')
    

def 主程式() :
    print('1.主程式')
    停筆()
    走到(起點x,起點y)
    下筆()
    
    紅地()
    青天()
    光芒()
    白日()
   
主程式()
```



<br/><br/><br/>

--------------


## 階段7: 使用者介面

🎦 範例影片

<iframe width="560" height="315" src="https://www.youtube.com/embed/qjlan7-zmu8?start=1240&amp;end=1405" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



--------------



🏷️ 重點說明

使用圖形框，讓使用者輸入數字。填入標題、說明、預設值、最小值、最大值，即可取得使用者的輸入。

於主程式最後，加上點擊後離開，點一下視窗就會關閉程式。

--------------

📄 Py4t程式碼

```python
from 海龜模組 import *
視窗設定(1200, 800)
速度('fast')
隱藏游標()

倍率 = 輸入數字('中華民國國旗','輸入倍率1-10',5, 1, 10)

起點x = -500
起點y = 300

def 紅地() :
    print('2.紅地')
    填充顏色('red')
    開始填色()
    for 數 in range(2) :
        向前(120 * 倍率)
        右轉(90)
        向前(80 * 倍率)
        右轉(90)
    停止填色()   
    
def 青天() :
    print('3.青天')
    填充顏色('blue')
    開始填色()
    for 數 in range(2) :
        向前(60 * 倍率)
        右轉(90)
        向前(40 * 倍率)
        右轉(90)
    停止填色()
    
def 光芒() :
    print('4.光芒')
    停筆()
    走到(15 * 倍率 + 起點x , -20 * 倍率 + 起點y)
    下筆()
    
    左轉(15)
    
    畫筆顏色('white')
    填充顏色('white')
    開始填色()
    for 數 in range(12) :
        向前(29 * 倍率)
        右轉(180-360/12)
    停止填色()
    
def 白日() :
    print('5.白日')
    停筆()
    走到(30 * 倍率 + 起點x , -20 * 倍率 + 起點y)
    下筆()
    
    畫點(17 * 倍率,'blue' )
    畫點(15 * 倍率, 'white')
    
def 主程式() :
    print('1.主程式')
    停筆()
    走到(起點x,起點y)
    下筆()
    
    紅地()
    青天()
    光芒()
    白日()
    
    點擊後離開()
    
主程式()
```



<br/><br/><br/>

