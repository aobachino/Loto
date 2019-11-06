import numbers1
import L2digit


print('前回の当選番号を入力してください')
preNumebr = str(input('>> '))
print('本日の曜日を入力してください')
print('月:Mon 火:Tue 水:Wed 木:Thu 金:Fri')
this_week = str(input('>> '))

resopnse1 = numbers1.PullNumber(preNumebr,this_week)
response2 = L2digit.PullNumber2(this_week)
#L2digit.PullNumber2(this_week)


print("前回の当選番号から曜日出現傾向の引き抜きと")
print("曜日出現傾向の割合から確率で出した番号は以下です")
print("※上位2桁が前回の当選番号/下位2桁が出現傾向割合の確率")

for i in resopnse1:
    print("当選予想番号 : {0}{1}".format(i,response2))
