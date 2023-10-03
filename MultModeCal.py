import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def func(state, t, m, k):
    x1, x2 = state
    dx2dt = -(k/m)*x1 - 2*alpha*x2/m
    return [x2, dx2dt]

g = 9.81
alpha = 2.2
m = 0.5
k = 1000
state0 = [0.0, 0.2]

t = np.arange(0,1,0.005)

sol = odeint(func, state0, t, args=(m, k))

omega = np.sqrt(k/m)

velocity = (-state0[0]*omega*np.sin(omega*t)+state0[1]*np.cos(omega*t))

disp = state0[0]*np.cos(omega*t)+(state0[1]/omega)*np.sin(omega*t)

fig = plt.figure(num='1自由度非減衰系の自由振動シミュレーション')
fig.suptitle('Displacement and velocity')
ax1 = fig.add_subplot(211)
ax1.set_ylabel('velocity [m/s]')
ax1.set_ylim(-0.25,0.25)

ax2 = fig.add_subplot(212)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('displacement [mm]')
ax2.set_ylim(-0.005,0.005)

print(sol)

ax1.plot(t, sol[:,1], 'b', label='Python odeint [x0=0, v0=0.1]')
#ax1.plot(t, velocity, 'r', label='Theory', c='b', marker='o', linestyle='None')

ax2.plot(t, sol[:,0], 'r', label='Displacements (mm)')
ax1.grid()
ax2.grid()
plt.show()
plt.close()