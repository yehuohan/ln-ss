
Laplace Transform
=================

LT用于复数（ :math:`s=\sigma + j \omega` ）域分析。

（单边）LT公式如下：

..  math::
    X(s) &= LT[x(t)] = \int_0^{\infty} x(t) e^{-st} dt \\
    x(t) &= LT^{-1}[X(s)] = \frac{1}{2 \pi j} \int_{\sigma - j \infty}^{\sigma + j \infty} F(s) e^{st} ds, \quad t > 0

LT将频率从实数域扩展到复数域，FT可以看作LT的特例（ :math:`s` 为纯虚数）。
