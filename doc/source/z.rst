
Z Transform
===========

ZT用于平面极坐标形式的复数 :math:`z=r e^{j \Omega}` 域分析。

（单边）ZT公式如下：

..  math::
    X(z) &= ZT[x(n)] = \sum_{n=0}^{\infty} x(n)z^{-n} \\

ZT将频率从实数域扩展到复数域，DTFT可以看作ZT的特例（ :math:`z` 的模为1，即 :math:`r=1` ）。

:math:`z` 平面与 :math:`s` 平面的映射：

..  math::
    z = e^{sT_s}
      = e^{(\sigma + j \omega) T_s}
      = e^{\sigma T_s} e^{j \omega T_s}
      = re^{j \Omega}

..  image:: z/z_s_map.png
    :align: center
    :scale: 50%

对于 :math:`z` 域的传递函数的零极点，也有和 :math:`s` 域零极点类似的结论：

#. 如果在单位圆上有零点，则在零点所对应的频率上幅值响应为零；
#. 对于不在单位圆上的零点，在单位圆上离零点最近的点对应的频率上幅值响应最小；
#. 对于在单位圆内部的极点，在单位圆上离极点最近的点对应的频率上幅值响应最大；
#. 如果极点和零点重合，对系统的频率响应没有影响。

:参考:

- `如何快速设计一个FIR滤波器(一) <https://zhuanlan.zhihu.com/p/45138629>`_
- `如何快速设计一个FIR滤波器(二) <https://zhuanlan.zhihu.com/p/45520018>`_
- `如何快速设计一个IIR滤波器 <https://zhuanlan.zhihu.com/p/51097798>`_
