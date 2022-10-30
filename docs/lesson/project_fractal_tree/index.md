---
hide:
  - navigation
---

# 📚專題：海龜與樹

----------------------------
##  📕 引言 
----------------------------




??? info "建議先備課程"

     在學習本專題前，建議先完成 :fontawesome-solid-long-arrow-alt-right: <a href="../zentangle/" target="_blank">「海龜畫禪繞」</a> ，在學習概念銜接上會較為平順。

<br/><br/><br/> 

----------------------------
##  📙 問題 
----------------------------



<br/><br/><br/> 

----------------------------
##  📗 搜尋
----------------------------


<br/><br/><br/> 

----------------------------
##  📒 構思
----------------------------



<br/><br/><br/> 

----------------------------
##  📘 實作(4)


###  ***程式結構***

----------------------------




<br>

???+ example "範例程式 程式結構 - - - - - - - (專題實作1/4 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=2&amp;end=129" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:07 章節時間如下】

        * 0:00 檔案儲存
        * 0:32 程式結構


    === "💻程式碼"

        ```python
        # 模組區 ----------
        from 海龜模組 import *

        # 全域變數 ----------

        # 函式區 ----------

        # 主程式 ----------


        完成()
        ``` 




<br/><br/><br/>

----------------------------


###  ***單線遞迴***

----------------------------


<br>

???+ example "範例程式 單線遞迴 - - - - - - - (專題實作2/4 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=131&amp;end=491" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度6:00 章節時間如下】

        * 2:11 單線遞迴

    === "💻程式碼"

        ```python
        # 模組區 ----------------
        from 海龜模組 import *

        # 全域變數 ----------------

        # 函式區 ----------------
        def 初始設定() :
            左轉(90)
            
        def 遞迴(層) :
            if 層 > 5 :
                畫點(10, 'red')
                return
            
            向前(50)
            畫點(10, 'black')
            右轉(20)
            
            遞迴(層 + 1)
            
            左轉(20)
            向後(50)
                
        # 主程式 ----------------
        初始設定()
        遞迴(1)
        完成()
        ``` 


<br/><br/><br/>

----------------------------

###  ***碎形樹***

----------------------------


<br>

???+ example "範例程式 碎形樹 - - - - - - - (專題實作3/4 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=493&amp;end=976" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度8:03 章節時間如下】

        * 8:13 碎形樹

    === "💻程式碼"

        ```python
        # 模組區 ----------------
        from 海龜模組 import *

        # 全域變數 ----------------
        最大層數 = 5
        轉角 = 20
        開始長度 = 100
        長縮減率 = 0.7

        # 函式區 ----------------
        def 初始設定() :
            左轉(90)
            速度('fastest')	
                
        def 遞迴(層, 長) :
            if 層 > 最大層數 :
                畫點(10, 'red')
                return
            
            向前(長)
            畫點(10, 'black')
            
            右轉(轉角)
            遞迴(層 + 1, 長 * 長縮減率)
            
            左轉(轉角 * 2)
            遞迴(層 + 1, 長 * 長縮減率)
            
            右轉(轉角)
            向後(長)
                
        # 主程式 ----------------
        初始設定()
        遞迴(1, 開始長度)
        完成()        
        ``` 

<br/><br/><br/>

----------------------------

###  ***碎形動畫***

----------------------------


<br>

???+ example "範例程式 碎形動畫 - - - - - - - (專題實作4/4 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=978&amp;end=1180" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度3:22 章節時間如下】

        * 16:18 碎形動畫

    === "💻程式碼"

        ```python
        # 模組區 ----------------
        from 海龜模組 import *

        # 全域變數 ----------------
        最大層數 = 5
        轉角 = 20
        開始長度 = 100
        長縮減率 = 0.7

        # 函式區 ----------------
        def 初始設定() :
            左轉(90)
            速度('fastest')
            tracer(0, 0)
                
        def 遞迴(層, 長) :
            if 層 > 最大層數 :
                畫點(10, 'red')
                return
            
            向前(長)
            畫點(10, 'black')
            
            右轉(轉角)
            遞迴(層 + 1, 長 * 長縮減率)
            
            左轉(轉角 * 2)
            遞迴(層 + 1, 長 * 長縮減率)
            
            右轉(轉角)
            向後(長)
                
        # 主程式 ----------------
        初始設定()

        for 數 in range(90+1) :
            筆跡清除()
            轉角 = 數 
            遞迴(1, 開始長度)
            update()    

        完成()        
        ``` 

<br/><br/><br/>

----------------------------
##  📙 擴展(3)


### ***樹與剪影***

----------------------------

<br>

