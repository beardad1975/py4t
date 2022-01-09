# 📚Py4t課程 - 力與運動遊樂場

電腦除了計算，也可以模擬科學實驗，幫助學習者理解概念。

讓我們使用Py4t來進行各種有趣的 **力與運動程式實驗** 吧！

相信你在體驗之後，未來學習相關的自然課或理化課時，就會更有 **學習動力**。

----------------------------

##  📕 球的彈性

很多同學下課時喜歡打球，球能做出各種不同的彈跳，要如何量測彈性呢？

----------------------------

**階段1: 新增圓球**

: ![圓球](circle.jpg) 

: 利用基本的程式來產生物理舞台，按下滑鼠後可以新增圓球。

: 一起動手來寫程式吧！

??? example "Let's Code 新增圓球"

    :fontawesome-solid-link: <a href="../../pie4t/bounce_ball/#_1" target="_blank">Py4t範例程式 新增圓球</a>

??? info "補充資料"

    什麼是「模擬主迴圈」？

    程式除了由依序執行、條件分支與重複結構，還有別的執行方式嗎？
    
    請參考:fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E4%BA%8B%E4%BB%B6%E9%A9%85%E5%8B%95%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88" target="_blank">維基百科: 事件驅動程式設計</a>

<br/><br/><br/> 

----------------------------

**階段2: 恢復係數**

: 如何知道一顆球的彈性好不好呢？
 
<iframe width="560" height="315" src="https://www.youtube.com/embed/_RWqefx0vAg?start=95&amp;end=215" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br/><br/>

: 恢復係數可以衡量兩個物體在碰撞後的反彈程度


![恢復係數](cor_explain.jpg) 
: (圖片來源[^1])

[^1]: 引用自【Fun科學】超彈力橡皮筋球 https://www.youtube.com/watch?v=_RWqefx0vAg 

<br/><br/>

: 讓我們用程式來模擬不同彈性的球吧！

??? example "Let's Code 恢復係數"

     :fontawesome-solid-link: <a href="../../pie4t/bounce_ball/#2" target="_blank">Py4t範例程式 恢復係數</a>

??? info "補充資料"

    了解更多 :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E6%81%A2%E5%A4%8D%E7%B3%BB%E6%95%B0" target="_blank">恢復係數</a>

    恢復係數與球類比賽有什麼關係？ :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E8%81%B7%E6%A3%92%E6%AF%94%E8%B3%BD%E7%94%A8%E7%90%83%E7%88%AD%E8%AD%B0" target="_blank">中華職棒比賽用球爭議</a>

<br/><br/><br/> 

----------------------------

**階段3: 超強彈性體**

: 將兩顆很有彈性的球互相碰撞，會發生什麼事？

<iframe width="560" height="315" src="https://www.youtube.com/embed/_RWqefx0vAg?start=227&amp;end=414" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br/><br/>



![超強彈性體](super_bounce.jpg) 
: (圖片來源[^1])

: 兩顆很有彈性的球在一起，下方的球數倍大於上方的球，就可以組成超越原本的彈性體

: 有沒有覺得很神奇？讓我們用程式來模擬看看吧！

??? example "Let's Code 超強彈性體"

     :fontawesome-solid-link: <a href="../../pie4t/bounce_ball/#3" target="_blank">Py4t範例程式 超強彈性體</a>

??? question "更多練習"

    影片中有3顆球的實驗，請你試著改寫程式，讓大、中、小球組成超強彈性體吧。

??? info "補充資料"

     超強彈性體的原理是什麼？請參考:fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E5%BD%88%E6%80%A7%E7%A2%B0%E6%92%9E" target="_blank">維基百科: 彈性碰撞</a>

<br/><br/><br/> 

----------------------------

##  📙 彈跳吧！圓球

: 如果一次產生多顆球，如何來產生規律的彈跳呢？

![彈性排列](bounce_array.jpg)

: 利用之前的恢復係數，讓我們來實作程式吧！

