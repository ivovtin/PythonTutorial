import numpy as np
import matplotlib.pyplot as plt

# равномерно распределённые значения от 0 до 5, с шагом 0.2
t = np.arange(0., 5., 0.2)

# красные чёрточки, синие квадраты и зелёные треугольники
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
