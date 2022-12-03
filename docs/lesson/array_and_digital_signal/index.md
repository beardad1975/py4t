---
hide:
  - navigation
---

# 📚 陣列與數位訊號

: 引言(陣列 訊號)

??? info "關於視覺與聲音教學模組"

    : ...

    : :fontawesome-solid-link: <a href="../../turtle4t/" target="_blank">...</a>

<br/><br/><br/> 



----------------------------

##  📙 陣列資料結構

### ***list與array***

----------------------------




<br/><br/><br/> 



----------------------------

### ***numpy多維陣列*** 

----------------------------




<br/><br/><br/> 

----------------------------

##  📗 聲音與1維陣列(2) 

### ***聲音的要素***

----------------------------

: 聲音是一種由振動產生的波動，聲波通過空氣的傳播，當耳朵接收到聲波時，就會讓我們聽見聲音。

: 那聲音有什麼基本的組成要素呢？一起來看看下面的影片：

: <iframe width="560" height="315" src="https://www.youtube.com/embed/d6Lzym61NDg?start=0&amp;end=108" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分48秒, 資料來源:</sup>[^sound_elements]<sup>)</sup>

[^sound_elements]: 【波動與聲音】 聲音的三要素, By 均一教育平台 Junyi Academy , [youtube連結](https://youtu.be/d6Lzym61NDg) 

: 經由影片的說明，我們可以得知，聲音的三要素是「**音調**」、「**響度**」與「**音色**」。

<br/><br/>

: 聲波不同的振動頻率，會產生不同的音調，讓我們感受到高音與低音。


: ![frequency](frequency.jpg)

: <sup>(資料來源:</sup>[^sound_elements]<sup>)</sup>


<br/><br/>

: 特定的頻率，可依規則組成不同的音階，讓聲音變成悅耳的音樂，音階與頻率的對照表如下：


: ![音高頻率表](pitch_frequency.jpg)

: <sup>(資料來源:</sup>[^pitch_frequency]<sup>)</sup>

[^pitch_frequency]: Make Maker . Arduino 蜂鳴器發聲, [http://jiader.blogspot.com/2018/08/arduino.html](http://jiader.blogspot.com/2018/08/arduino.html)


<br/><br/>

: 聲波的振動幅度大小，會產生不同的聲音響度，讓我們感受到大聲與小聲。


: ![amplitude](amplitude.jpg)

: <sup>(資料來源:</sup>[^sound_elements]<sup>)</sup>


<br/><br/>

: 不同聲源的聲波有不同的波形，會產生不同的音色，讓我們可以分辨出如人聲與樂器聲的差異。

: ![wave_form](wave_form.jpg)

: <sup>(資料來源:</sup>[^sound_elements]<sup>)</sup>




<br/><br/><br/> 

----------------------------

###  ***聲音訊號*** 

----------------------------

: 聲音訊號可以定義為「**隨著時間改變的振幅大小**」，在經過**取樣**與**量化**的處理後，就可以將聲音**數位化**。音訊的數位聲波資訊可以利用「**1維陣列的資料結構**」來存放。為了更清楚地觀察聲波變化，我們可以將音訊的資料陣列以圖表的方式來呈現。

: ![聲音陣列圖表](sound_array_chart.png)

<br/><br/>

: 真實世界中的聲波是連續的類比訊號，如果要將聲波數位化，變成一個個離散的數位訊號，就必須對聲音訊號做「取樣」的動作，請看下圖：

: ![聲音取樣](sampling.png)

<br/><br/>

: 了解了「取樣率」與「取樣週期」後，看看下圖中，在常見的數位音訊取樣率。取樣率越高，數位音訊的品質就越好。


: ![常見取樣率](sample_rate_example.jpg)

: <sup>(資料來源:</sup>[^sample_rate_example]<sup>)</sup>

[^sample_rate_example]: 取樣率, [維基百科連結](https://zh.wikipedia.org/zh-tw/%E9%87%87%E6%A0%B7%E7%8E%87) 

<br/><br/>

: 在將聲音訊號取樣時，取到的值是聲音的振幅大小(與響度有關)，這個動作是「量化」，可以使用不同位元數來表示量化的值。採用的位元數越高，振幅會有更細膩的變化，音訊的品質就越好。


: ![聲音量化](quantization.png)

<br/><br/>



: ![生成音訊](sound_source_example.jpg)

: * 自然界中的聲音可以弦波來表示，弦波是類比訊號的代表。

: * 方波是只有「低」與「高」這兩種變化，常出現在電子訊號的處理，是數位訊號的代表。

: * 如果將量化值以隨機方式產生，就會是發出沙沙聲的雜訊。而其中的白噪音是一種均勻分布，平均值為0，樣本之間互相獨立的均勻雜訊。根據一些研究顯示，在一定的條件下，白噪音可以幫助睡眠(註[^white_noise_and_sleeping])。

[^white_noise_and_sleeping]: hello醫師, 白噪音可助眠～這3種潛在影響要注意, [https://helloyishi.com.tw/sleep/a-good-nights-sleep/what-does-white-noise-affect-us/](https://helloyishi.com.tw/sleep/a-good-nights-sleep/what-does-white-noise-affect-us/)


<br/><br/>

: 請動手實作程式。

???+ example "範例程式 聲音訊號 - - - - - - - (聲音與1維陣列 1/2 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/-BMUwYRELw4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度14:47 章節時間如下】

        * 0:00 存檔、切換便利貼
        * 1:00 聲音、陣列與圖表
        * 5:50 取樣與量化
        * 10:34 陣列切片與音源



    === "💻程式截圖"

        ![程式截圖](snapshot/sound_signal.jpg) 


<br/><br/><br/> 

----------------------------

###  ***音訊處理*** 

----------------------------

: 樂器的波形

: 人聲的波形

: 聲音的處理 混合



<br/><br/><br/>

----------------------------


##  📘 灰階圖與2維陣列

***灰階圖生成***

----------------------------



<br/><br/><br/> 

----------------------------

***照片數位處理*** 

----------------------------

<br/><br/><br/>


----------------------------

##  📙 彩色影像與3維陣列

***彩圖通道分離***

----------------------------


<br/><br/><br/>

----------------------------

***視訊拼接*** 

----------------------------

<br/><br/><br/>