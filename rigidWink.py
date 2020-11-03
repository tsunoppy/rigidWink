# Calculation for the winkler rigid plate model
# Coded by tsunoppy on Sunday

import math
import openpyxl
from openpyxl.utils import get_column_letter # 列幅の指定 2020/05/27

import numpy as np
import matplotlib.pyplot as plt

class Winkler:

    ########################################################################
    # Init
    def __init__(self):
        self.x = [] # Xdir. position (m)
        self.y = [] # Ydir. position (m)
        self.r = [] # Rotation, 1
        self.kd = [] # Local stiffness vector
        self.sd = [] # Local area vector
        self.ag = 0. # area
        self.xg = 0. # gravity center
        self.yg = 0. # gravity center
        self.error = "" # Error Message

    ########################################################################
    # Make Model
    def getModel(self,xx1,xx2,yy1,yy2,ndimx,ndimy,kb):
        # data.xlsx からデータを読み込む
        # 戻り値 0: 失敗, 1: 成功
        try:
            # xx1,xx2,yy1,yy2,kb,ndimx,ndimy
            # m,m,m,m,kN/m2/m,-,-
            for i in range(0,len(xx1)):
                self.creatMatrix(xx1[i],xx2[i],yy1[i],yy2[i],kb[i],ndimx[i],ndimy[i])
            return 1
        except Exception as err:
            print(err)
            return 0

    ########################################################################
    # View Model
    def viewModel(self):
        # Spring Position View
        plt.axes().set_aspect('equal')
        plt.scatter(self.x,self.y,s=1,color="black")
        plt.scatter(self.xg,self.yg,color="red")
        plt.show()

    ########################################################################
    # Make Model Matrix
    def creatMatrix(self,xx1,xx2,yy1,yy2,kb,ndimx,ndimy):
        delx = (xx2-xx1)/float(ndimx)
        dely = (yy2-yy1)/float(ndimy)
        # print(delx,dely)
        # Create spring position
        for j in range(0,ndimy+1):
            for i in range(0, ndimx+1):
                self.x.append(float(xx1+float(i)*delx))
                self.y.append(float(yy1+float(j)*dely))
                self.r.append(float(1))
        """
        # Check Data read
        k=1
        for j in range(0,ndimy+1):
        for i in range(0, ndimx+1):
        idx = i + (ndimx+1) * j
        #print(i,j,"ID=",idx,"Position[m]=",x[idx],y[idx])
        k = k+1
        print("xsize=", len(x), "ysize=",len(y))
        """
        # Create spring properties
        # local area
        sc = delx*dely/4
        ss = delx*dely/2
        st = delx*dely
        # local stiffness
        kc = kb*delx*dely/4
        ks = kb*delx*dely/2
        kt = kb*delx*dely
        for j in range(0,ndimy+1):
            for i in range(0,ndimx+1):
                # For Corner
                if i == 0 and j == 0 \
                   or i == ndimx and j == 0 \
                   or i == 0 and j == ndimy \
                   or i == ndimx and j == ndimy:
                    self.kd.append(kc)
                    self.sd.append(sc)
                    # For Side
                elif i == 0 and 1 <= j and j < ndimy \
                     or ( i == ndimx and 1 <= j and j < ndimy ) \
                     or ( 1 <= i and i < ndimx and j == 0) \
                     or ( 1 <= i and i < ndimx and j == ndimy):
                    self.kd.append(ks)
                    self.sd.append(ss)
                else:
                    self.kd.append(kt)
                    self.sd.append(st)
                # print(i,j,kd[i+j*ndimx])

    ########################################################################
    # Make Gravity center
    def getG(self,xx1,xx2,yy1,yy2):
        ag = 0.
        tmpxg = 0.
        tmpyg = 0.

        suma = 0.
        sumxg = 0.
        sumyg = 0.

        for i in range(0,len(xx1)):
            ag = (xx2[i]-xx1[i])*(yy2[i]-yy1[i])
            tmpxg = (xx2[i]+xx1[i])/2.0
            tmpyg = (yy2[i]+yy1[i])/2.0
            suma = suma + ag
            sumxg = sumxg + tmpxg*ag
            sumyg = sumyg + tmpyg*ag

        self.xg = float(sumxg)/float(suma)
        self.yg = float(sumyg)/float(suma)

        # Check Result
        print("g = ", self.xg,self.yg)

    ########################################################################
    # Solve Matrix analysis
    def solve(self,nn,mmx,mmy):
        print("Start Solve-------")
        force = np.array([mmx,mmy,nn])
        # 釣り合いマトリクス, A
        #print(self.x)
        vecXg = self.xg*np.array(self.r)
        vecYg = self.yg*np.array(self.r)
        a = np.array(self.x)-vecXg
        a = np.vstack((a,np.array(self.y)-vecYg))
        a = np.vstack((a,np.array(self.r)))
        # 転置行列 AT
        at = a.T
        # 対角行列の作成, Local 剛性マトリクス
        kdtmp = np.array(self.kd)
        #kk = np.diag(self.kd)
        #####
        # 収歛計算
        for ii in range(0,100):
            print("Cal_",ii+1)
            # 縮合マトリックス
            kk = np.diag(kdtmp)
            kkk = a @ kk @ at
            # 逆マト
            #kkkinv = kkk**-1
            kkkinv = np.linalg.inv(kkk)
            # Solve disp.
            disp = kkkinv @ force
            disp2 = at @ disp
            spforce = kk @ disp2
            # itelation
            ind = 0
            for i in range(0,len(spforce)):
                if spforce[i] < 0:
                    np.put(kdtmp,[i],0.0)
                    ind = 1
            if ind == 0:
                print("Break!-------")
                break
        #
        # output
        #print("A = ",a)
        sig = spforce // np.array(self.sd)
        print("*** Analysis detail -----------")
        print("K = A*K*AT = \n",kkk)
        print("K^-1= \n",kkkinv)
        print("f = [Mx, My, Nz] = \n",force)
        print("d = [tx, ty, dz] = \n",disp)
        print("d' = \n", disp2)
        print("f' = \n", spforce)
        print("sig = \n", sig)

        xx = np.array(self.x)
        yy = np.array(self.y).T
        plt.axes().set_aspect('equal')
        plt.scatter(xx,yy,c=sig,cmap='Reds', vmin=0.0)
