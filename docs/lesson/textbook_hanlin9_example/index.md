---
hide:
  - navigation
---

# 📚 Python程式設計-計算篇 (9上翰林版2-2)


本課程是做為資訊科技教科書的補充教材與範例操作，搭配課本中的內容，來學習Python的基本輸入輸出，資料型態的轉換、內建函式的使用、認識選擇與重複結構…等，入門文字型程式語言，銜接高中資訊科技課程。

實際撰寫程式時，搭配Py4t專為中小學學生設計的便利貼與輔助排版功能，簡化Python程式撰寫的步驟。希望讓學生能更專注於程式的思考及運算思維的培養。


??? info "教科書資料引用來源"

     本課程之例題、範例程式及Scratch對照圖片，均引用自翰林出版資訊科技教科圖書9上第2章-從Scratch到Python，2-2Python程式設計-計算篇


<br/><br/><br/>

----------------------------

##  📕 哈囉 

----------------------------

在校園的早晨，常常會看到同學之間互相道早安。仔細想一想，「當別人跟我說早安，而我也向他打招呼」，在這個情境中發生了什麼事？

<br/>

: ![打招呼](listen_and_say.jpg)

<br/>

人與人之間的「聽」跟「說」，對電腦來說，有沒有類似的動作？

<br/>

: ![輸入輸出](input_output.jpg)

<br/>

**請設計一個程式，讓使用者輸入名字後，電腦會將名字呈現在畫面上與使用者打招呼。**

<br/>


???+ example "範例 哈囉程式"




    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/XdwNrOKtyUU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/hello.jpg)

    === "🗒️Scratch積木對照"

        ![Scratch對照](snapshot/hello_scratch.png)

??? info "補充資料 馮紐曼與現代電腦架構"

     :fontawesome-solid-link: <a href="https://www.inside.com.tw/article/9507-von-neumann-architecture" target="_blank">【Lynn 寫點科普】你知道你正在用的電腦是 70 年前發明的馮紐曼架構嗎？</a>


<br/><br/><br/>


----------------------------

##  📙 求三數之和 

----------------------------

除了把輸入的文字直接顯示，有時我們會想要把資料做一些計算，比如是加法的運算。

但是在Python程式中，「文字」卻不能直接拿來做計算，這到底是為什麼呢？


<br/><br/>

: ![文字數字差異](number_string_in_memory.png)

<br/>

所以記得要把「輸入文字」先轉換成「整數」哦。

接下來，**請設計一個程式，讓使用者輸入三個數字後，再呈現三個數字相加的和**。

<br/>

???+ example "範例 求三數之和"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/fgobY4o2BTU?start=2&amp;end=306" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/sum_of_3_numbers.jpg)
        

    === "🗒️Scratch積木對照"

        
        ![Scratch對照](snapshot/sum_of_3_numbers_scratch.png)

<br/><br/><br/>


----------------------------

##  📒 求平均數 

----------------------------

計算後的數字，也可以再轉換成字串，做出不同的輸出組合。再來做個練習。

**請設計一個程式，讓使用者輸入兩個數字後，再呈現兩個數字的平均值**。

程式資料的轉換流程如下：

<br/>

: ![資料型態與轉換](data_type_transform.jpg)

<br/>

請試著動手寫寫看。

<br/>

???+ example "範例 求平均數"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/4_UyYrlISZw?start=2&amp;end=336" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/average.jpg)
        

    === "🗒️Scratch積木對照"

        
        ![Scratch對照](snapshot/average_scratch.png)


<br/><br/><br/>

----------------------------

##  📗 計算學期成績 

----------------------------


除了計算以外，我們也常常會對結果做分析，從數字中取出有意義的訊息。


<br/>

: ![資料分析](analyze_data.jpg)

<br/>

**請設計一個程式，讓使用者輸入各項成績後，再將各項成績轉換為學期成績，並判
斷學期成績是否及格？（其中，作業成績占 40％，測驗成績占 40％，平時成績占
20％，學期成績 60 分為及格分數。）**


<br/>

???+ example "範例 計算學期成績"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/H4ouv9LyflI?start=2&amp;end=555" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/grade.jpg)
        

    === "🗒️Scratch積木對照"

        
        ![Scratch對照](snapshot/grade_scratch.png)

??? abstract "結構化程式設計"

    :fontawesome-solid-link: <a href="../basic/scratch_python_compare/#_6" target="_blank">選擇結構</a>

<br/><br/><br/>


----------------------------

##  📘 累加計算 

----------------------------


???+ example "範例 累加計算"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/DhcDjRpchoA?start=2&amp;end=399" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/accumulation.jpg)
        

        註：課本範例使用sum做為變數名稱，但sum為python內建函式，不建議使用，故在本範例中改為total
        

    === "🗒️Scratch積木對照"

        ![Scratch對照](snapshot/accumulation_scratch.png)

        
        
<br/><br/><br/>


----------------------------

##  📕 密碼檢查

----------------------------

???+ example "範例 密碼檢查"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/rZMMfeqgRnw?start=2&amp;end=505" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/check_password.jpg)       

    === "🗒️Scratch積木對照"

        ![Scratch對照](snapshot/check_password_scratch.png)

<br/><br/><br/>

----------------------------

##  📙 任意數的所有因數

----------------------------

???+ example "範例 任意數的所有因數"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/_5sLEY8aFAA?start=2&amp;end=330" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/factors.jpg)       

    === "🗒️Scratch積木對照"

        ![Scratch對照](snapshot/factors_scratch.png)



<br/><br/><br/>

----------------------------

##  📒  抽獎

----------------------------

???+ example "範例 抽獎"

    === "🎦Py4t操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/vOE9gW7T2Fc?start=2&amp;end=464" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    === "💻Python程式截圖"

        ![程式截圖](snapshot/lottery.jpg)       

    === "🗒️Scratch積木對照"

        ![Scratch對照](snapshot/lottery_scratch.png)

<br/><br/><br/>