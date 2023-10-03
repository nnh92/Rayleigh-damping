import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def func(x, t):
    dxdt=1/x-np.sin(np.pi*x**x)/(x*x)
    return dxdt

x = 1
t = np.arange(0,2,0.0125)

sol = odeint(func, x, t)

print(sol)

plt.plot(t, sol[:], 'b', label='theta(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()