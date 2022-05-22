---
hide:
  - navigation
---

# 📚 力與運動遊樂場   

<a href="https://zh.wikipedia.org/zh-tw/%E8%89%BE%E8%90%A8%E5%85%8B%C2%B7%E7%89%9B%E9%A1%BF" target="_blank">艾薩克·牛頓爵士</a>是一位英格蘭的物理學家、數學家與天文學家，對數學、自然科學、工業技術等有許多重要的貢獻。牛頓力學是研究物體運動的學問，對於拋體到天文學上的星球運動等，提供了相當準確的結果。在中小學自然領域中的力與運動課程，就是在學習基礎的牛頓力學。

: ![原理與蘋果樹](newton.jpg)

: <sup>(資料來源:</sup>[^newton]<sup>)</sup>

[^newton]: 艾薩克·牛頓 , [維基百科連結](https://zh.wikipedia.org/zh-tw/%E8%89%BE%E8%90%A8%E5%85%8B%C2%B7%E7%89%9B%E9%A1%BF) 

電腦除了計算以外，也可以模擬科學實驗，幫助學習者理解概念。
一起來進行各種有趣的 **力與運動程式模擬** 吧！


??? info "關於物理程式"
    : Py4t物理程式的底層函式庫、範例程式與原始碼。

    : :fontawesome-solid-link: <a href="../../pie4t/" target="_blank">物理學習模組 說明</a>

<br/><br/><br/> 

----------------------------

##  📕 球的彈性(3)

----------------------------

很多同學下課時喜歡打球，球是會有產生各種不同的彈跳，讓球類的活動變得非常有趣。

: ![圓球](campus_basketball.jpg)

: <sup>(資料來源:</sup>[^basketball_court]<sup>)</sup>

[^basketball_court]: 新建中籃球場, By Yu tptw, [維基百科連結](https://zh.wikipedia.org/wiki/File:%E6%96%B0%E5%BB%BA%E4%B8%AD%E7%B1%83%E7%90%83%E5%A0%B420211110.jpg) 

<br/><br/><br/> 

----------------------------

***新增圓球***

----------------------------

利用物理程式來產生物理舞台，在舞台中，只要產生物體並設置好各種物理量，就能產生力與運動的模擬。



: ![圓球](circle.jpg) 

<br/>

利用事件處理函式，設置球的位置，可以增加物理程式的互動性。

??? info "滑鼠操作事件"

    : 在某些程式中，會進一步將滑鼠操作細分多個動作，並觸發對應的事件

    : :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#mouse_event" target="_blank">滑鼠操作事件</a>

<br/>

首先，設計一個按下滑鼠後可以新增圓球的程式吧！

<br/>

???+ example "範例程式 新增圓球 - - - - - - -  (球的彈性1/3 新檔)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/sIAgw3FryX8?start=1&amp;end=128" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:07 章節時間如下】

        * 0:00 存檔、匯入模組
        * 0:24 新增圓球

    === "💻程式截圖"

        ![程式截圖](snapshot/bounce_ball_add.jpg)


??? info "模擬主迴圈？流程？"

    : 什麼是「模擬主迴圈」？它的程式結構與演算流程是什麼？

    : :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#event_driven" target="_blank">事件驅動程式 結構與流程</a>

    -----------------------------

    : 補充資料 
    
    : :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E4%BA%8B%E4%BB%B6%E9%A9%85%E5%8B%95%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88" target="_blank">維基百科: 事件驅動程式設計</a>

<br/><br/><br/> 

----------------------------

***恢復係數***

----------------------------

想一想，球的彈性是什麼？彈性可以測量嗎？

如何知道一顆球的彈性好不好呢？
 
<iframe width="560" height="315" src="https://www.youtube.com/embed/_RWqefx0vAg?start=95&amp;end=215" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(2分00秒, 資料來源:</sup>[^super_bounce]<sup>)</sup>



<br/><br/>

恢復係數可以衡量兩個物體在碰撞後的反彈程度。影片中測量籃球恢復係數的說明如下：


![恢復係數](cor_explain.jpg) 

: <sup>(資料來源:</sup>[^super_bounce]<sup>)</sup>

[^super_bounce]: 【Fun科學】超彈力橡皮筋球, By 佑來了, [youtube連結](https://www.youtube.com/watch?v=_RWqefx0vAg) 

<br/><br/>

藉由恢復係數的設置，用程式來模擬不同彈性的球吧！

<br/>

???+ example "範例程式 恢復係數 - - - - - - - (球的彈性2/3 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/sIAgw3FryX8?start=131&amp;end=251" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:00 章節時間如下】

        * 2:11 恢復係數

    === "💻程式截圖"

        ![程式截圖](snapshot/bounce_ball_restitution.jpg)


??? info "補充資料"

    : 了解更多 :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E6%81%A2%E5%A4%8D%E7%B3%BB%E6%95%B0" target="_blank">恢復係數</a>

    : 恢復係數與球類比賽有什麼關係？ :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E8%81%B7%E6%A3%92%E6%AF%94%E8%B3%BD%E7%94%A8%E7%90%83%E7%88%AD%E8%AD%B0" target="_blank">中華職棒比賽用球爭議</a>

<br/><br/><br/> 

----------------------------

***超強彈性體***

----------------------------

將兩顆很有彈性的球互相碰撞，會發生什麼事？

: <iframe width="560" height="315" src="https://www.youtube.com/embed/_RWqefx0vAg?start=227&amp;end=414" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(3分07秒, 資料來源:</sup>[^super_bounce]<sup>)</sup>

<br/><br/>

太奇妙了！將兩顆很有彈性的球在一起，下方的球較大，上方的球較小，竟然就變成可以超越原本高度的彈性體。

: ![超強彈性體](super_bounce.jpg) 

: <sup>(資料來源:</sup>[^super_bounce]<sup>)</sup>



可以用程式來模擬這個現象嗎？試著動手寫寫看。

<br/>

???+ example "範例程式 超強彈性體 - - - - - - - (球的彈性3/3 接續)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/sIAgw3FryX8?start=253&amp;end=410" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:37 章節時間如下】

        * 4:14 超強彈性體

    === "💻程式截圖"

        ![程式截圖](snapshot/bounce_ball_super.jpg)


??? question "更多練習"

    : 影片中有3顆球的實驗，請你試著改寫程式，讓大、中、小球組成超強彈性體吧。

??? info "彈性碰撞"

    : 超強彈性體的原理是什麼？請參考:fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E5%BD%88%E6%80%A7%E7%A2%B0%E6%92%9E" target="_blank">維基百科: 彈性碰撞</a>

<br/><br/><br/> 



----------------------------

##  📒 力與斜面(4)

----------------------------

公園遊戲區裡常會出現的溜滑梯，當溜滑梯的傾斜度不同時，溜起來的感覺也不同。

: ![溜滑梯](slide.jpg)

: <sup>(資料來源:</sup>[^slide]<sup>)</sup>

[^slide]: 位於葫蘆埤自然公園中的溜滑梯, By 月亮灣, [維基百科連結](https://zh.wikipedia.org/wiki/File:葫蘆埤自然公園溜滑梯.jpg)

<br/>

----------------------------

***新增球與斜面***

----------------------------



用斜面來模擬溜滑梯，在程式中要如何做出不同的傾斜度呢？


: ![不同斜面](multiple_slides.jpg) 

<br/>

Py4t內建了物理舞台地形的輔助功能，能更容易地做出各種物理模擬，輔助操作如下圖：

: ![地形輔助](terrain_assist.jpg)

<br/>


動手做做看，利用輔助功能，建立出不同的斜面。

<br/>

???+ example "範例程式 新增球與斜面 - - - - - - -  (力與斜面1/4 新檔)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=2&amp;end=302" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度5:00 章節時間如下】

        * 0:00 存檔、匯入模組
        * 0:49 新增球與斜面

    === "💻程式截圖"

        ![程式截圖](snapshot/force_and_slide_terrain.jpg)


<br/><br/><br/> 



----------------------------

***落下速度比較***

----------------------------

當球在不同的斜面落下時，哪個快？哪個慢？

: ![球在不同斜面](ball_on_slide.jpg) 

<br/>

利用物理程式輔助功能，來模擬球從斜面落下的結果。

<br/>

???+ example "範例程式 速度比較 - - - - - - - (力與斜面2/4 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=303&amp;end=339" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


        【長度0:36 章節時間如下】

        * 5:03 速度比較


    === "💻程式截圖"

        ![程式截圖](snapshot/force_and_slide_velocity.jpg)


??? info "補充資料" 
    
    : :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=TMEB1KoJpNI" target="_blank">youtube: 吉娃斯科學小教室 : 斜面運動、重力、支撐力</a>

    


<br/><br/><br/> 

----------------------------

***摩擦力***

----------------------------

什麼是摩擦力？如果摩擦力消失一分鐘會如何？

: <iframe width="560" height="315" src="https://www.youtube.com/embed/JdMkAvibBec?start=12&amp;end=96" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分24秒, 資料來源:</sup>[^disappear_friction]<sup>)</sup>

[^disappear_friction]: 如果摩擦力消失一分鐘？, By 大膽科學, [youtube連結](https://www.youtube.com/watch?v=JdMkAvibBec&t=12s)

<br/>

摩擦力作用於物體的相反方向，並與相互摩擦的物體有關。

摩擦係數由滑動面的性質、粗糙度等因素決定。滑動面越粗糙，摩擦係數越大。

: ![摩擦力](friction_direction.jpg) 

: <sup>(資料來源:</sup>[^friction_example]<sup>)</sup>

[^friction_example]: 摩擦力受各性質的影響, 引用自中學生網站, [pdf連結](https://www.shs.edu.tw/works/essay/2011/03/2011033016033626.pdf)

設定物體的不同摩擦係數，寫出程式並觀察模擬的結果。

<br/>

???+ example "範例程式 摩擦力 - - - - - - - (力與斜面3/4 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=341&amp;end=504" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:43 章節時間如下】

        * 5:40 摩擦力

    === "💻程式截圖"

        ![程式截圖](snapshot/force_and_slide_friction.jpg)


??? info "補充資料" 
    
    : :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=9DMUl30gFXk" target="_blank">youtube: myViewBoard 原創內容：摩擦力</a>

    : :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=Bhm3iPFqYEo" target="_blank">youtube: 均一教育平台【八下理化】【觀念】摩擦力</a>

    

<br/><br/><br/> 

----------------------------

***施加力量***

----------------------------

<iframe width="560" height="315" src="https://www.youtube.com/embed/oPsfwZXCf1s?start=14&amp;end=77" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分03秒, 資料來源:</sup>[^skateboard]<sup>)</sup>

[^skateboard]: 8歲女孩成功挑戰5公尺極限滑板, By 即新聞, [youtube連結](https://www.youtube.com/watch?v=oPsfwZXCf1s&t=14s)


在滑板上以一定的速度衝上斜坡時，會發生什麼事？

設置物體的衝力後，以程式模擬衝上斜坡的現象。

<br/>

???+ example "範例程式 施力 - - - - - - - (力與斜面4/4 接續)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U3dnShwtdDQ?start=505&amp;end=633" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:08 章節時間如下】

        * 8:26 施力


    === "💻程式截圖"

        ![程式截圖](snapshot/force_and_slide_impulse.jpg)

??? info "補充資料" 
    
    : :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=yGPpFelGeEQ" target="_blank">youtube: 國中理化教學資料庫 伽利略斜面實驗</a>

<br/><br/><br/> 

----------------------------

##  📗 噴射拋體(2)

----------------------------

推鉛球，是一個常見的運動會比賽項目。

: <iframe width="560" height="315" src="https://www.youtube.com/embed/EkiaYNEAagA?start=0&amp;end=118" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分58秒, 資料來源:</sup>[^shot_put]<sup>)</sup>

[^shot_put]: 超越人類極限【金牌鉛球國手】巨人手掌宛如人體砲臺發射器, By 健人蓋伊, [youtube連結](https://www.youtube.com/watch?v=EkiaYNEAagA)

鉛球丟出後，就是一個在空中的拋物體。

<br/><br/><br/> 

----------------------------

***拋體運動***

----------------------------

鉛球被推出時，在空中的軌跡是什麼樣的線條？

: <iframe width="560" height="315" src="https://www.youtube.com/embed/bhavS93SEaM?start=32&amp;end=97" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分05秒, 資料來源:</sup>[^projectile_motion]<sup>)</sup>

[^projectile_motion]: 吉娃斯科學小教室｜#37 : 拋體運動｜動能、重力、運動半徑｜兒童科普動畫, By 
EngineTV 原金動畫, [youtube連結](https://www.youtube.com/watch?v=bhavS93SEaM&t=32s)

<br/><br/>

如果想用程式來模擬拋體，要先決定發射位置與速度。

將圓球發射位置定在視窗左下角，用滑鼠的座標位置當作速度的大小，操作起來較為直覺，如下圖：


: ![滑鼠速度向量](mouse_vector_from_origin.png) 

<br/><br/>

一起來動手寫寫看。

<br/>

???+ example "範例程式 拋體運動 - - - - - - - (噴射拋體1/2 新檔)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/UgJ6ed8H03Q?start=2&amp;end=192" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度3:10 章節時間如下】

        * 0:00 存檔、匯入模組
        * 0:31 拋體運動

    === "💻程式截圖"

        ![程式截圖](snapshot/projectile_basic.jpg)


??? info "補充資料" 

    : :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E6%8B%8B%E9%AB%94" target="_blank">維基百科: 拋體</a>

    : :fontawesome-solid-link: <a href="https://www.zetria.org/view.php?subj=physics&chap=lfym2aorgz" target="_blank">學呀: 拋物線運動</a>


<br/><br/><br/>


----------------------------

***連續噴射***

----------------------------

完成了基本的拋體運動程式，接下來可以做出什麼變化呢？

: <iframe width="560" height="315" src="https://www.youtube.com/embed/HGBoMrsC0iE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(9秒, 資料來源:</sup>[^sprinkler]<sup>)</sup>

[^sprinkler]: 太陽能系統-自動灑水器-噴水頭, By CHIJIJOHNNY, [youtube連結](https://www.youtube.com/watch?v=HGBoMrsC0iE)

<br/><br/>


讓我們把多顆小圓球當成拋體，做出噴水的簡單模擬。

這次將發射位置定在視窗中間底部，當發射位置改變時，要如何用滑鼠來呈現速度？為了達到直覺的操作，需做以下的修正：

<br/>

: ![滑鼠速度向量2](mouse_vector_from_middle_bottom.png) 

<br/><br/>

一起來動手寫寫看。

<br/>

???+ example "範例程式 連續噴射 - - - - - - - (噴射拋體2/2 接續)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/UgJ6ed8H03Q?start=193&amp;end=383" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度3:10 章節時間如下】

        * 3:13 連續噴射

    === "💻程式截圖"

        ![程式截圖](snapshot/projectile_continuous.jpg)




<br/><br/><br/>

----------------------------

##  📗 重力控制(2)

----------------------------

重力是什麼？如果失去了重力會如何？



: <iframe width="560" height="315" src="https://www.youtube.com/embed/oyXkJ3OYxfQ?start=32&amp;end=190" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(2分38秒, 資料來源:</sup>[^no_gravity]<sup>)</sup>

[^no_gravity]: 如果我們失去引力五秒？ , By 大膽科學, [youtube連結](https://youtu.be/oyXkJ3OYxfQ)


除非到外太空，不然在地球上很難進行重力的實驗。

經由物理程式的模擬，可以做出無重力，甚至是重力反轉的效果。





----------------------------

***無重力狀態***

----------------------------


你知道如何在太空中做披薩嗎？

: <iframe width="560" height="315" src="https://www.youtube.com/embed/UVGgrLqsAzw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分00秒, 資料來源:</sup>[^space_pizza]<sup>)</sup>

[^space_pizza]: Pizza Night on the Space Station!, By NASA, [youtube連結](https://youtu.be/UVGgrLqsAzw)

在太空中的物體若沒有固定好，物體受到一點力量，就會照著慣性的作用，產生漂浮的現象。


在物理模擬程式中，以重力加速度的平面向量來表示重力，向量代表著重力的方向及大小。

: ![上下向量](y_vector_explained.png) 

知道了這些，就可以來寫無重力的模擬程式。

<br/>

???+ example "範例程式 無重力狀態 - - - - - - - (重力控制1/2 新檔)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/I_i5OyGIObQ?start=0&amp;end=343" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度5:43 章節時間如下】

        * 0:00 存檔、匯入模組
        * 0:31 無重力狀態

    === "💻程式截圖"

        ![程式截圖](snapshot/gravity_float.jpg)


??? info "慣性與向量" 
    
    : :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E6%85%A3%E6%80%A7" target="_blank">維基百科: 慣性</a>

    : :fontawesome-solid-link: <a href="https://youtu.be/4H04xpngVlo?list=PLTQ2T0cDHYPfypQn6t_sXV1N581kwf7Ei" target="_blank">youtube: 平面運動 【觀念】向量（1）向量的表示方法</a>
    

<br/><br/><br/> 

----------------------------

***重力搬運***

----------------------------

除了上下的向量，也可以使用左右的向量

: ![左右向量](x_vector_explained.png) 

<br/>

如果可以控制4個方向的向量，可以做什麼呢？

來看看在國際太空站的太空人如何進行趣味奧運比賽。

: <iframe width="560" height="315" src="https://www.youtube.com/embed/ZlPpHILyEl4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分14秒, 資料來源:</sup>[^space_olympics]<sup>)</sup>

[^space_olympics]: Highlights from the first-ever space Olympics!, By 
NASA, [youtube連結](https://www.youtube.com/watch?v=ZlPpHILyEl4)

<br/>


請發揮你的創意，用控制重力的程式做出搬運物體的遊戲。


???+ example "範例程式 重力搬運 - - - - - - - (重力控制2/2 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/I_i5OyGIObQ?start=347&amp;end=667" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度5:20 章節時間如下】

        * 5:47 重力搬運


    === "💻程式截圖"

        ![程式截圖](snapshot/gravity_game.jpg)


??? info "結構化程式設計"

    : :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#if" target="_blank">選擇結構</a>

??? info "重力" 
   
    : :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=VB20FLopIWg" target="_blank">youtube: 高一物理【觀念】重力</a>
    
    : :fontawesome-solid-link: <a href="https://zh.wikipedia.org/wiki/%E5%BC%95%E5%8A%9B" target="_blank">維基百科: 重力</a>

<br/><br/><br/> 

----------------------------

##  📙 彈性排列(3)

----------------------------

什麼是繩波？

: <iframe width="560" height="315" src="https://www.youtube.com/embed/P7QrXW4ky34" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(31秒, 資料來源:</sup>[^rope_wave]<sup>)</sup>

[^rope_wave]: 繩波示波器, By 國中理化教學資料庫, [youtube連結](https://www.youtube.com/watch?v=P7QrXW4ky34)


讓我們用多顆球的排列並彈跳，來做出類似繩波的效果。

<br/>

----------------------------

***固定球數***

----------------------------

如何一次產生多顆球並產生有變化的彈跳呢？

: ![彈性排列想法](bounce_array_thought.jpg)

利用之前的恢復係數，讓我們來實作程式吧！

<br/>

???+ example "範例程式 固定球數 - - - - - - - (彈性排列1/3 新檔)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U9DAN6NbkbY?start=0&amp;end=240" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度4:00 章節時間如下】

        * 0:00 存檔、匯入模組
        * 1:04 固定球數        

    === "💻程式截圖"

        ![程式截圖](snapshot/bounce_array_constant.jpg)

??? info "結構化程式設計"

    : :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#for" target="_blank">計次式重複 (for 迴圈)</a>

    : :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#loop_var" target="_blank">迴圈變數與圈數</a>


<br/><br/><br/> 

----------------------------

***變數模式識別***

----------------------------


如果要從10顆球，可以隨意調整成20或40或80顆，程式要如何寫呢？



識別變數的模式，找出各個變數之間的關係！

: ![變數模式識別](variable_pattern.jpg)

??? info "運算思維"

    :fontawesome-solid-link: <a href="../basic/comthink/#_4" target="_blank">樣式辨識</a>

<br/>

想清楚了嗎？動手寫寫看。

<br/>

???+ example "範例程式 變數模式識別 - - - - - - - (彈性排列2/3 接續)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U9DAN6NbkbY?start=243&amp;end=406" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度2:43 章節時間如下】

        * 4:03 變數模式識別        


    === "💻程式截圖"

        ![程式截圖](snapshot/bounce_array_pattern.jpg)


<br/><br/><br/>

----------------------------

***不同波動變化***

----------------------------

利用不同的彈性排列變化，來做出有規律的彈跳效果。

: ![彈性排列](bounce_array.jpg)



<br/>


一起來寫寫看。

???+ example "範例程式 不同波動變化 - - - - - - - (彈性排列3/3 接續)"


    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/U9DAN6NbkbY?start=408&amp;end=660" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度4:12 章節時間如下】

        * 6:48 不同波動變化

    === "💻程式截圖"

        ![程式截圖](snapshot/bounce_array_various.jpg)

??? info "結構化程式設計"

    : :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#if_else" target="_blank">雙向選擇結構</a>

??? info "波"

    : 多顆圓球不斷彈跳的樣子，會聯想到什麼？ 
    
    : :fontawesome-solid-link: <a href="https://www.youtube.com/watch?v=k80ID8yVJyg" target="_blank">youtube: 繩波的反射示範實驗</a>

    : :fontawesome-solid-link: <a href="https://youtu.be/bHIoI4-iB_A" target="_blank">youtube: 量子現象【觀念】波粒二象性－物質波（高一物理）</a>

<br/><br/><br/>

----------------------------

##  ⭐ 進階專題

----------------------------

太棒了，經過了前面的課程，相信你已經學會基本的物理模擬程式，並能改變物體的物理性質來做出不同的變化。

如果想要更進一步，可以挑戰下面的程式專題哦！


: :fontawesome-solid-link: <a href="../project_collision_lab/" target="_blank">物理撞擊實驗室</a>

<br/><br/><br/>