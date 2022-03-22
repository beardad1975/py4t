from random import randint
n = 30
box = []
for i in range(1, n + 1) :
    position = randint(0, i-1)
    box.insert(position, i)
print(box)
print('第一特獎:' + str(box[0]))
print('第二特獎:' + str(box[1]))
print('第三特獎:' + str(box[2]))