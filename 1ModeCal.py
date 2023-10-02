import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def func(state, t, m, k):
    x1, x2 = state
    dx2dt = -(k/m)*x1
    return [x2, dx2dt]

m = 0.5
k = 1000
state0 = [0.0, 0.1]

t = np.linspace(0, 1,501)

sol = odeint(func, state0, t, args=(m, k))

print(sol)

plt.plot(t, sol[:], 'b', label='theta(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()