password = '137'
times = 1
password2 = input('請輸入密碼:')
while password != password2 and times < 3 :
    print('密碼錯誤！')
    times = times + 1
    password2 = input('請輸入密碼:')
if password == password2 :
    print('歡迎使用本系統')
else :
    print('輸入密碼錯誤3次，帳號已被鎖定')