#        plt.scatter(xx,yy,c=sig,cmap='Greys', vmin=0.0)
#        plt.scatter(xx,yy,c=sig,cmap='binary', vmin=0.0)
        plt.colorbar()
        plt.show()

########################################################################
# End Class

obj = Winkler()

# Force
nn  = 1400000.0 # Axial Force, kN
mmx = 0 # Over Turning Moment, kN.m
mmx = 15000000.0 # Over Turning Moment, kN.m
mmy = 15000000.0 # Over Turning Moment, kN.m
#mmy = 8000000.0 # Over Turning Moment, kN.m

xx1 = []
xx2 = []
yy1 = []
yy2 = []
ndimx = []
ndimy = []
kb = []

xx1.append(0.0)
xx2.append(100.0)
yy1.append(0.0)
yy2.append(30.0)
ndimx.append(100)
ndimy.append(30)
kb.append(50000.0)


xx1.append(0.0)
xx2.append(50.0)
yy1.append(30.0)
yy2.append(60.0)
ndimx.append(50)
ndimy.append(30)
kb.append(50000.0)

print("------------------------------")

if obj.getModel(xx1,xx2,yy1,yy2,ndimx,ndimy,kb):
    obj.getG(xx1,xx2,yy1,yy2)
    obj.viewModel()
    print("Complete Model Making")
else:
    del obj
    obj = Winkler()
    print("Fail Model Making")

obj.solve(nn,mmx,mmy)
print("------------------------------")
obj.solve(nn,0,0)
print("Complete")
