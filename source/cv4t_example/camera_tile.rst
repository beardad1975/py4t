:orphan:

.. _電視牆:

視覺範例 電視牆 
================================

在每一張取影的攝影機影像中，先將影像轉成灰階，並把影像縮小(150)，再利用多維陣列的拼貼功能，在直向與橫向兩個方向中，各拼貼4次，就做出了如同電視牆的效果。

註：電腦上需要有視訊攝影機

.. literalinclude:: camera_tile.py
    :caption: 黑白電視牆的py4t程式碼
    :linenos:

執行結果(黑白)

.. image:: camera_tile.jpg
    :width: 500px
    :align: center
    :alt: 範例程式截圖

再來彩色電視牆的拼貼，拼貼時，在直向與橫向兩個方向中，各拼貼3次，但在第3維度(顏色)維特不變即可

.. literalinclude:: color_camera_tile.py
    :caption: 彩色電視牆的py4t程式碼
    :linenos:

執行結果(彩色)

.. image:: color_camera_tile.jpg
    :width: 500px
    :align: center
    :alt: 範例程式截圖