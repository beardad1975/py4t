---
hide:
  - navigation
---

# 🏀 物理 教學函式庫

---------------

### 📗 說明

---------------

這個教學函式庫是建立在[pymunk](http://www.pymunk.org/en/latest/)的2D物理引擎上，並利用[arcade](https://api.arcade.academy/en/latest/)函式庫繪圖。可以建立基本形狀(圓形、方形)，控制物體的基本物理量(質量、摩擦力等)，改變環境的重力。

在其中所運用到的，其實就是憤怒鳥類型遊戲的模擬原理。稍加運用就可以改變2D物體的彈性、摩擦，並以互動事件的方式，操控重力，做出有趣的物理模擬。

為讓學習過程順暢，在函式庫中也設計了座標與地形的輔助功能，如下說明：

![地形輔助](terrain_assist.jpg){width=700}

<br/>

??? info "pymunk的官方說明"

     :fontawesome-solid-link: <a href="http://www.pymunk.org/en/latest/overview.html" target="_blank">pymunk overview</a>

??? info "arcade的官方說明"

     :fontawesome-solid-link: <a href="https://api.arcade.academy/en/latest/get_started.html" target="_blank">Arcade Get Started Here</a>


<br/><br/>


---------------

### 📕 基本用法

---------------

```python
from 物理模組 import * 

# 舞台設置或初始設置(一次)

# 事件處理函式
### 如「按下滑鼠時」函式
### 當事件發生時即會執行

模擬主迴圈()
```

在開頭匯入「物理模組」，最後加上「模擬主迴圈」函式，中間程式可以做舞台設置或初始設置(一次)，也可以加入「事件處理函式」，來決定相關事件發生時，要做的動作。

<br/><br/>

---------------

### 📕 便利貼

---------------

使用便利貼，拖曳後就會貼上程式碼，降低文字程式的學習難度。



| 便利貼顯示           | 便利貼內容                               |
| :-----------:                    | :-------------------------:          |
| ![顯示](pie4t_display_postit.jpg)    | ![便利貼](pie4t_postit.jpg)    |


<br/><br/>


---------------

### 📘 範例程式

---------------

各種以物理教學函式庫做出的程式範例。

| 範例                             | 截圖                                                              |
| :-----------:                    | :------------------------------------:                            |
| [無摩擦力](frictionless.md)          | [![無摩擦力](frictionless.jpg){width=150}](frictionless.md)           |
| [操控重力](gravity.md)          | [![操控重力](gravity.jpg){width=150}](gravity.md)           |
| [球的彈性](bounce_ball.md)          | [![球的彈性](bounce_ball.jpg){width=150}](bounce_ball.md)           |
| [噴射拋體](projectile.md)          | [![噴射拋體](projectile.jpg){width=150}](projectile.md)           |
| [彈性排列](bounce_array.md)          | [![彈性排列](bounce_array.jpg){width=150}](bounce_array.md)           |
| [力與斜面](force_and_slide.md)          | [![力與斜面](force_and_slide.jpg){width=150}](force_and_slide.md)           |
| [重力控制](inertia_gravity.md)          | [![重力控制](inertia_gravity.jpg){width=150}](inertia_gravity.md)           |
| [物理撞擊實驗室](collision_lab.md)          | [![物理撞擊實驗室](collision_lab.jpg){width=150}](collision_lab.md)           |


<br/><br/>


---------------

### 📒 入門課程

---------------

: ![力與運動遊樂場](../lesson/mechanics_playground/digest.jpg)

學習物理程式，做出彈性、斜面、拋體與重力等模擬程式。
:fontawesome-solid-long-arrow-alt-right: <a href="../lesson/mechanics_playground/" target="_blank">「力與運動遊樂場」</a>

<br/><br/>

---------------

### 📕 專題課程

---------------

: ![物理撞擊實驗室](../lesson/project_collision_lab/digest.jpg)

利用撞擊物與障礙物，進行撞擊的測試，找出影響撞擊的因素。
:fontawesome-solid-long-arrow-alt-right: <a href="../lesson/project_collision_lab/" target="_blank">「物理撞擊實驗室」</a>


<br/><br/>




---------------

### 📙 原始碼與套件

---------------

物理 教學函式庫 在:fontawesome-brands-github:github上的原始碼: [pie4t](https://github.com/beardad1975/pie4t)

物理 教學函式庫 在PyPI上發布的套件: [pie4t](https://pypi.org/project/pie4t/)，可使用pip install pie4t安裝

<br/><br/>



