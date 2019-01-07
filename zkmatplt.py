# ------------------------------------------------------------
# Copyright (c) 2017-present, SeetaTech, Co.,Ltd.
#
# Licensed under the BSD 2-Clause License.
# You should have received a copy of the BSD 2-Clause License
# along with the software. If not, See,
#
#      <https://opensource.org/licenses/BSD-2-Clause>
#
# ------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换sans-serif字体支持中文
plt.rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题


def setting():
    '''
    画出xy坐标轴
    '''
    ax = plt.gca()  # 获得坐标轴对象

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴   指定左边的边为 y 轴

    ax.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))


def func11():
    x = [0]
    y = [1]

    plt.xlim((-2, 2))  # 设置X坐标轴的范围
    plt.ylim((-1, 2))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('deta(t)')  # 设置坐标轴的文字标签

    plt.title('单位冲激信号')  # 设置标题
    plt.grid()  # 显示网格

    plt.scatter(x, y, color='r')
    plt.show()


def func12():
    x = [-3, -2, -1, 0, 0, 1, 2, 3]
    y = [0, 0, 0, 0, 1, 1, 1, 1]

    plt.xlim((-5, 5))  # 设置X坐标轴的范围
    plt.ylim((-1, 2))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('deta(t)')  # 设置坐标轴的文字标签

    plt.title('单位阶跃信号')
    plt.grid()  # 显示网格

    plt.plot(x, y, color='r')
    plt.show()


def func13():
    x = [0, 0]
    y = [-1, 1]

    plt.xlim((-2, 2))  # 设置X坐标轴的范围
    plt.ylim((-2, 2))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('deta(t)')  # 设置坐标轴的文字标签

    plt.title('冲激偶信号')
    plt.grid()  # 显示网格

    plt.scatter(x, y, color='r')
    plt.show()


def func14():
    x = np.arange(0, 5)
    y = x

    plt.xlim((-1, 5))  # 设置X坐标轴的范围
    plt.ylim((-1, 5))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('r(t)')  # 设置坐标轴的文字标签

    plt.title('斜坡信号')

    plt.grid()  # 显示网格

    plt.plot(x, y, color='r')
    plt.show()


def func15():
    x = np.arange(-5, 5, 0.1) * np.pi
    y = np.sin(x) / x
    y[np.where(np.isnan(y))] = 1

    plt.xlim((np.floor(-5 * np.pi), np.ceil(5 * np.pi)))  # 设置X坐标轴的范围
    plt.ylim((-0.4, 1))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('Sa(t)')  # 设置坐标轴的文字标签

    plt.title('抽样信号')

    plt.plot(x, y, color='r')
    plt.grid()  # 显示网格
    plt.show()


def func16():
    tau = 3
    x = np.arange(-5, 5, 0.01)
    y = np.zeros_like(x)
    y[np.where(tau > np.abs(x))] = 1

    plt.xlim((-5, 5))  # 设置X坐标轴的范围
    plt.ylim((-0.2, 1.2))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('G(t)')  # 设置坐标轴的文字标签

    plt.text(-tau - 0.3, -0.1, r'-$\tau$',
             fontdict={'size': 16, 'color': 'r'})  # 显示tau文本
    plt.text(tau - 0.2, -0.1, r'$\tau$',
             fontdict={'size': 16, 'color': 'r'})

    plt.title('方波脉冲信号')

    plt.plot(x, y, color='r')
    plt.grid()  # 显示网格
    plt.show()


def func17():
    tau = 4
    x = np.arange(-tau, tau, 0.01)
    y = np.zeros_like(x)
    y[np.where(np.abs(x) <= tau)] = 1 - (np.abs(x) / tau)

    plt.xlim((-tau - 1, tau + 1))  # 设置X坐标轴的范围
    plt.ylim((-0.2, 1.2))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('Gt(t)')  # 设置坐标轴的文字标签

    plt.text(-tau - 0.3, -0.1, r'-$\tau$',
             fontdict={'size': 16, 'color': 'r'})
    plt.text(tau - 0.2, -0.1, r'$\tau$',
             fontdict={'size': 16, 'color': 'r'})

    plt.title('三角形脉冲信号')

    plt.plot(x, y, color='r')
    plt.grid()  # 显示网格
    plt.show()