??? example "Let's Code 彈跳吧！圓球"

     :fontawesome-solid-link: <a href="../../pie4t/bounce_array/" target="_blank">Py4t範例程式 彈跳圓球</a>

??? question "更多練習"

    影片中有偶數球有不同的彈性變化，請你試著改寫成3種彈性變化吧。(提示：使用 if elif else，並利用除數為3的餘數)

??? info "補充資料"

    多顆圓球不斷彈跳的樣子，會聯想到什麼？ 
    
    :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=k80ID8yVJyg" target="_blank">youtube: 繩波的反射示範實驗</a>

    :fontawesome-solid-link: <a href="https://youtu.be/bHIoI4-iB_A" target="_blank">youtube: 量子現象【觀念】波粒二象性－物質波（高一物理）</a>

<br/><br/><br/> 

----------------------------

##  📒 力與斜面

**階段1: 新增球與斜面**

: 溜滑梯的傾斜度不同，溜起來的感覺也不同。

: ![溜滑梯](slide.jpg)

: (圖片來源[^2])

<br/>

[^2]: 引用自維基百科 https://zh.wikipedia.org/wiki/File:葫蘆埤自然公園溜滑梯.jpg

: 用斜面來模擬溜滑梯，在程式中要如何做出不同的傾斜度呢？


: ![不同斜面](multiple_slides.jpg) 


: Py4t物理模組內建了地形的輔助功能，操作如下圖

: ![地形輔助](terrain_assist.jpg)

: 動手做做看，建立不同的斜面

??? example "Let's Code 新增球與斜面"

     :fontawesome-solid-link: <a href="../../pie4t/force_and_slide/#1" target="_blank">Py4t範例程式 新增球與斜面</a>

<br/><br/><br/> 

----------------------------

**階段2: 速度比較**

球在不同的斜面落下，會怎樣呢？

: ![球在不同斜面](ball_on_slide.jpg) 

用程式來模擬看看

??? example "Let's Code 速度比較"

     :fontawesome-solid-link: <a href="../../pie4t/force_and_slide/#2" target="_blank">Py4t範例程式 速度比較</a>

??? info "補充資料" 
    
    :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=TMEB1KoJpNI" target="_blank">youtube: 吉娃斯科學小教室 : 斜面運動、重力、支撐力</a>

    


<br/><br/><br/> 

----------------------------

**階段3: 摩擦力**


<iframe width="560" height="315" src="https://www.youtube.com/embed/JdMkAvibBec?start=12&amp;end=96" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br/>

: 摩擦力作用於物體的相反方向

: ![摩擦力](friction_direction.jpg) 

: (圖片來源[^3])

[^3]: 引用自中學生網站 https://www.shs.edu.tw/works/essay/2011/03/2011033016033626.pdf

用程式來模擬看看

??? example "Let's Code 摩擦力"

     :fontawesome-solid-link: <a href="../../pie4t/force_and_slide/#3" target="_blank">Py4t範例程式 摩擦力</a>

??? info "補充資料" 
    
    :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=9DMUl30gFXk" target="_blank">youtube: myViewBoard 原創內容：摩擦力</a>

    :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=Bhm3iPFqYEo" target="_blank">youtube: 均一教育平台【八下理化】【觀念】摩擦力</a>

    

<br/><br/><br/> 

----------------------------

**階段4: 施力**

<iframe width="560" height="315" src="https://www.youtube.com/embed/oPsfwZXCf1s?start=14&amp;end=77" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

衝上斜坡時，會發生什麼事？

用程式來模擬看看

??? example "Let's Code 施力"

    :fontawesome-solid-link: <a href="../../pie4t/force_and_slide/#4" target="_blank">Py4t範例程式 施力</a>

??? info "補充資料" 
    
    :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=yGPpFelGeEQ" target="_blank">youtube: 國中理化教學資料庫 伽利略斜面實驗</a>

<br/><br/><br/> 

----------------------------