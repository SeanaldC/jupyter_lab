import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp



# Initialize paramters
theta = 1
gamma = 0.8
l = 0.01
tau = 1 #maybe?
s = 1
a = 0.5
Gamma = 100
lam = 0.02


# solve the system dy/dt = f(t, y)
def f(t, y):
     wi = y[0]
     Xi = y[1]
     ei = y[2]
     # the model equations 
     f0 = (theta*ei-gamma)
     f1 = ((lam*(1-Xi/Gamma) - (1-tau)*Xi**(a-1)) - (s*Xi**(a)*(1 - wi - tau*Xi**(1-a))))
     f2 = ei*(a*(f1) + ((s*Xi**(a)*(1 - wi - tau*Xi**(1-a)))) - l)
     return [f0, f1, f2]

# Initial conditions
w0 = 0.6
N0 = 4
K0 = 1
e0 = 0.8
X0 = N0/K0


f_init = [w0, X0, e0]

t = np.linspace(0, 100, 101) 

# Solve ODEs

soln = odeint(f, y0=f_init, t=t, tfirst=True)


soln2 = solve_ivp(f, t_span=(0,max(t)), y0=f_init, t_eval=t, rtol = 1e-6, atol = 1e-9)
w = soln[:, 0]
X = soln[:, 1]
e = soln[:, 2] 

# plot results
plt.figure()
plt.plot(t, w, label='Wage Share')
plt.plot(t, e, label='Employment Rate')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Percent')
plt.title('Eco-Goodwin Cycles')
plt.savefig('goodwin_model_plot.png')  # Save the plot as an image

