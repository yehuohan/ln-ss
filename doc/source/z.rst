
Z Transform
===========

ZT用于平面极坐标形式的复数 :math:`z=r e^{j \Omega}` 域分析。

（单边）ZT公式如下：

..  math::
    X(z) &= ZT[x(n)] = \sum_{n=0}^{\infty} x(n)z^{-n} \\

ZT将频率从实数域扩展到复数域，DTFT可以看作ZT的特例（ :math:`z` 的模为1，即 :math:`r=1` ）。
