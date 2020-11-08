import numpy as np
import matplotlib.pyplot as plt

A = (1, 2, 0, 3, 4)

for x in A:
    y = np.cos(x)
    print(y)

x = np.arange(-10, 10.01, 0.01)
#x = (1, 2, 5, 7, 8, 9, 11, 20)
#y = (1, 2, 3, 5, 5, 6, 10, 11)
plt.figure(figsize=(10, 5))
#plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
#plt.plot(x, x)
#plt.plot(x, y)
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
#plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_ith_legend.png')
plt.show()

