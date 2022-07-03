# 👨‍👩‍👧‍👦 [問答] Py4t網站製作

Grace Li老師在fb社團詢問，Py4t網站是如何製作的？

Py4t的網頁及課程使用了開放原始碼且用python開發的Material for MkDocs套件，以下QA形式呈現Py4t網站設計的細節。

<br/>

----------------------------------

## ❓ 什麼是Material for MkDocs

Material for MkDocs是一種靜態網站產生器(Static Site Generator)，利用Markdown及python程式就可以快速產生網站，不需要使用HTML, CSS 或 JavaScript。是程式設計師設計簡易網站的好用工具。


Material for MkDocs的特色：

* It's just Markdown (可以僅使用簡單的Markdown語法)

* Works on all devices (響應式網頁適合各種裝置)

* Made to measure (有不同的網頁主題，設定簡單)

* Fast and lightweight (製作快速不複雜)

* Open Source (開放原始碼，於github上開發)


Material for MkDocs官網(使用方式請參考document)：

[https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)

<br/>

--------------------------------------------

## ❓ 為什麼要使用Material for MkDocs

網站可以從基礎的HTML, CSS 或 JavaScript開始從頭設計，並搭配程式及資料庫建立互動式網頁。這樣的網站功能豐富，可以客製化許多細節，做出的網頁效果做好，但是需要許多的人力、技術，時間，甚至是金錢。

另外，網站也可以使用Word Press或Google 協作平台…等簡易且免費使用的網路服務，這種方式適合不熟悉HTML的使用者。但是會有限制，比如能客製化的項目不多，無法簡單下載整個網站。且如果使用平台的服務有調整(如改為收費、廣告、網站服務政策改變等)，只能接受，不然會有搬移的代價。

靜態網站產生器的優缺點會介於前兩種之間，簡易製作，可客製作的內容多(也可以使用HTML、CSS客製化)，也不受限於某一網站。這種方式有彈性，但需要有一些程式的概念與技術。

Py4t是一個免費開源的推廣計畫，社群成員的討論利用fb社團服務，Py4t影片也使用youtube服務，所以剩下的只有資訊與課程的需求，使用靜態的HTML網頁即可達到目的。採用Material for MkDocs會比從頭寫HTML容易，以目前開發人力不多的情形下，是可行的方案。採用以python撰寫的第三方套件，對python程式語言的推廣也有正面的示範意義。

<br/>

-------------------------------------

## ❓ 什麼是Markdown 

因為網頁原本是需要寫HTML，但是HTML還是有一點複雜度，所以就有人發展出易讀易寫的純文字格式，最後再轉換產生成HTML，許多網站都可以直接使用Markdown。

* [Markdown - 維基百科，自由的百科全書](https://zh.wikipedia.org/zh-tw/Markdown)

* [Markdown 語法說明](https://markdown.tw/)



<br/>

----------------------------------------

## ❓ Py4t的網頁原始碼在哪裡 

Py4t的網頁目前是託管在github所提供的空間，在py4t程式碼空間(repository)下的docs資料夾中

* [Py4t的網頁原始碼(.md檔)](https://github.com/beardad1975/py4t/tree/master/docs)

每次更改網頁時，由網頁原始碼(markdown)產生的靜態html，則在site資料夾中

* [Py4t的靜態網頁(.html檔)](https://github.com/beardad1975/py4t/tree/master/site)




