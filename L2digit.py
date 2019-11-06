# coding utf-8
# Your code here!
import random
import pandas as pd
import xlrd
import os

def PullNumber2(week):
    this_week = str(week)
    num1 = 0 #3桁目
    num2 = 0 #4桁目
    float_pers = [] #パーセンテージ格納
    float_probs = [] #重みづけ格納

    # ランダム出力
    float_num1 = float(format(random.uniform(0,1) * 10,".3f"))
    float_num2 = float(format(random.uniform(0,1) * 10,".3f"))

    # ファイル読出し
    def  fileRead(this_week):

        frequent_list = []
        oPers = []  #リターン
        list_sum = 0

        # EXCELファイルを開きます。
        xl_bk = xlrd.open_workbook('numbers.xlsx')
        xl_sh = xl_bk.sheet_by_index(1)

        # 曜日から各数字の出現回数を取得します。
        week_number = 0
        for i in range(1,6):
            if(this_week == str(xl_sh.cell(i,0).value)):
                week_number = i

        # 頻出回数取得
        for i in range(1,11):
            frequent_list.append(int(xl_sh.cell(week_number,i).value))

        list_sum = sum(frequent_list)
        # パーセンテージ変換
        """
        for row in range(len(frequent_list)):
            oPers.append(float((float(frequent_list[row]) / float(list_sum)) * float(100)))
        """

        for row in frequent_list:
            oPers.append((float(row) / float(list_sum)) * 100)

        return oPers

    # 割合から重みを求める
    def  probab(iPers):

        oProbs = [] #リターン

        """
        for i in iPers:
            print(i)

        test = type(float(iPers[0]))
        print(test)
        """

        # 計算処理
        for i in range(10):
            if i == 0:
                oProbs.append(float(iPers[i]) / float(10))
            else:
                oProbs.append(float(oProbs[i-1]) + ((float(iPers[i]) / float(10))))
        return oProbs

    # 重みから下二桁を求める
    def  Loto(fnum,iProbs):

        oNum = 0 #リターン
        if fnum >= float(0) and fnum < float(iProbs[0]):
            oNum = 0
        elif fnum >= float(iProbs[0]) and fnum < float(iProbs[1]) :
            oNum = 1
        elif fnum >= float(iProbs[1]) and fnum < float(iProbs[2]) :
            oNum = 2
        elif fnum >= float(iProbs[2]) and fnum < float(iProbs[3]) :
            oNum = 3
        elif fnum >= float(iProbs[3]) and fnum < float(iProbs[4]) :
            oNum = 4
        elif fnum >= float(iProbs[4]) and fnum < float(iProbs[5]):
            oNum = 5
        elif fnum >= float(iProbs[5]) and fnum < float(iProbs[6]) :
            oNum = 6
        elif fnum >= float(iProbs[6]) and fnum < float(iProbs[7]) :
            oNum = 7
        elif fnum >= float(iProbs[7]) and fnum < float(iProbs[8]) :
            oNum = 8
        else:
            oNum == 9

        return int(oNum)

    float_pers = fileRead(this_week)
    probs = probab(float_pers)

    num1 = Loto(float_num1,probs)
    num2 = Loto(float_num2,probs)

    return str(num1) + str(num2)
