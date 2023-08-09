# -*- coding: utf-8 -*-

import codecs
from imp import reload
import math
import time
import sys
import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.linear_model import SGDRegressor

import sys
reload(sys)
# sys.setdefaultencoding('utf-8')


# 将数据转化成为矩阵
def matrix(x):
    return np.matrix(np.array(x)).T


# 线性函数
def linerfunc(xList, thList, *intercept):
    res = 0.0
    for i in range(len(xList)):
        res += xList[i] * thList[i]
    if len(intercept) == 0:
        return res
    else:
        return res + intercept[0][0]


def linerfunc1(xList, theta1, theta2, theta3):

    s = linerfunc(xList,theta2)
    y2 = linerfunc(xList,theta3)
    xList = [1,s]
    y1 = linerfunc(xList, theta1)
    # for i in range(len(xList)):
    #     s += xList[i] ** i * theta2[i]
    #     y2 += xList[i] ** i * theta3[i]
    # for i in range(len(xList)):
    #     y1 += s ** i * theta1[i]
    res = y1 + y2
    # print 'bj'
    # print xList
    # print res
    return res

# 加载数据
def loadData(fileName,n):
    x = []
    y = []
    regex = re.compile('\s+')
    with open(fileName, 'r') as f:
        readlines = f.readlines()
        for line in readlines:
            dataLine = regex.split(line)
            dataList = [float(k) for k in dataLine[0:-1]]
            xList = dataList[0:2]
            for i in range(2,n+1):
                xList.append(dataList[1] ** i)
            x.append(xList)
            y.append(dataList[-1])
    return x, y


# 求解回归的参数
def normalEquation(xmat, ymat):
    temp = xmat.T.dot(xmat)
    isInverse = np.linalg.det(xmat.T.dot(xmat))
    if isInverse == 0.0:
        print('irreversible matrix')
        return None
    else:
        inv = temp.I
        return inv.dot(xmat.T).dot(ymat)


# 梯度下降求参数
def gradientDecent(xmat, ymat):
    sgd = SGDRegressor(max_iter=1000000, tol=1e-7)
    sgd.fit(xmat, ymat)
    return sgd.coef_, sgd.intercept_


# 测试代码

def testTrainResult(xTest, yTest, theta1, theta2, theta3, file):
    nright = 0
    sum = 0
    for i in range(len(xTest)):
        if ((int)(linerfunc1(xTest[i], theta1, theta2, theta3)) == (int)(yTest[i])):
            nright += 1
        # a = abs(linerfunc1(xTest[i], theta1, theta2, theta3) - yTest[i]) / yTest[i]
        # if(a < 0.5):
        #     sum += a
    print('The accuracy of the prediction method about normequation is {}'.format((float)(nright) / len(xTest)))

    nestimate = 0
    for i in range(len(xTest)):
        if (linerfunc1(xTest[i], theta1, theta2, theta3) * 1.5 >= yTest[i] >= linerfunc1(xTest[i], theta1, theta2, theta3) * 0.5):
            nestimate += 1

    file.write(str((float)(nright) / len(xTest)) + '\t' + str((float)(nestimate) / len(xTest)) + '\t')



def mean_squared_error(xTest,yTest, theta1, theta2, theta3):
    sum = 0
    for i in range(len(xTest)):
        sum += (linerfunc1(xTest[i], theta1, theta2, theta3) - yTest[i]) ** 2
    print ('The mean square error MSE is{}'.format(sum/len(xTest)))
    return sum/len(xTest)

def mean_absolute_error(xTest,yTest,theta1,theta2,theta3):
    sum = 0
    for i in range(len(xTest)):
        sum += math.fabs(linerfunc1(xTest[i], theta1, theta2, theta3) - yTest[i])
    print ('The mean absolute error MAE is {}'.format(sum/len(xTest)))
    return sum/len(xTest)

def root_mean_squared_error(xTest,yTest, theta1, theta2, theta3):
    """Calculate the RMSE between y_true and y_predict"""

    return math.sqrt(mean_squared_error(xTest,yTest, theta1, theta2, theta3))

def r2_score(xTest, yTest, theta1, theta2, theta3):
    sum = 0
    var = 0
    y = 0
    for i in range(len(yTest)):
        sum += (yTest[i] - linerfunc1(xTest[i], theta1, theta2, theta3)) ** 2
    for i in range(len(yTest)):
        y += yTest[i]
    y /= len(yTest)
    for i in range(len(yTest)):
        var += (yTest[i] - y) ** 2
    print ('The coefficient of determination r2 is {}'.format(1 - sum / var))
    return 1 - sum / var

