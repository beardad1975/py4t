# 🔰 語音範例 - 文字轉語音

### 🎦 範例影片

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/585639930?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479&amp;h=f0168e5f2d" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="text to speech"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>



--------------

### 🏷️ 原理說明

只有把字串當成語音合成的函式，就可以讓電腦發出語音(使用windows文字轉語音功能)，再利用for迴圈與字串的格式化替換功能，就能做出簡單的銀行或醫院語音叫號效果。

<sup><sub>💬電腦上要有喇叭與麥克風。</sub></sup>

--------------

### 📄 Py4t程式碼

```python
rom 語音模組 import *

設定語音速度(2)

for 數 in range(5) :
    文字 = '來賓{}號請到{}號櫃台辦理'.format(數+50, 數)
    語音合成(文字)
```




