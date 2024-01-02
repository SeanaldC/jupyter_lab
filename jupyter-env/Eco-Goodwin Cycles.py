import numpy as np
def eco_goodwin(y, t, s, n, delta, sig, phi0, phi1, phi2, a0, a1, a2, a3, theta0, theta1, lam, G, d):
    omega, eta, e, x, k, v, z, b = y
    dydt = [omega*(phi0+phi1/(1-e)+(phi2-1)*(a0+a1/(1-e)+a2*omega+a3*eta)), eta*(theta0+theta1*eta+((v**(sig/(1-sig)))/(1-sig))*(lam*(1-x/G)-d-(1-omega-eta-delta*z)/(s*k-z))), e*((1-omega-eta-delta*z)/(s*k-z)-n), x*(lam*(1-x/G)-d), k*((1-omega-eta-delta*z)/(s*k-z)), v*(lam*(1-x/G)-d - (1-omega-eta-delta*z)/(s*k-z)), z*((1-omega-eta-delta*z)/(s*k-z)-(1-omega-eta-delta*z)/(s*k-z)), b*(theta0+theta1*eta)]
    return dydt


# Initialize parameters
s=0.8
n=0.01
delta=0.01
sig=0.1
phi0=-1
phi1=1
phi2=1 #Captures worker power
a0=1
a1=1
a2=1
a3=1
theta0=0
theta1=1
G=100
lam=0.1
d=1
rho=1

y0 = [0.3,0.3,0.8,400,100,1,1,1]

y=(rho*y0[5]**((sig-1)/sig)+b*y0[4]**(sig/(sig-1)))**(sig/(sig-1))
z=y0[5]/y
v=y0[4]/y

t = np.linspace(0, 100, 101)

from scipy.integrate import odeint
sol = odeint(eco_goodwin, y0, t, args=(s, n, delta, sig, phi0, phi1, phi2, a0, a1, a2, a3, theta0, theta1, lam, G, d), rtol=1e-6, atol=1e-8)


import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='Wage Share')
plt.plot(t, sol[:, 1], 'g', label='Nature Share')
plt.plot(t, sol[:, 2], 'c', label='Employment Rate')
plt.legend(loc='best')
plt.xlabel('t')
plt.title('Environmental Fallout of Class Conflict')
plt.grid()
plt.show()



plt.plot(t, sol[:, 3], 'g', label='Natural Capital Growth')
plt.plot(t, sol[:, 4], 'b', label='Capital Accumulation')
plt.legend(loc='best')
plt.xlabel('t')
plt.title('Capitals')
plt.grid()
plt.show()

plt.plot(t, sol[:, 7], 'b', label='Nature-biased technical change')
plt.legend(loc='best')
plt.xlabel('t')
plt.title('Tech')
plt.grid()
plt.show()