# def r2_score(xTest,yTest,theta):
#     sum = 0
#     var = 0
#     y = 0
#     for i in range(len(xTest)):
#         sum += (yTest[i] - linerfunc(xTest[i], theta)) ** 2
#     for i in range(len(yTest)):
#         y += yTest[i]
#     y /= len(yTest)
#     for i in range(len(yTest)):
#         var += (yTest[i] - y) ** 2
#     print ('决定系数 MSE 为 {}'.format(1-sum/var))
# 可视化
def dataVisual(xmat, ymat, k, g, intercept,n,z):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    # plt.title('n=%i' %n)

    plt.scatter(xmat[:, 1].flatten().A[0], ymat[:, 0].flatten().A[0],s = 1,c = 'red')
    # x = np.linspace(0.005, 0.05, 100)
    x = np.linspace(0, 30000, 200)
    y = k[0]
    g = g[0] + intercept
    for i in range(1, n+1):
        y += x ** i * k[i]
    # plt.plot(x, g, c='green')
    plt.plot(x, y)
    plt.show()
    # filename = 'D:/codes/pycharm/ft/train2/Tsv-S/image/'+str(z)+'/p'+str(n)+'.png'
    # print  filename
    # plt.savefig(filename)
    # plt.close()
# 运行程序
def dataVisual1(xmat1, ymat1, theta1,xmat2, ymat2, theta2,xmat3, ymat3, theta3, n, z):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    # plt.title('n=%i' %n)
    plt.scatter(xmat2[:, 1].flatten().A[0], (ymat1[:, 0]+ymat3[:, 0]).flatten().A[0],s = 2,c = 'red')
    # print xmat2[:,1]
    # print (ymat1[:, 0]+ymat3[:, 0])
    # x = np.linspace(0.005, 0.05, 100)
    x = np.linspace(0.005, 0.05, 100)
    s = theta2[0]
    y1 = theta1[0]
    y2 = theta3[0]
    for i in range(1, n+1):
        s += x ** i * theta2[i]

        y2 += x ** i * theta3[i]
    for i in range(1, n+1):
        y1 += s ** i * theta1[i]
    y = y1+y2
    z1 = 0.5 * y
    z2 = 1.5 * y
    # print y1
    # print y2
    # print x
    # print y
    # plt.plot(x, g, c='green')
    # plt.plot(x, z1)
    plt.plot(x, y)
    # plt.plot(x, z2)
    # plt.show()
    current_path = sys.path[0]
    filename = str(current_path)+'/e-Tsve\\image\\' + str(z) + '/p' + str(n) + '.png'
    # filename = 'E:\\实验室项目\\接下来的项目\\train4\\train4\\e-Tsve\\image\\' + str(z) + '/p' + str(n) + '.png'
    print(filename)
    plt.savefig(filename)
    plt.close()
