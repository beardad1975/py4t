:orphan:

.. _正多邊形:

海龜範例 正多邊形
================================

正多邊形的外角和都是360度，海龜在轉出一個角度的線條時，角度都是外角

.. image:: external_angle.jpg
    :width: 500px
    :align: center
    
  

利用這個外角的特性，我們先定義出正多邊形的函式(引數為長與邊)。

利用for迴圈重複10次，即可連續畫出3邊形到12邊形



.. literalinclude:: regular_polygon.py
    :caption: 畫出正多邊形的py4t程式碼
    :linenos:

執行結果

.. image:: regular_polygon.jpg
    :width: 500px
    :align: center
    :alt: 範例程式截圖



