:orphan:

.. _影像格線:

視覺範例 影像格線 
================================

在每一張取影的攝影機影像中，先將影像轉成灰階，再利用多維陣列的切片功能，在直向與橫向兩個方向中，每隔50點就畫一條白線(顏色值255)，就做出了影像格線的效果。

註：電腦上需要有視訊攝影機

.. literalinclude:: camera_slice.py
    :caption: 影像格線的py4t程式碼
    :linenos:

執行結果

.. image:: camera_slice.jpg
    :width: 500px
    :align: center
    :alt: 範例程式截圖