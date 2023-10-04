import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def func(var, t, m, k, c, A, f0, alpha):
    x, v = var
    force = A*np.sin(2*np.pi*(f0*t + alpha*t*t/2))
    dvdt = -(k/m)*x - (c/m)*v + force
    return [v, dvdt]

g = 9.81
c = 1.0
m = 1.0
k = 100

tmax = 100
t = np.arange(0,tmax,0.005)

A = 15
f0 = -5
f1 = 50
alpha = (f1-f0)/tmax

force = A*np.sin(2*np.pi*(f0*t + alpha*t*t/2))

zeta = 0.12
cc = 2*np.sqrt(m*k)*zeta

var0 = [0.0, 1.0]

sol = odeint(func, var0, t, args=(m, k, cc, A, f0, alpha))

omega = np.sqrt(k/m)

velocity = (-var0[0]*omega*np.sin(omega*t)+var0[1]*np.cos(omega*t))

disp = var0[0]*np.cos(omega*t)+(var0[1]/omega)*np.sin(omega*t)

fig = plt.figure(num='1自由度非減衰系の自由振動シミュレーション')
fig.suptitle('Displacement and velocity')
ax1 = fig.add_subplot(221)
ax1.set_xlabel('time [s]')
ax1.set_ylabel('velocity [m/s]')
ax1.set_ylim(-5,5)

ax2 = fig.add_subplot(223)
ax2.set_xlabel('time [s]')
ax2.set_ylabel('displacement [mm]')
ax2.set_ylim(-0.50,0.50)

ax3 = fig.add_subplot(122)
ax3.set_xlabel('time [s]')
ax3.set_ylabel('F [N]')

print(sol)

ax1.plot(t, sol[:,1], 'b', label='Python odeint [x0=0, v0=0.1]')
#ax1.plot(t, velocity, 'r', label='Theory', c='b', marker='o', linestyle='None')

ax2.plot(t, sol[:,0], 'r', label='Displacements (mm)')
ax3.plot(t, force, 'r', label='Displacements (mm)')

ax1.grid()
ax2.grid()
plt.show()
plt.close()