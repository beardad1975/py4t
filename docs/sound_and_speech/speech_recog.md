# 🔰 語音範例 - 語音辨識

### 🎦 範例影片

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/585669658?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479&amp;h=48c9d9d290" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="speech_poker"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


--------------

### 🏷️ 原理說明

利用google的語音辨識功能，來控制排序撲克的發牌動作，語音的指令有「發一張牌」以及「全部發完」

<sup><sub>💬電腦上要有喇叭與麥克風。語音辨識使用google需連網</sub></sup>

--------------

### 📄 Py4t程式碼

```python
from 語音模組 import *
from 演算法 import poker

poker.產生牌組(10)
語音辨識google()

while True:
    if 辨識成功了嗎():
        文字 = 取得辨識文字()
        if '發一張牌' in 文字:
            poker.發牌(單張=True)
        if '全部發完' in 文字:
            poker.發牌()
```