def func18():
    x = np.arange(-5, 5, 0.01)
    y = np.ones_like(x)
    y[np.where(x < 0)] = -1

    plt.xlim((-5, 5))  # 设置X坐标轴的范围
    plt.ylim((-1.2, 1.2))  # 设置Y坐标轴的范围

    plt.xlabel('t')  # 设置坐标轴的文字标签
    plt.ylabel('Gt(t)')  # 设置坐标轴的文字标签

    plt.title('符号函数')

    plt.plot(x, y, color='r')
    plt.grid()  # 显示网格
    plt.show()


def func19():
    # 画第一个子图
    ax1 = plt.subplot(141)
    ax1.set_title('单位样值序列')
    ax1.set_xlim((-1.5, 3.5))
    ax1.set_ylim((-0.5, 4))
    ax1.set_xlabel('n')
    ax1.set_ylabel('Sigma(n)')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax1.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax1.spines['left'].set_position(('data', 0))
    x = [0]
    y = [1]
    ax1.scatter(x, y, color='r')
    for i, xx in enumerate(x):
        ax1.plot([xx, xx], [0, y[i]], color='b', linewidth=2.5, linestyle="-")

    # 画第二个子图
    ax2 = plt.subplot(142)
    ax2.set_title('单位阶跃序列')
    ax2.set_xlim((-1.5, 3.5))
    ax2.set_ylim((-0.5, 4))
    ax2.set_xlabel('n')
    ax2.set_ylabel('Sigma(n)')
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax2.xaxis.set_ticks_position('bottom')
    ax2.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax2.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax2.spines['left'].set_position(('data', 0))
    x = np.arange(0, 5)
    y = np.ones_like(x) * 0.5
    ax2.scatter(x, y, color='r')
    for i, xx in enumerate(x):
        ax2.plot([xx, xx], [0, y[i]], color='b', linewidth=2.5, linestyle="-")

    # 画第三个子图
    ax3 = plt.subplot(143)
    ax3.set_title('斜波序列')
    ax3.set_xlim((-1.5, 3.5))
    ax3.set_ylim((-0.5, 4))
    ax3.set_xlabel('n')
    ax3.set_ylabel('Sigma(n)')
    ax3.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax3.xaxis.set_ticks_position('bottom')
    ax3.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax3.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax3.spines['left'].set_position(('data', 0))
    x = np.arange(0, 4)
    y = x
    ax3.scatter(x, y, color='r')
    for i, xx in enumerate(x):
        ax3.plot([xx, xx], [0, y[i]], color='b', linewidth=2.5, linestyle="-")

    # 画第四个子图
    ax4 = plt.subplot(144)
    ax4.set_title('矩形序列')
    ax4.set_xlim((-1.5, 3.5))
    ax4.set_ylim((-0.5, 4))
    ax4.set_xlabel('n')
    ax4.set_ylabel('Sigma(n)')
    ax4.spines['right'].set_color('none')
    ax4.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax4.xaxis.set_ticks_position('bottom')
    ax4.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴   指定左边的边为 y 轴
    ax4.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax4.spines['left'].set_position(('data', 0))
    x = np.arange(0, 5)
    y = np.ones_like(x)
    ax4.scatter(x, y, color='r')
    for i, xx in enumerate(x):
        ax4.plot([xx, xx], [0, y[i]], color='b', linewidth=2.5, linestyle="-")

    # plt.grid()  # 显示网格
    plt.show()


if __name__ == "__main__":
    setting()
    # func11()
    # func12()
    # func13()
    # func14()
    # func15()
    # func16()
    # func17()
    # func18()
    func19()
