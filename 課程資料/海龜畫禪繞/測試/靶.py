from 海龜模組 import *
import random as 隨機


def 靶() :
    for 數 in range(100, 0, -20) :
        畫點(數, 'red')
        畫點(數-10, 'pink')


for 數 in range(100) :
    向前(200)
    靶()
    右轉(360/6-5)
    


完成()
