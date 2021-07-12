:orphan:

.. _彩色方陣:

3D範例 彩色方陣 
================================

利用雙層for迴圈，沿著x軸與y軸方向，內層迴圈的次數會外層迴圈的索引改變，造成樓梯形狀的效果。

顏色的部份，將不同的索引值帶入到HSV的顏色設定，產生了彩色方陣

    

.. literalinclude:: color_array.py
    :caption: 彩色方陣的py4t程式碼
    :linenos:

執行結果

.. image:: color_array.jpg
    :width: 500px
    :align: center
    :alt: 範例程式截圖