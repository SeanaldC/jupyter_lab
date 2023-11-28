import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from phaseportrait import PhasePortrait2D

p=1
g=0.1
n=0.01
phi=2
lam=1

phi+g>lam
p>g+n

def dF(w, e):
    return (w*(-phi+lam/(1-e)-g),e*((1-w)*p-(g+n)))



example = PhasePortrait2D(dF, [0, 1], Polar=False, Title='Goodwin cycle', xlabel='Wage Share', ylabel='Employment Rate')
fig, ax = example.plot()


# Define the Goodwin model
def goodwin(y, t, p, g, n, phi, lam):
    e,w = y
    dydt = [e*((1-w)*p-(g+n)),
           w*(-phi+lam/(1-e)-g)]
    return dydt

p=1
g=0.1
n=0.01
phi=8
lam=1

phi+g>lam
p>g+n

# Set initial conditions
y0 = [0.6, 0.68]  # Initial values of w, e, v

# Set time points
t = np.linspace(0, 10, 1000)

# Solve the system of ODEs
sol = odeint(goodwin, y0, t, args=(p, g, n, phi, lam))

# Plot the results
plt.plot(t, sol[:, 1], label='Wage Share (w)')
plt.plot(t, sol[:, 0], label='Employment Rate (e)')
plt.xlabel('Time')
plt.ylabel('Shares')
plt.title('Neo-Marxian Goodwin Cycle')
plt.legend()
plt.show()


# Plot the results with wage share on the horizontal axis and employment rate on the vertical axis
plt.plot(sol[:, 1], sol[:, 0], label='Goodwin Cycle')
plt.xlabel('Wage Share (w)')
plt.ylabel('Employment Rate (e)')
plt.title('Neo-Marxian Goodwin Cycle')
plt.legend()
plt.show()