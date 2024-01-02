import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from phaseportrait import PhasePortrait2D

p=8
g=0.1
n=0.01
phi=1
lam=1

def dF(w, e):
    return ((1-w)*p-(g+n),-phi+lam/(1-e)-g)



example = PhasePortrait2D(dF, [0, 1], Polar=False, Title='Goodwin cycle')
fig, ax = example.plot()


# Define the Goodwin model
def goodwin(y, t, p, g, n, phi, lam):
    w, e = y
    dydt = [(1-w)*p-(g+n),
           -phi+lam*e-g]
    return dydt

p=1
g=0.1
n=0.01
phi=1
lam=2

# Set initial conditions
y0 = [0.6, 0.68]  # Initial values of w, e, v

# Set time points
t = np.linspace(0, 10, 1000)

# Solve the system of ODEs
sol = odeint(goodwin, y0, t, args=(p, g, n, phi, lam))

# Plot the results
plt.plot(t, sol[:, 0], label='Wage Share (w)')
plt.plot(t, sol[:, 1], label='Employment Rate (e)')
plt.xlabel('Time')
plt.ylabel('Shares')
plt.title('Neo-Marxian Goodwin Cycle')
plt.legend()
plt.show()


# Plot the results with wage share on the horizontal axis and employment rate on the vertical axis
plt.plot(sol[:, 0], sol[:, 1], label='Goodwin Cycle')
plt.xlabel('Wage Share (w)')
plt.ylabel('Employment Rate (e)')
plt.title('Neo-Marxian Goodwin Cycle')
plt.legend()
plt.show()