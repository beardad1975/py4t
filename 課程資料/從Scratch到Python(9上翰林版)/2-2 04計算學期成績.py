score1 = int(input('請輸入作業成績:'))
score2 = int(input('請輸入測驗成績:'))
score3 = int(input('請輸入平時成績:'))
grade = score1 * 0.4 + score2 * 0.4 + score3 * 0.2
print('學期成績是' + str(grade))
if grade  <  60 :
    print('不及格')
else :
    print('及格')