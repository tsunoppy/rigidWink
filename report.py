# -*- coding:utf-8 -*-
import os, sys
#import Image
#import urllib2
#from cStringIO import StringIO


#zipアーカイブからファイルを読み込むため。通常は必要ないはず。
#sys.path.insert(0, 'reportlab.zip')

import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm

class Report():

    def __init__(self):
        self.FONT_NAME = "Helvetica"

    ########################################################################
    # 文字と画像を配置
    def create_row(self,c, index, data, imagefile):
        y_shift = -240 * index
        c.setFont(self.FONT_NAME, 9)
        for i in range(1,len(data)):
            # txt
            c.drawString(55, 720-(i-1)*10 + y_shift, data[i])
            # png
            c.drawImage(imagefile, 300,  y_shift + 40, width=8*cm , preserveAspectRatio=True)

    ########################################################################
    # pdfの作成
    def print_page(self, c, inputf, index, imagefile, nCase):


        #タイトル描画
        c.setFont(self.FONT_NAME, 20)
        c.drawString(50, 795, u"Uplift Analysis")

        #グリッドヘッダー設定
        xlist = [40, 250, 560]
        ylist = [760, 780]
        c.grid(xlist, ylist)

        #sub title
        c.setFont(self.FONT_NAME, 12)
        c.drawString(55, 765, u"Case")
        c.drawString(270, 765, u"Pressure")

        #データを描画
        ########################################################################
        #for i, data in range(0,int(nCase)):
        for i in range(0,nCase):
            f = open(inputf[index+i],'r')
            tmpData = []
            while True:
                line = f.readline()
                if line:
                    if line != '\n':
                        tmpData.append(line.replace('\n',''))
                    else:
                        tmpData.append('')
                else:
                    break
            f.close()
            data = tmpData
            self.create_row( c, i, data, imagefile[index+i])

        #最後にグリッドを更新
        ylist = [40,  280,  520,  760]
        c.grid(xlist, ylist[3 - nCase:])
        #ページを確定
        c.showPage()

    ########################################################################
    # pdfの作成
    def print_head(self, c , title):

        #title = 'Sample Project'

        #タイトル描画
        c.setFont(self.FONT_NAME, 20)
        c.drawString(50, 795, title)

        #sub title
        c.setFont(self.FONT_NAME, 12)

        #データを描画
        ########################################################################
        inputf = './db/input.txt'
        f = open(inputf,'r')
        tmpData = []
        while True:
            line = f.readline()
            if line:
                if line != '\n':
                    tmpData.append(line.replace('\n',''))
                else:
                    tmpData.append('')
            else:
                break
        f.close()
        data = tmpData
        #c.setFont(self.FONT_NAME, 9)
        for i in range(0,len(data)):
            # txt
            c.drawString(55, 720-(i-1)*14, data[i])
        """
        # Model Diagram
        imagefile = './db/model.png'
        c.drawImage(imagefile, 60,  -300, width=18*cm , preserveAspectRatio=True)
        """
        #ページを確定
        c.showPage()
    ########################################################################
    # whole control
    def create_pdf(self, inputf, imagefile, pdfFile, title):

        # Parameter -------
        # inputf   : path to text file
        # imagefile: path to png file
        # pdfFile  : name of making pdf file

        #フォントファイルを指定して、フォントを登録
        #folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
        #pdfmetrics.registerFont(TTFont(FONT_NAME, os.path.join(folder, 'ipag.ttf')))
        #出力するPDFファイル
        c = canvas.Canvas(pdfFile)

        # ページ数
        ########################################################################
        dataNum = len(inputf)
        numPage = dataNum // 3
        numMod = dataNum % 3
        #print(numPage,numMod)
        if numMod >= 1:
            numPage = numPage + 1

        # pdfの作成
        ########################################################################
        self.print_head( c , title)

        for i in range(0,numPage):
            index = 3*i # index: 参照データのインデックス
            if numPage == 1:
                self.print_page( c, inputf, index, imagefile, dataNum)
            elif i != numPage-1 and numPage != 1:
                self.print_page( c, inputf, index, imagefile, 3)
            else:
                if numMod != 0:
                    self.print_page( c, inputf, index, imagefile, numMod)
                else:
                    self.print_page( c, inputf, index, imagefile, 3 )

        #pdfファイル生成
        ########################################################################
        c.save()
        print ("repot.py is Okay!!.")

########################################################################
# END CLASS


########################################################################
# test script
"""
pdfFile = "test.pdf"
obj = Report()
# テキストの読み込み
########################################################################
inputf = []
inputf.append("../db/result_0.txt")
inputf.append("../db/result_1.txt")
inputf.append("../db/result_2.txt")
inputf.append("../db/result_1.txt")
inputf.append("../db/result_2.txt")
print(inputf)

imagefile = []
imagefile.append("../db/result_0.png")
imagefile.append("../db/result_1.png")
imagefile.append("../db/result_2.png")
imagefile.append("../db/result_1.png")
imagefile.append("../db/result_2.png")

obj.create_pdf(inputf,imagefile,pdfFile)
"""
