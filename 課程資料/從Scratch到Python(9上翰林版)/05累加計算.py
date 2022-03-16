n = int(input('請輸入數字 n:'))
total = 0
for i in range(1, n + 1) :
    total = total + i
print('1+2+...+' + str(n) + '=' + str(total))