#coding=utf-8
#from http://blog.csdn.net/xiaosebi1111/article/details/48653675
import numpy as np
#解决pycharm报错方法 https://www.linuxidc.com/Linux/2018-03/151117.htm
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib.ticker import MultipleLocator, FuncFormatter
#http://blog.csdn.net/luminganan/article/details/51322234 安装方法
import matplotlib.pyplot as pl
class LHSample:
    '拉丁超立方算法类'
    D = 0
    bounds = [[0,1],[0,1]]
    N = 0
    '''
    :param D:参数个数
    :param bounds:参数对应范围（list）
    :param N:拉丁超立方层数
    :return:样本数据
    '''
    def __init__(self,D,bounds,N):

        self.D = D
        self.bounds = bounds
        self.N = N

    def getSample(self):
        result = np.empty([N, D])
        temp = np.empty([N])
        d = 1.0 / N

        for i in range(D):

            for j in range(N):
                temp[j] = np.random.uniform(
                    low=j * d, high=(j + 1) * d, size = 1)[0]

            np.random.shuffle(temp)

            for j in range(N):
                result[j, i] = temp[j]

        #对样本数据进行拉伸
        b = np.array(bounds)
        lower_bounds = b[:,0]
        upper_bounds = b[:,1]
        if np.any(lower_bounds > upper_bounds):
            print '范围出错'
            return None

        #   sample * (upper_bound - lower_bound) + lower_bound
        np.add(np.multiply(result,
                           (upper_bounds - lower_bounds),
                           out=result),
               lower_bounds,
               out=result)
        return result

if __name__ =='__main__':
    D = 2
    N = 30
    bounds = [[0,90],[0,90]]
    xs = (bounds[0][1] - bounds[0][0])/N
    ys = (bounds[1][1] - bounds[1][0])/N
    ax = pl.gca()
    pl.ylim(bounds[1][0] - ys,bounds[1][1]+ys)
    pl.xlim(bounds[0][0] - xs, bounds[0][1] + xs)
    pl.grid()
    ax.xaxis.set_major_locator( MultipleLocator(xs) )
    ax.yaxis.set_major_locator(MultipleLocator(ys))
    lhs = LHSample(D,bounds,N)
    samples = lhs.getSample()
    XY = np.array(samples)
    X = XY[:,0]
    Y = XY[:,1]
    pl.scatter(X,Y)
    pl.show()