def main():
    current_path = sys.path[0]
    filename123=str(current_path)+'/e-Tsve/e-Tsvee-Tsve_2000.xls'
    list = codecs.open(filename=filename123, mode="w", encoding='utf-8')
    # list = codecs.open(r"/e-Tsve/e-Tsvee-Tsve_2000.xls", "w", encoding='utf-8')
    # list = codecs.open(r"E:\\实验室项目\\接下来的项目\\train4\\train4\\e-Tsvee-Tsve_2000_1.xls", "w", encoding='utf-8')
    # list = codecs.open(r"E:\\实验室项目\\接下来的项目\\RandomWalkTest2\\", "w", encoding='utf-8')
    list.write("Experiment number" + "\t" + "n times"  + "\t" + "Factor 1" + "\t"  + "Factor 2" + "\t"  + "Factor 3" + "\t" + "Correct rate" + "\t" + "Accurate rate within 5 percent error" + "\t" + "MSE" + "\t" + "RMSE" + "\t" + "MAE" + "\t" + "Square(R)" + "\t"  + "time consuming" + "\n")

    for i in range(1,27):
        re = []
        list.write(str(i))
        for n in range(1,10):
            starttime = time.time()
            filename1 = str(current_path)+'/S-Tsv/'+str(i)+'.xls'
            filename2 = str(current_path)+'/e-S/'+str(i)+'.xls'
            filename3 = str(current_path)+'/e-Te/' + str(i) + '.xls'
            # filename1 = 'train4/train4/S-Tsv/'+str(i)+'.xls'
            # filename2 = 'train4/train4/e-S/'+str(i)+'.xls'
            # filename3 = 'train4/train4/e-Te/' + str(i) + '.xls'
            print("这是第"+"%d"+"轮\n",n)
            x1, y1 = loadData(filename1,n)
            x2, y2 = loadData(filename2, n)
            x3, y3 = loadData(filename3, n)
            # 划分训练集合和测试集
            lr = 0.2
            xTrain1 = x1[:int(len(x1) * lr)]
            yTrain1 = y1[:int(len(y1) * lr)]
            xTrain2 = x2[:int(len(x2) * lr)]
            yTrain2 = y2[:int(len(y2) * lr)]
            xTrain3 = x3[:int(len(x3) * lr)]
            yTrain3 = y3[:int(len(y3) * lr)]

            yTest1 = y1[int(len(y1) * lr):]
            xTest2 = x2[int(len(x2) * lr):]
            xTest3 = x3[int(len(x3) * lr):]
            yTest3 = y3[int(len(y3) * lr):]

            yTest = yTest1
            for k in range(0, len(yTest1)):
                yTest[k] = yTest1[k] + yTest3[k]
                # print yTest[k]

            print (len(xTest2))
            print (len(yTest))
            xmat1 = matrix(xTrain1).T
            ymat1 = matrix(yTrain1)
            # 通过equation来计算模型的参数
            theta1 = normalEquation(xmat1, ymat1)
            print('Calculate the parameters of the model by equation')
            try:
                theta1 = theta1.reshape(1, len(theta1)).tolist()[0]
            except:
                continue
            print(theta1)

            xmat2 = matrix(xTrain2).T
            ymat2 = matrix(yTrain2)
            # 通过equation来计算模型的参数
            theta2 = normalEquation(xmat2, ymat2)
            print('Calculate the parameters of the model by equation')
            theta2 = theta2.reshape(1, len(theta2)).tolist()[0]
            print(theta2)

            xmat3 = matrix(xTrain3).T
            ymat3 = matrix(yTrain3)
            # 通过equation来计算模型的参数
            theta3 = normalEquation(xmat3, ymat3)
            print('Calculate the parameters of the model by equation')
            theta3 = theta3.reshape(1, len(theta3)).tolist()[0]
            print(theta3)
            nright = 0

            list.write('\t' + str(n) + '\t' + str(theta1) + '\t' + str(theta2) + '\t' + str(theta3) + '\t')
            for j in range(len(xTest2)):
                S = linerfunc(xTest2[j],theta2)
                xTest1 = [1,S]
                Tsv = linerfunc(xTest1,theta1)
                Te = linerfunc(xTest3[j],theta3)
                Tsve = Tsv + Te
                T = yTest1[j]+yTest3[j]
                if ((int)(Tsve) == (int)(T)):
                    nright += 1
            print('The accuracy of the fitting function {}'.format((float)(nright) / len(xTest2)))
            starttime1 = time.time()
            res = linerfunc1(xTest2[1],theta1,theta2,theta3)
            mse = mean_squared_error(xTest2, yTest, theta1, theta2, theta3)
            rmse = math.sqrt(mse)
            print ('The root mean square error RMSE is {}'.format(rmse))
            mae = mean_absolute_error(xTest2, yTest, theta1, theta2, theta3)
            r2 = r2_score(xTest2, yTest, theta1, theta2, theta3)
            endtime1 = time.time()
            dtime1 = endtime1 - starttime1
            # 掉包sklearn的梯度下降的算法求参数
            # print('掉包sklearn的梯度下降的算法求参数')
            # gtheta, Interc = gradientDecent(xTrain, yTrain)
            # print('参数')
            # print(gtheta)
            # print('截距')
            # print(Interc)
            testTrainResult(xTest2, yTest, theta1, theta2, theta3, list)
            dataVisual1(xmat1, ymat1, theta1,xmat2, ymat2, theta2,xmat3, ymat3, theta3, n, i)
            endtime = time.time()
            dtime = endtime - starttime
            list.write(str(mse) + '\t' + str(rmse) + '\t' + str(mae) + '\t' + str(r2) + "\t" + str(dtime) + "\t" + str(dtime1) + '\n')

        list.write('\n')

    list.close()
            # mean_squared_error(xTest, yTest, theta)

            # r2_score(xTest, yTest, theta)



if __name__ == "__main__":
    main()