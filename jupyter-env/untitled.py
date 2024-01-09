import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp



# Initialize parameters
s=0.8
n=0.01
delta=0.01
sig=-10
phi0=-1
phi1=1
phi2=2 #Captures worker power
a0=1
a1=1
a2=1
a3=1
theta0=-1
theta1=1
G=100
lam=0.1
d=1
rho=1

# define system of ODEs

def dSdt(t, S):
    w, eta, e, x, k, v, z, y, b = S
    return[w*(phi0+phi1/(1-e)+(phi2-1)*(a0+a1/(1-e)+a2*w+a3*eta)),
          eta*(theta0+theta1*eta+((v**(sig/(1-sig)))/(sig-1))*(lam*(1-x/G)-d-(1-w-eta-delta*z)/(s*k-z))),
          e*((1-w-eta-delta*z)/(s*k-z)-n),
          x*(lam*(1-x/G)-d),
          k*((1-w-eta-delta*z)/(s*k-z)),
          v*(lam*(1-x/G)-d - (1-w-eta-delta*z)/(s*k-z)),
          z*((1-w-eta-delta*z)/z-(1-w-eta-delta*z)/(s*k-z)),
          y*((1-w-eta-delta*z)/(s*k-z)),
          b*(theta0+theta1*eta)]

# Initial conditions

w0 = 0.3
eta0 = 0.3
e0 = 0.8
x0 = 75
k0 = 100
b0=1
y0=(rho*k0**((sig-1)/sig)+b0*x0**(sig/(sig-1)))**(sig/(sig-1))
z0=k0/y0
v0=x0/y0


S0 = [w0,eta0,e0,x0,k0,v0,z0,y0,b0]

t = np.linspace(0, 100, 10000)

# Solve

sol = solve_ivp(dSdt, (0,100), y0=S0, method='DOP853', t_eval=t, rtol=1e-10, atol=1e-13)

t = sol.t
w1 = sol.y[0]
eta1 = sol.y[1]
e1 = sol.y[2]
x1 = sol.y[3]
k1 = sol.y[4]
v1 = sol.y[5]
z1 = sol.y[6]
y1 = sol.y[7]
b1 = sol.y[8]

# Plot

plt.plot(t, w1)
plt.plot(t, eta1)
plt.plot(t, e1)

