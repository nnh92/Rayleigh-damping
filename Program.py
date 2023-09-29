import numpy as np
from matplotlib import pyplot as plt

f = open("input.inp", 'r').readlines()

mode1 = int(input("Nhap mode dao dong so 1:"))
mode2 = int(input("Nhap mode dao dong so 2:"))

def ReadFileF(f):
    lst = []
    x = []
    y = []
    for i in range(len(f)):
        lst.append(f[i].split(	))
        x.append(float(lst[i][0]))
        y.append(float(lst[i][1]))
    return x, y

def generate_rayleigh_damping(f1, f2, h1, h2):
    beta = (h1*f1 - h2*f2)/np.pi/(f1*f1-f2*f2)
    alpha = 4*h1*np.pi*f1 -4*np.pi*np.pi*beta*f1*f1
    return alpha, beta

def check_rayleigh_damping(alpha, beta, fi, x, y):
    zeta = alpha/4/np.pi/fi + beta*np.pi*fi

    fig, ax = plt.subplots(num='Rayleigh damping')

    ax.plot(fi, zeta, color = 'magenta')
    ax.grid()
    ax.set_xlim(0,70)
    ax.set_ylim(0,0.2)
    ax.set(xlabel='Response angular frequency (Hz)', ylabel='Damping ratio (%)', title='Mass and Stiffness')
    
    ax2 = ax.twinx()
    ax2.scatter(x, y,color = 'orange', s = 3)

    plt.text(45,0.14, r'$\alpha$ = {}'.format(round(alpha,6)))
    plt.text(45,0.13, r'$\beta$  = {}'.format(round(beta,6)))

    plt.show()
    plt.close()

x, y = ReadFileF(f)

alpha, beta = generate_rayleigh_damping(float(x[mode1-1]), float(x[mode2-1]), float(y[mode1-1]), float(y[mode2-1]))

fi = np.arange(0.01,70,0.005)
check_rayleigh_damping(alpha, beta, fi, x, y)