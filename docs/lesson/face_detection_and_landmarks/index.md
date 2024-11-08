---
hide:
  - navigation
---

# 📚 人臉偵測與臉部特徵


: 從下面的照片中，你看到了什麼？

: ![pareidolia_scene](pareidolia_scene.jpg)

: <sup>(資料來源:</sup>[^pareidolia_scene]<sup>)</sup>

[^pareidolia_scene]: 空想性錯視 維基百科, https://zh.wikipedia.org/zh-tw/%E7%A9%BA%E6%83%B3%E6%80%A7%E9%94%99%E8%A7%86

<br/>

: 是不是很直覺讓我們聯想到人臉呢？這種心理現象一般稱為空想性錯視(pareidolia)。


: 那什麼是空想性錯視呢？我們可以透過下方影片來瞭解：

: <iframe width="560" height="315" src="https://www.youtube.com/embed/l4fi-X5vZzI?start=30&amp;end=127" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(1分37秒, 資料來源:</sup>[^face_pareidolia]<sup>)</sup>

[^face_pareidolia]: 為何我們總是會看到臉孔?, by 皮毛小知識  , [youtube連結](https://youtu.be/l4fi-X5vZzI) 


: 空想性錯視是人類大腦與生俱來的功能，讓我們能認出人臉。你知道嗎？電腦在相關軟硬體的搭配下，也可以看出人臉呢！在這個課程中，讓我們一起來探索人臉偵測的資訊科技，及其相關應用。

??? info "關於視覺影像"

    : 本課程使用到整合後的教學函式庫，如下連結。

    : :fontawesome-solid-link: <a href="../../cv4t/" target="_blank">Py4t 視覺影像 說明、範例程式</a>

<br/>
<br/>
<br/> 

----------------------------

##  📙 電腦視界(1)

----------------------------


: 在此，我們要來了解，當電腦在觀看週遭環境時，到底看到了什麼？

: 首先，電腦以視訊攝影機做為眼睛，透過攝影機中的感光電子元件，將拍攝到的影像轉換成由0與1組成的數位訊號，後續可以讓它做各種運算處理並顯示在螢幕上。


<br/>

: ![computuer_vision_flow](computuer_vision_flow.png)


<br/>

: 由上圖中可以得知，影像在電腦的記憶體中，會以陣列的資料結構存放，那什麼是陣列呢？

: 陣列(Array)是一種**資料結構**，是由**相同資料類型**(整數、字串或浮點數等)元素所組成。

: 常見的陣列種類可分成1、2、3維陣列，讓大量資料的排列方式更多元，在生活中都有實際的應用情形。

: ![1維陣列](parking_1d.jpg)

: ![2維陣列](parking_2d.jpg)

: ![3維陣列](parking_3d.jpg)

: <sup>(資料來源:</sup>[^parking_array]<sup>)</sup>

[^parking_array]: 圖片來源：康軒教科書 國中二上科技領域資訊科技課本第52頁圖片

<br/>
<br/>

: 如果我們想要對影像做分析或處理，就必須要處理影像的3維陣列，利用索引的方式可以讓我們指定陣列的某一部分，在本課程中會使用numpy函式庫的多維陣列，其索引語法如下：


: ![3d_array_syntax](3d_array_syntax.png)

<br/>
<br/>
: 如果一次只能索引一個點的話，當我們想要一次存取一塊陣列，在程式撰寫時會變得更複雜。numpy函式庫提供切片(slicing)的語法，只要熟悉它，就可以讓我們很方便的索引到任何一塊想要的區域。

: ![3d_array_slice](3d_array_slice.png)

<br/>

: 甚至還有跳著選的陣列索引，如第0、2、4、…的方式(需指定步進值，類似等差數列的公差)。有了這些切片方法，是不是以更容易選到你想要的那一塊陣列了呢。


: ![3d_array_slice2](3d_array_slice2.png)

<br/>

接著讓我們來實作看看。




???+ example "範例程式 電腦視界 - - - - - - - (電腦視界 1/1 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/V2ei9Wurv6M?start=2&amp;end=382" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度6:20 章節時間如下】

        * 0:00 存檔、切換便利貼
        * 1:00 設置攝影機
        * 1:36 攝影機單張畫面
        * 2:15 觀察陣列
        * 3:43 攝影機連續畫面
        * 4:35 鏡像-左右翻轉
        * 5:06 修改攝影機畫面



    === "💻程式碼"

        ```python
        from 視覺模組 import *

        攝影機 = 設置影像擷取(後端='DSHOW')

        while True :
            陣列 = 擷取影像(攝影機)
            陣列 = 左右翻轉(陣列)
            
            顯示影像(陣列)
            
            print(陣列.shape)
            print(陣列[0:10, 0:10, 0])
            
            陣列[:, 200:400, :] = 0
            顯示影像(陣列, 視窗名稱='Image 2')
        ```


<br/>
<br/>


----------------------------

##  📗  看見人臉(1)

----------------------------

: 想要讓電腦認出人臉，我們可以透過人臉偵測器來達成。

: 一開始，先設置好人臉偵測器，之後將代表影像的3維陣列做為偵測器的輸入，從結果中，我們就可以得到人臉的資訊。


<br/>

: ![face_detection_flow](face_detection_flow.png)


<br/>

: 人臉偵測器感覺起來很像神秘的黑盒子，它的內部到底是什麼呢？

: 這個偵測器，其實是由全球AI科學家研究出來有關機器學習(Machine Learning)的成果之一，特別是這幾年快速發展的深度學習(Deep Learning)，由於這個主題相當的龐大與複雜，我們僅會透過下方的影片(手寫數字辨識)，做為對深度學習的基本認識。

<br/>

: <iframe width="560" height="315" src="https://www.youtube.com/embed/aircAruvnKk?start=0&amp;end=156" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(2分36秒,請自行開啟中文字幕,資料來源:</sup>[^multilayer_perceptron]<sup>)</sup>

[^multilayer_perceptron]: 究竟神經網路是什麼？ l 第一章 深度學習, By 3Blue1Brown  , [youtube連結](https://youtu.be/aircAruvnKk)


<br/>

: 下圖是人類神經元的圖示，AI科學家從人類的神經元及神經系統得到靈感，建構出以數學及電腦程式組成的人工神經網路。

: ![human_neuron](human_neuron.jpg)

: <sup>(資料來源:</sup>[^human_neuron]<sup>)</sup>

[^human_neuron]: 神經元 維基百科, https://zh.wikipedia.org/zh-tw/%E7%A5%9E%E7%B6%93%E5%85%83

<br/>

: 人臉偵測器，是由深度學習方式所訓練出來的人工神經網路。其最簡單的型式是多層感知器，由每一層中的神經元，互相關連，組成複雜的神經網路來做出如同人類能力的各項辨識。

<br/>

: ![mlp_reconize_digit](mlp_reconize_digit.jpg)


<br/>

: 接著讓我們來實作看看。

<br/>


???+ example "範例程式 看見人臉 - - - - - - - (看見人臉 1/1 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/TUb_CzM2PjI?start=2&amp;end=348" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度5:46 章節時間如下】

        * 0:00 存檔、切換便利貼
        * 0:41 設置攝影機、人臉偵測器
        * 1:22 擷取影像迴圈
        * 2:32 偵測、標示人臉
        * 4:10 標示信心值



    === "💻程式碼"

        ```python
        from 視覺模組 import *

        攝影機 = 設置影像擷取(後端='DSHOW')
        偵測器 = 設置FaceDetection()

        while True :
            陣列 = 擷取影像(攝影機)
            陣列 = 左右翻轉(陣列)
            顯示影像(陣列)
            
            結果 = 偵測器.process(陣列)
            if 結果:
                標記Face(陣列, 結果)
                臉 = 取出Face(結果)
                畫出文字(image=陣列,
                    text=str(臉.score),
                    pos=臉.bottom_left)        
                顯示影像(陣列, 視窗名稱='Image 2')
        ``` 




<br/>
<br/>



----------------------------

##  📘  臉部網格(2)


***更多臉部特徵***

----------------------------


: 在機器學習領域中，臉部特徵(face landmark)指的是臉部一組組容易尋找的點，眼睛、鼻子、嘴脣等。


: ![face_landmark_photos](face_landmark_photos.jpg)

: <sup>(資料來源:</sup>[^face_landmark_photos]<sup>)</sup>

[^face_landmark_photos]: Deep Recurrent Regression for Facial Landmark Detection, https://arxiv.org/pdf/1510.09083.pdf

<br/>

: 各個臉部特徵點會有給定的編號，本課程所使用的臉部網格位置及編號(468點，來自mediapipe)，詳見 [臉部特徵點編號圖](face_mesh.png)。

<br/>

: 有了臉部特徵點之後，將不同組的特徵點連結起來，可以得到臉部網格或是臉部輪廓等效果，看起來是不是很有趣啊。

: ![face_mesh_drawing](face_mesh_drawing.jpg)



<br/>

: 一起來動手實作。


???+ example "範例程式 更多臉部特徵 - - - - - - - (臉部網格 1/2 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/9pxUQugN83E?start=2&amp;end=340" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度5:38 章節時間如下】

        * 0:00 存檔、切換便利貼
        * 0:39 更多臉部特徵 
        * 0:50 設置攝影機、臉部網格偵測器
        * 1:35 擷取影像迴圈
        * 2:33 偵測臉部特徵點
        * 3:35 標示臉部網格、特徵點與輪廓

    === "💻程式碼"

        ```python
        from 視覺模組 import *

        攝影機 = 設置影像擷取(後端='DSHOW')
        偵測器 = 設置FaceMesh()

        while True :
            陣列 = 擷取影像(攝影機)
            陣列 = 左右翻轉(陣列)
            顯示影像(陣列)
            
            結果 = 偵測器.process(陣列)
            if 結果:
                陣列[:, :, :] = 0
                標記FaceMesh(陣列, 結果, 'FACE_LANDMARKS')
                標記FaceMesh(陣列, 結果, 'CONTOURS')
                    
                顯示影像(陣列, 視窗名稱='Image 2') 
        ``` 





<br/>
<br/>

----------------------------

***臉部動作***

----------------------------

: 霍金(Stephen William Hawking, 1942-2018)是世界知名的英國物理學家，他提出的黑洞理論，量子力學…等，在科學上有許多貢獻。他也曾出版過知名的科普書籍「時間簡史：從大爆炸到黑洞」。

: 霍金患有漸凍人症，從二十多歲開始，必須要使用枴杖與輪椅才能行走，病情也隨著時間逐漸惡化至嚴重。在這樣的環境下，他是如何撰寫研究論文與書本寫作的呢？讓我們一起來認識霍金的高科技輪椅。


<br/>


: <iframe width="560" height="315" src="https://www.youtube.com/embed/18HzCMecF4g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(3分08秒,資料來源:</sup>[^wheelchair_technology]<sup>)</sup>

[^wheelchair_technology]: 霍金的天价轮椅有何黑科技？眨眨眼就能说话，轮椅界的劳斯莱斯！, By 科普記  , [youtube連結](https://youtu.be/18HzCMecF4g)


<br/>

: 那我們是否可以將人臉偵測關鍵點的技術，用來幫助因行動不便，而無法使用現有輸入方式的人呢？

: 這是個值得嘗試的程式，讓我們可以進行無障礙的體驗活動。試試看用臉部動作來做出打字輸入的簡易程式，比如說，使用嘴脣上的2個關鍵點，並計算距離後，就可以偵測開口的動作。有了關鍵的偵測開口動作，未來就可以將程式擴展為具有文字輸入的功能。


<br/>

: ![mouth_opening_detection](mouth_opening_detection.jpg)

<br/>


: 一起來實作看看，偵測開口動作的程式。


???+ example "範例程式 臉部動作 - - - - - - - (臉部網格 2/2 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/9pxUQugN83E?start=343&amp;end=596" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度4:13 章節時間如下】

        * 5:43 臉部動作
        * 6:25 計算開口長度
        * 8:07 符合開口條件的動作

    === "💻程式碼"

        ```python
        from 視覺模組 import *

        攝影機 = 設置影像擷取(後端='DSHOW')
        偵測器 = 設置FaceMesh()
        數字 = 0

        while True :
            陣列 = 擷取影像(攝影機)
            陣列 = 左右翻轉(陣列)
            顯示影像(陣列)
            
            結果 = 偵測器.process(陣列)
            if 結果:
                陣列[:, :, :] = 0
                標記FaceMesh(陣列, 結果)
                特徵清單 = 取出Landmarks(結果)        
                
                開口長度 = abs(特徵清單[13][1] - 特徵清單[14][1])
                if 開口長度 > 10 :
                    標記FaceMesh(陣列, 結果, 'LIPS')
                    數字 += 1
                    print(數字)
                顯示影像(陣列, 視窗名稱='Image 2') 
        ``` 


??? info "進階範例 人臉輸入數字"

    : 人臉數字輸入，眨右眼增加數字，眨左眼減少數字，開口輸入數字

    : :fontawesome-solid-link: <a href="../../cv4t/face_input_number/" target="_blank">進階範例 人臉輸入數字</a>


<br/>
<br/>

----------------------------

##  📗  濾鏡貼紙(2)

***特徵點與png去背圖***

----------------------------

: 從臉部網格所取得的特徵點，多是以圖片座標xy來表達，但這個座標系統與我們在數學課所學的平面直角座標略有不同，簡單來說，是將第一象限做上下翻轉而來，每個座標值沒有負數，且均為整數。

<br/>

: ![image_coordinate](image_coordinate.png)

<br/>

: 臉部特徵點還可以有什麼應用呢？我們可以做出類似IG或是相機app的濾鏡貼紙效果，幫相機裡的人增加卡通裝飾(如貓耳朵或狗耳朵)。

: 想要達到這個功能，必須要能夠將一張圖，覆疊至另一張圖上。為了有更好的覆疊效果，我們需要認識alpha(阿爾法)通道。

: ![rgba_channels](rgba_channels.jpg)

: <sup>(資料來源:</sup>[^alpha_channel]<sup>)</sup>

<br/>

: 通常電腦圖片是以Red、Green、Blue三個通道。但有些圖片具有RGBA四個通道(如PNG圖檔)，A通道也稱為alpha通道，此通道代表的不是顏色，而是不透明度，如下圖所示，白色部份是不透明(值為255)，黑色的部份是透明(值為0)。

<br/>

: ![alpha_channel_effect](alpha_channel_effect.jpg)

: <sup>(資料來源:</sup>[^alpha_channel]<sup>)</sup>

[^alpha_channel]:Export with ALPHA Channel to make your video Transparent - Premiere Pro, by storysium, https://youtu.be/s3r5Ezzv3Rs

<br/>

從下面的影片中，可以看出alpha通道的效果，可以讓圖片的背景去除。

<br/>


: <iframe width="560" height="315" src="https://www.youtube.com/embed/s3r5Ezzv3Rs?start=9&amp;end=29" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(20秒,資料來源:</sup>[^alpha_channel]<sup>)</sup>


<br/>

: 接著，我們會使用png去背圖來覆疊到攝影機的視訊上，一起來實作看看。



???+ example "範例程式 特徵點與png去背圖 - - - - - - - (濾鏡貼紙 1/2 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/JVkRS2VDHJg?start=0&amp;end=506" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

        【長度 章節時間如下】

        * 0:00 存檔、切換便利貼
        * 0:51 攝影機程式
        * 2:24 png去背圖
        * 4:37 取得特徵點
        * 6:26 png貼至特徵點

    === "💻程式碼"

        ```python
        # 需匯入crown.png(視覺便利貼:png->匯入)

        from 視覺模組 import *

        攝影機 = 設置影像擷取(後端='DSHOW')
        png陣列 = 讀取png影像('crown.png')
        偵測器 = 設置FaceMesh()

        while True :
            陣列 = 擷取影像(攝影機)
            陣列 = 左右翻轉(陣列)
            顯示影像(陣列)
            
            結果 = 偵測器.process(陣列)
            if 結果:
                特徵清單 = 取出Landmarks(結果)
                貼上png中心點(陣列,png陣列,特徵清單[10])
                
                顯示影像(陣列, 視窗名稱='Image 2')  
        ```


<br/>
<br/>

----------------------------

***兩點轉換***

----------------------------

: 在上一個範例中，雖然有將裝飾的png圖貼上，但實際運行時，發現了一些問題，就是當自己的臉在不同的遠近及角度時，裝飾圖都不會改變，造成比例大小及角度的不一致，這要怎麼克服呢？

: 在這裡，我們會採用已經經過簡化後的兩點transform(轉換)來解決這個問題。首先，利用繪圖軟體來找出裝飾圖png上的來源點1及來源點2的座標。再來從 [臉部特徵點編號圖](face_mesh.png) 中找出目標點1及目標點2的編號，經由兩點transform，裝飾圖png就會適當的縮放與旋轉，產生位置吻合的轉換png陣列。

<br/>

: ![two_points_transformation](two_points_transformation.png)

??? info "關於兩點transform的原理與實作"

    : 兩點轉換的原理，需使用到平移、旋轉及放大的轉換矩陣。

    : :fontawesome-solid-link: <a href="https://en.wikipedia.org/wiki/Transformation_matrix#Other_kinds_of_transformations" target="_blank">transformation matrix</a>

    : 兩點轉換的原始碼，使用到numpy及opencv，來完成需要的矩陣運算

    : :fontawesome-solid-link: <a href="https://github.com/beardad1975/cv4t/blob/main/cv4t/draw_lib.py#L173" target="_blank">兩點轉換原始碼</a>


<br/>
<br/>

: 有了轉換後的裝飾圖png，再把它覆疊到原本的攝影機影像上，就可以做出如IG的濾鏡貼紙效果了。

: ![filter_sticker_effect](filter_sticker_effect.png)

<br/>


: 動手實作看看。

???+ example "範例程式 兩點轉換 - - - - - - - (濾鏡貼紙 2/2 接續)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/JVkRS2VDHJg?start=513&amp;end=704" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


        【長度 章節時間如下】

        * 8:33 兩點轉換

    === "💻程式碼"

        ```python
        # 需匯入crown.png(視覺便利貼:png->匯入)

        from 視覺模組 import *

        攝影機 = 設置影像擷取(後端='DSHOW')
        png陣列 = 讀取png影像('crown.png')
        偵測器 = 設置FaceMesh()

        while True :
            陣列 = 擷取影像(攝影機)
            陣列 = 左右翻轉(陣列)
            顯示影像(陣列)
            
            結果 = 偵測器.process(陣列)
            if 結果:
                特徵清單 = 取出Landmarks(結果)
                轉換png陣列 = 兩點transform(
                    來源影像=png陣列,
                    來源pt1=(100,150),
                    來源pt2=(150,150),
                    目標影像=陣列,
                    目標pt1=特徵清單[109],
                    目標pt2=特徵清單[338])
                貼上png(陣列,轉換png陣列)
                
                顯示影像(陣列, 視窗名稱='Image 2') 
        ```


??? info "進階範例 濾鏡貼紙(多種切換)"

    : 使用空白鍵切換不同的造型貼紙

    : :fontawesome-solid-link: <a href="../../cv4t/filter_sticker_switch/" target="_blank">進階範例 濾鏡貼紙(多種切換)</a>

<br/>
<br/>


----------------------------

##  📘  AR面具(1)

----------------------------


: AR（Augmented Reality），又稱為擴增實境，是指在螢幕的攝影機影像上，透過位置與角度的計算，讓螢幕上的虛擬物件能夠跟現實世界場景進行結合與互動的技術。


: <iframe width="560" height="315" src="https://www.youtube.com/embed/NEasf4Q0xDA?start=0&amp;end=55" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


: <sup>(55秒,資料來源:</sup>[^ar_mr_vr]<sup>)</sup>

[^ar_mr_vr]: 【AR、VR、MR 哪裡不一樣 ?】跨出虛擬走入現實：「AR擴增實境」, By 科技大觀園  , [youtube連結](https://youtu.be/NEasf4Q0xDA)


<br/>

: 由以上的影片得知，臉部濾鏡貼紙，是在人臉的攝影機影像上，加上數位裝飾圖片，因此也可視為是一種AR技術。

: 但是，我們發現，如果濾鏡的貼紙越來越大，就會越來越不合適臉型，因為兩點轉換是以一直線為基礎，並不是直接對應整個臉型。那我們有辦法將一個卡通面具，對應到人臉並貼合臉型嗎？

: 試著將兩點對應，擴展為多點對應。以下為面具圖檔做對應的特徵點，包含主要的臉部特徵，計有74點。




: ![mask_annotation](mask_annotation.jpg)



<br/>

接著將編號，特徵點，x、y座標等所需的對應資訊，存入檔案中(csv格式)，然後依據面具png圖檔及對應資訊檔案，來做已經簡化過的面具transform變換功能，就會達到AR面具的效果。


: ![csv_annotation](csv_annotation.jpg)


<br/>

??? info "關於面具transform的原理"


    : :fontawesome-solid-link: <a href="https://learnopencv.com/create-snapchat-instagram-filters-using-mediapipe/" target="_blank">面具transform的原理</a>

    : (AR面具的範例程式，是參考自此篇文--在learnopencv.com的教學文章及範例程式，並做適度簡化，讓學生進行實作學習。)



<br/>


: 一起來實作看看。


???+ example "範例程式 AR面具 - - - - - - - (AR面具 1/1 新檔)"

    === "🎦操作影片"
    
        <iframe width="560" height="315" src="https://www.youtube.com/embed/-rWygtI_UGo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


        【長度 章節時間如下】

        * 0:00 存檔、切換便利貼
        * 0:39 攝影機程式
        * 2:15 臉部偵測
        * 4:08 載入面具資料
        * 6:18 面具轉換

    === "💻程式碼"

        ```python
        # 需匯入white_mask.png(視覺便利貼:更多臉部特徵->匯入)
        # 需匯入white_mask.csv(視覺便利貼:更多臉部特徵->匯入)

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
                特徵清單 = 取出Landmarks(結果)
                轉換png陣列 = 面具transform(
                    來源影像=png陣列,
                    臉型對應=面具臉型,
                    目標影像=陣列,
                    偵測結果=結果)
                貼上png(陣列,轉換png陣列)
                
                顯示影像(陣列, 視窗名稱='Image 2')
        ```

??? info "進階範例 AR面具(多種切換)"

    : 每次重新偵測臉部時，即會切換

    : :fontawesome-solid-link: <a href="../../cv4t/ar_mask_switch/" target="_blank">進階範例 AR面具(多種切換)</a>

??? info "進階範例 如何自訂新的AR面具"

    : Py4t的範例面具有4種，如果你覺得不夠，想要自訂一個新的面具，或是想要了解多點對應的標記方式(許多機器學習的專案，其實都要花許多時間整理、標記資料)。你可以先準備好一個面具檔案，然後照著下方的教學影片做出，整個過程約需30分鐘，需要有耐心。

    : :fontawesome-solid-link: <a href="https://youtu.be/iT2aiqdHrBw" target="_blank">自訂新的AR面具</a>

    : :fontawesome-solid-link: <a href="https://drive.google.com/drive/folders/1kG-Cac7sME1ogDrylS79wG9MncjcXDDu?usp=drive_link" target="_blank">範例程式(大猩猩面具)</a>

    

    : (由Py4t社群的樂活老師提問而來)


<br/>
<br/>


----------------------------

##  📙 科技社會議題

*** 人臉辨識與未來商店 ***

----------------------------

: 利用人臉偵測，來產生臉部的特徵點，並計算如兩眼距離、鼻子到嘴巴的距離、顴骨形狀、嘴唇、耳朵和下巴的輪廓等，將這些臉部資料與個人個資儲存後，可以做為下次辨識人臉的依據，就好像把人臉當作指紋的身分確認，這種技術稱為人臉辨識。

: 在美國、中國大陸，有些商店、飯站開始實驗以人臉做為身份認証的付款方式。

<br/>

: <iframe width="560" height="315" src="https://www.youtube.com/embed/qbckDLoklZE?start=36&amp;end=185" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(2分29秒, 資料來源:</sup>[^face_recognition_issue]<sup>)</sup>

[^face_recognition_issue]: 【民視全球新聞】人臉辨識雙面刃 用之不當恐引社會危機, by 民視新聞網  , [youtube連結](https://youtu.be/qbckDLoklZE) 


<br/>
<br/>


----------------------------

*** 人臉辨識、執法監控與個人隱私 ***

----------------------------

: 如果政府把人臉辨識，當作法律執行的工具來監控人民時，對我們的個人隱私會產生什麼影響呢？


: <iframe width="560" height="315" src="https://www.youtube.com/embed/qbckDLoklZE?start=187&amp;end=451" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

: <sup>(4分24秒, 資料來源:</sup>[^face_recognition_issue]<sup>)</sup>


: 科技技術是一種工具，端看人類如何去運用，就好像水能載舟，亦能覆舟，我們必需小心地、負責任地使用這個技術。

: 另外，由於科技發展日新月異，在現今的時代，我們也要時時更新自己的知識，以順應未來世界。


<br/>
<br/>