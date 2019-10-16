
Laplace Transform
=================

LT用于复数（ :math:`s=\sigma + j \omega` ）域分析。

（单边）LT公式如下：

..  math::
    X(s) &= LT[x(t)] = \int_0^{\infty} x(t) e^{-st} dt \\
    x(t) &= LT^{-1}[X(s)] = \frac{1}{2 \pi j} \int_{\sigma - j \infty}^{\sigma + j \infty} F(s) e^{st} ds, \quad t > 0

LT将频率从实数域扩展到复数域，FT可以看作LT的特例（ :math:`s` 为纯虚数）。


- 传递函数

在零初始条件下，线性时不变系统输出量的拉氏变换，与输入量的拉氏变换之比，称为该系统的传递函数：

..  math::
    G(s) = \frac{Y_o(s)}{X_i(s))}

频率特性：

..  math::
    G(j \omega) = \frac{Y_o(j \omega)}{X_i(j \omega))} = G(s)|_{s = j \omega}


当 :math:`G(s)=0` ，称为系统零点，对应频率的幅值为零，即无输出（滤波）；

当 :math:`G(s)=\infty` ，称为系统极点，对应频率的幅值无穷大，即放大输入。
