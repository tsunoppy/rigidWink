# Calculation for the winkler rigid plate model
# Coded by tsunoppy on Sunday

import math
import openpyxl
from openpyxl.utils import get_column_letter # 列幅の指定 2020/05/27

import numpy as np
import matplotlib.pyplot as plt

# File Control
import os

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
        self.gmax = 0. # graph area
        self.gmin = 0. # graph area
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
            """
            # Model save
            plt.axes().spines['right'].set_visible(False)
            plt.axes().spines['top'].set_visible(False)
            plt.axes().set_aspect('equal')
            plt.scatter(self.x,self.y, s=1,color="black")
            plt.scatter(self.xg,self.yg, color="red")
            fig.savefig("./db/model.png", format="png", dpi=300)
            plt.close(fig)
            """

            return 1
        except Exception as err:
            print(err)
            return 0

    ########################################################################
    # View Model
    def viewModel(self):
        # Spring Position View

        xmax = max(self.x)
        xmin = min(self.x)
        ymax = max(self.y)
        ymin = min(self.y)
        self.gmax = max(xmax,ymax)
        self.gmin = min(xmin,ymin)
        """
        plt.xlim(gmin-2,gmax+2)
        plt.ylim(gmin-2,gmax+2)
        """
        fig = plt.figure()
        plt.axes().spines['right'].set_visible(False)
        plt.axes().spines['top'].set_visible(False)
        plt.axes().set_aspect('equal')
        """
        plt.scatter(self.x,self.y,label="Spring Position", s=1,color="black")
        plt.scatter(self.xg,self.yg, label="Gravity Center", color="red")
        plt.legend()
        """
        plt.scatter(self.x,self.y,s=1,color="black")
        plt.scatter(self.xg,self.yg, color="red")
        plt.show()
        plt.close(fig)

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
        tmpag = 0.
        tmpxg = 0.
        tmpyg = 0.

        suma = 0.
        sumxg = 0.
        sumyg = 0.

        for i in range(0,len(xx1)):
            tmpag = (xx2[i]-xx1[i])*(yy2[i]-yy1[i])
            tmpxg = (xx2[i]+xx1[i])/2.0
            tmpyg = (yy2[i]+yy1[i])/2.0
            suma = suma + tmpag
            sumxg = sumxg + tmpxg*tmpag
            sumyg = sumyg + tmpyg*tmpag

        self.xg = float(sumxg)/float(suma)
        self.yg = float(sumyg)/float(suma)
        self.ag = float(suma)

        # Check Result
        print("g = ", self.xg,self.yg, "a=",self.ag)

        # Save Model Input
        savefile = "./db/input.txt"
        lines = "## Center of Gravity\n"
        lines += " "
        lines += "gx = {:.2f} m".format(self.xg)+", "
        lines += "gy = {:.2f} m".format(self.yg)+", "
        lines += "A = {:.2f} m2".format(self.yg)+"\n"
        self.out_add(savefile,lines)

    ########################################################################
    # write output text file
    def out(self,outFile,lines):
        fout = open(outFile, "w")
        fout.writelines(lines)
        fout.close()

    # add output text file
    def out_add(self,outFile,lines):
        fout = open(outFile, "a")
        fout.writelines(lines)
        fout.close()

    ########################################################################
    # Solve Matrix analysis
    def solve(self,title,index,nn,mmx,mmy):
        details = "### Analysis detail ----------- \n"
        details += "# Start Solve------\n"
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
            details += "Cal_" + str(ii+1) + "\n"
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
                details += "break\n---"
                break

        # Cal for output
        # Total Area
        # 接地圧, kN/m2
        sig = spforce // np.array(self.sd)
        sigmax = 0.0
        sigmin = 100000.0
        for i in range(0,len(sig)):
            if sigmax < sig[i]:
                sigmax = sig[i]
                sigmaxId = i
            if sigmin > sig[i]:
                sigmin = sig[i]
                sigminId = i
        # 接地率
        sbar = 0.0
        upliftx = []
        uplifty = []
        for i in range(0,len(spforce)):
            if kdtmp[i] !=  0.0:
                sbar = sbar + self.sd[i]
            else:
                upliftx.append(self.x[i])
                uplifty.append(self.y[i])
        eta = sbar/self.ag*100.0

        # Checkoutput
        ####################
        """
        print("*** Analysis detail -----------")
        print("K = A*K*AT = \n",kkk)
        print("K^-1= \n",kkkinv)
        print("f = [Mx, My, Nz] = \n",force)
        print("d = [tx, ty, dz] = \n",disp)
        print("d' = \n", disp2)
        print("f' = \n", spforce)
        print("sig = \n", sig)
        print("sigMax = \n", sigmax)
        print("sigMin = \n", sigmin)
        print("eta = \n", eta)
        """

        # Details
        ####################

        details += "K = A*K*AT = \n"
        details += str(kkk) + "\n"
        details += "K^-1= \n"
        details += str(kkkinv) + "\n"
        details += "f = [Mx, My, Nz] = \n"
        details += str(force) + "\n"
        details += "d = [tx, ty, dz] = \n"
        details += str(disp) + "\n"
        details += "d' = \n"
        details += str(disp2) + "\n"
        details += "f' = \n"
        details += str(spforce) + "\n"
        details += "sig = \n"
        details += str(sig) + "\n"
        details += "sigMax = "
        details += str(sigmax) + "\n"
        details += "sigMin = "
        details += str(sigmin) + "\n"
        details += "eta ="
        details += str(eta) + "\n"

        lines = "\n"
        lines += "# Case: " + str(title) + "\n"
        lines += "\n"
        lines += "# Load:\n"
        lines += "   N  = "
        lines += "{:.0f} kN\n".format(force[2])
        lines += "   Mx = "
        lines += "{:.0f} kN.m\n".format(force[0])
        lines += "   My = "
        lines += "{:.0f} kN.m\n".format(force[1])

        lines += "\n"
        lines += "# Disp.:\n"
        lines += "   dz  = "
        lines += "{:.0f} mm\n".format(disp[2]*1000)
        lines += "   tx = "
        lines += "1/{:.0f} rad\n".format(1.0/disp[0])
        lines += "   ty = "
        lines += "1/{:.0f} rad\n".format(1.0/disp[1])

        lines += "\n"
        lines += "# Max.:\n"
        lines += "   Vertial Disp. : "
        lines += " {:.0f} mm\n".format(np.max(disp2)*1000)
        lines += "   Max. Pressure : "
        lines += " {:.0f} kN/m2\n".format(sigmax)
        lines += "   Min. Pressure : "
        lines += " {:.0f} kN/m2\n".format(sigmin)
        lines += "   Max. Angle : "
        maxtheta = 1.0/(math.sqrt(disp[0]**2+disp[1]**2))
        lines += " {:.0f} rad\n".format(maxtheta)
        lines += "   Contact Ratio : "
        lines += " {:.0f} %\n".format(eta)


        xx = np.array(self.x)
        yy = np.array(self.y).T


        ########################################################################
        # Interactive Glaph
        """
        plt.axes().set_aspect('equal')
        plt.scatter(xx,yy,c=sig,cmap='Reds', vmin=0.0)
        plt.colorbar()
        plt.show()
        """

        # Uplift Spring plot
        fig = plt.figure()
        plt.axes().spines['right'].set_visible(False)
        plt.axes().spines['top'].set_visible(False)
        plt.axes().set_aspect('equal')
        plt.scatter(self.x,self.y, s=1,color="black")
        plt.scatter(self.xg,self.yg, color="red")
        if len(upliftx) != 0:
            plt.scatter(upliftx,uplifty,s=1,color="blue")
        savefile = "./db/uplift_"+str(index)+".png"
        fig.savefig(savefile, format="png", dpi=300)
        plt.close(fig)

        # Stress plot
        fig = plt.figure()

        plt.axes().spines['right'].set_visible(False)
        plt.axes().spines['top'].set_visible(False)
        plt.axes().set_aspect('equal')
        plt.scatter(xx,yy,c=sig,cmap='Reds',vmin=0.0)
        savefile = "./db/result_"+str(index)+".png"
        fig.savefig( savefile, format="png", dpi=300)
        plt.close(fig)

        # save result text
        savefile = "./db/result_"+str(index)+".txt"
        self.out(savefile,lines)
        savefile = "./db/detail_"+str(index)+".txt"
        self.out(savefile,details)



########################################################################
# End Class

"""
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
"""