???+ example "範例程式 樹與剪影 - - - - - - - (專題實作1/3 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=1182&amp;end=1645" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度7:43 章節時間如下】

        * 19:42 樹與剪影 

    === "💻程式碼"

        ```python
        # 模組區 ----------------
        from 海龜模組 import *

        # 全域變數 ----------------
        最大層數 = 11
        轉角 = 20
        開始長度 = 300
        長縮減率 = 0.7
        開始寬度 = 40
        寬縮減率 = 0.7

        # 函式區 ----------------
        def 初始設定() :
            左轉(90)
            速度('fastest')
            tracer(50, 0)
            視窗設定(1000, 1000)
            畫筆顏色('black')
            停筆()
            走到(0,-500)
            bgpic('sunset1.gif')
                
        def 遞迴(層, 長, 寬) :
            if 層 > 最大層數 :
                return
            
            下筆()
            畫筆尺寸(寬)
            向前(長)
            停筆()
            
            右轉(轉角)
            遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
            
            左轉(轉角 * 2)
            遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
            
            右轉(轉角)
            向後(長)
                
        # 主程式 ----------------

        初始設定()

        遞迴(1, 開始長度, 開始寬度)    

        完成()        
        ``` 


<br/><br/><br/>

----------------------------

### ***樹與混沌***

----------------------------


<br>

???+ example "範例程式 樹與混沌 - - - - - - - (專題實作2/3 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=1647&amp;end=2134" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度8:07 章節時間如下】

        * 27:27 樹與混沌

    === "💻程式碼"

        ```python
        # 模組區 ---------------
        from 海龜模組 import *
        import random as 隨機

        # 全域變數 ---------------
        最大層數 = 11
        開始長度 = 300
        長縮減最小 = 0.6
        長縮減最大 = 0.8
        開始寬度 = 40
        寬縮減率 = 0.7
        轉角最小 = 10
        轉角最大 = 40
        夾角最小 = 30
        夾角最大 = 70

        # 函式區 ---------------
        def 初始設定() :
            左轉(90)
            速度('fastest')
            tracer(50, 0)
            視窗設定(1000, 1000)
            畫筆顏色('black')
            停筆()
            走到(0,-500)
            bgpic('sunset1.gif')

                
        def 遞迴(層, 長, 寬) :
            if 層 > 最大層數 :
                return
            
            下筆()
            畫筆尺寸(寬)
            向前(長)
            停筆()
            
            轉角 = 隨機.randint(轉角最小,轉角最大)
            右轉(轉角)
            長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
            遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
            
            夾角 = 隨機.randint(夾角最小,夾角最大)
            左轉(夾角)
            長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
            遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
            
            右轉(夾角 - 轉角)
            向後(長)
            
        # 主程式 ---------------
        初始設定()

        遞迴(1, 開始長度, 開始寬度)
        update()

        完成()        
        ``` 

<br/><br/><br/>

----------------------------

### ***樹與葉***

----------------------------

<br>

???+ example "範例程式 樹與葉 - - - - - - - (專題實作3/3 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FEi_l-Ie1Gc?start=2136&amp;end=2488" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度5:52 章節時間如下】

        * 35:36 樹與葉

    === "💻程式碼"

        ```python
        # 模組區 ---------------
        from 海龜模組 import *
        import random as 隨機

        # 全域變數 ---------------
        最大層數 = 11
        開始長度 = 300
        長縮減最小 = 0.6
        長縮減最大 = 0.8
        開始寬度 = 40
        寬縮減率 = 0.7
        轉角最小 = 10
        轉角最大 = 40
        夾角最小 = 30
        夾角最大 = 70
        葉直徑 = 6
        葉層數 = 5

        # 函式區 ---------------
        def 初始設定() :
            左轉(90)
            速度('fastest')
            tracer(50, 0)
            視窗設定(1000, 1000)
            畫筆顏色('black')
            停筆()
            走到(0,-500)
            bgpic('sunset1.gif')
            隨機.seed(1)

        def 葉() :
            畫點(葉直徑, 'black')
            for 數 in range(4) :
                向前(葉直徑 * 2)
                畫點(葉直徑, 'black')
                向後(葉直徑 * 2)
                右轉(90)
                
        def 遞迴(層, 長, 寬) :
            if 層 > 最大層數 :
                return
            elif 層 > 最大層數 - 葉層數 :
                葉()
            
            下筆()
            畫筆尺寸(寬)
            向前(長)
            停筆()
            
            轉角 = 隨機.randint(轉角最小,轉角最大)
            右轉(轉角)
            長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
            遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
            
            夾角 = 隨機.randint(夾角最小,夾角最大)
            左轉(夾角)
            長縮減率 = 隨機.uniform(長縮減最小, 長縮減最大)
            遞迴(層 + 1, 長 * 長縮減率, 寬 * 寬縮減率)
            
            右轉(夾角 - 轉角)
            向後(長)
            
        # 主程式 ---------------
        初始設定()
        遞迴(1, 開始長度, 開始寬度)
        update()
        完成()        
        ``` 

<br/><br/><br/>


----------------------------
##  📒 結語
----------------------------


<br/><br/><br/>