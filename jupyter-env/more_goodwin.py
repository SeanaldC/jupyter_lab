import numpy as np
def goodwin(y, t, g, theta, a, s, lam, G, p, damp, b, d, n, X):
    w, e, x = y
    dydt = [(theta*X/(1-e)-g-a)/10, s*(1-w)*p-(n+d+a), lam*(1-X/G)-damp*b]
    return dydt


theta = 1
g = 7
a=0.4
s=0.7
lam = 1
p=2.5
G=1
damp=0.5
b=2
d=0.1
n=0.01
X=0.75

y0 = [0.6,0.8, 1]

t = np.linspace(0, 5, 101)

from scipy.integrate import odeint
sol = odeint(goodwin, y0, t, args=(g, theta, a, s, lam, G, p, damp, b, d, n, X))

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='Wage Share')
plt.plot(t, sol[:, 1], 'g', label='Employment Rate')
plt.plot(t, sol[:, 2], 'c', label='Natural Capital')
plt.legend(loc='best')
plt.xlabel('t')
plt.title('Environmental Fallout of Class Conflict')
plt.grid()
plt.show()

