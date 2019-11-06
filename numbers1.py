# coding: utf-8
import pandas as pd
import csv
import os
import urllib.request
import xlrd
import collections

'''
print('前回の当選番号を入力してください')
preWinningNumber = str(input('>> ')) #'9047' でない'5682' 最大値以下が2つだぶった場合にうまく出力できない
print('本日の曜日を入力してください')
print('月:Mon 火:Tue 水:Wed 木:Thu 金:Fri')
this_week = str(input('>> ')) #  でない'Mon'
'''
def PullNumber(targetNumber,week):
    preWinningNumber = str(targetNumber)
    this_week = str(week)

    # 結果を格納する変数
    result = []

    # EXCELファイルを開きます。
    xl_bk = xlrd.open_workbook('numbers.xlsx')
    xl_sh = xl_bk.sheet_by_index(1)

    # 曜日から各数字の出現回数を取得します。
    week_number = 0
    for i in range(1,6):
        if(this_week == str(xl_sh.cell(i,0).value)):
            week_number = i

    appearanceTendency_list = []
    for i in range(1,11):
        appearanceTendency_list.append(int(xl_sh.cell(week_number,i).value))

    # 出現回数を表示します
    for i in range(10):
        print('直近50回の内{0}曜日の{1}の出現回数は{2}です'.format(this_week,i,appearanceTendency_list[i]))

    # 出現回数と数字を辞書型として定義します。
    number_dic ={}
    for i in range(0,10):
        number_dic.setdefault(int(i),int(appearanceTendency_list[i]))

    # 前回の当選番号から同一の数値を削除します。
    intList = []
    for i in range(0,4):
        strWork = int(preWinningNumber[i])
        if(strWork not in intList):
            intList.append(strWork)

    # 当選番号から同一の値が削除できたか確認してます。
    '''
    for i in intList:
        print(i)
    '''

    # 前回の当選番号のみを取得します
    winningNumber = {}
    for i in intList:
        winningNumber.setdefault(int(i),int(number_dic[i]))

    # 確認用
    #print(winningNumber)

    maxNum = int(max(winningNumber.values()))
    # 前回の当選番号から出現回数の最大値を取得します
    maxNumbers = {}
    for item_key,item_value in winningNumber.items():
        if(item_value == maxNum):
            maxNumbers.setdefault(item_key,item_value)

    maxNumCount = len(maxNumbers)
    #maxNumCount = list(winningNumber.values()).count(maxNum)
    #print(maxNumCount)

    #print(maxNumCount)
    if maxNumCount == 1:
        # 1桁が確定したので、残りの1桁を求めます
        # まず、確定した1桁を取得します
        num = 0
        for i in maxNumbers:
            num = i

        # 上記を削除して2番目に大きい値を取得します。
        del winningNumber[num]
        nextNum = int(max(winningNumber.values()))

        # 取得した2番目に大きい値を持つdicのみ取得します。
        nextNumbers = {}
        for item_key,item_value in winningNumber.items():
            if(item_value == nextNum):
                nextNumbers.setdefault(item_key,item_value)

        for item_key,item_value in nextNumbers.items():
            if len(nextNumbers) == 1:
                #print("前回の当選番号{0}で曜日ごとの出現傾向から".format(preWinningNumber))
                #print("{0}{1} が出現しやすい2桁です".format(num,item_key))
                result.append(str(num)+str(item_key))
                break
            elif len(nextNumbers) > 1:
                #print("前回の当選番号{0}で曜日ごとの出現傾向から".format(preWinningNumber))
                #print("出現しやすい2桁の組み合わせは以下です。")
                for i_key,i_value in nextNumbers.items():
                    #print("{0}{1}".format(num,i_key))
                    result.append(str(num)+str(i_key))
                break

    # 出現しやすい2桁がきまったので出力
    elif maxNumCount == 2:
        resultWork = str("")
        for i in maxNumbers.keys():
            resultWork += str(i)

        #確認用
        #print("前回の当選番号{0}で曜日ごとの出現傾向から".format(preWinningNumber))
        #print("出現しやすい2桁の組み合わせは {0} です".format(resultWork))
        result.append(resultWork)

    else:
        # 出現回数の高い数字を配列に確保
        numbers =[]
        for i in maxNumbers.keys():
            numbers.append(i)

        #確認用
        #print("前回の当選番号{0}で曜日ごとの出現傾向から".format(preWinningNumber))
        #print("出現しやすい2桁の組み合わせは以下です。")
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                #print("{0}{1}".format(numbers[i],numbers[j]))
                result.append(str(numbers[i])+str(numbers[j]))

    return result
