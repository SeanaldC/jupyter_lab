import numpy as np
def goodwin(y, t, g, theta, a, s, lam, G, p, b, d, n, u, ghat, uhat, z, phi, bhat, rho):
    w, e, x, eta = y
    dydt = [w*(-z + theta/(1-e)), e*(s*p*u*g*(1-eta-w)+ghat+uhat-(a+n)), x*(lam*(1-x/G)-d*b), eta*(-(rho+bhat)+phi/(x/G))]
    return dydt

z=2
theta=1
g=2
a=1
s=1
lam=2
p=1
G=100
d=0.5
b=2
n=0.01
u=0.8
ghat=1
uhat=1
bhat=1
phi=1
rho=1

#conditions for economically feasible results
phi/(rho+bhat) > (a+n-(ghat+uhat))/(s*p*u*g)
theta/z<1
phi/(rho+bhat)<1
lam>d*b


y0 = [0.4,0.6, 100, 0.3]

t = np.linspace(0, 20, 101)

from scipy.integrate import odeint
sol = odeint(goodwin, y0, t, args=(g, theta, a, s, lam, G, p, b, d, n, u, ghat, uhat, z, phi, bhat, rho))

import matplotlib.pyplot as plt
plt.ylim()
plt.plot(t, sol[:, 0], 'red', label='Wage Share')
plt.plot(t, sol[:, 1], 'blue', label='Employment Rate')
plt.plot(t, sol[:, 3], 'teal', label='Nature Share')
plt.legend(loc='best')
plt.xlabel('t')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(False)
plt.savefig('goodwin_model_plot.png')  # Save the plot as an image
plt.show()

plt.ylim()
plt.plot(t, sol[:, 2], 'green', label='Natural Capital')
plt.legend(loc='best')
plt.xlabel('t')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(False)
plt.show()