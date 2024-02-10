import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp



# Initialize paramters
theta = 0.1
gamma = 1
l = 0.01
tau = 0 #maybe?
s = 1
a = 0.5
Gamma = 100
lam = 0.02
d = 1


# solve the system dy/dt = f(t, y)
def f(t, y):
     wi = y[0]
     Xi = y[1]
     ei = y[2]
     # the model equations 
     f0 = (theta/(1-ei)-gamma)
     f1 = ((lam*(1-Xi/Gamma) - d*(1-tau)*(Xi**(a-1))) - (s*(Xi**(a))*(1 - wi - tau*(Xi**(1-a)))))
     f2 = (a*(f1) + ((s*(Xi**(a))*(1 - wi - tau*(Xi**(1-a))))) - l)
     return [f0, f1, f2]

# Initial conditions
w0 = 0.6
N0 = 30
K0 = 1
e0 = 0.8
X0 = N0/K0


f_init = [w0, X0, e0]

t = np.linspace(0, 200, 1000) 

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

plt.figure()
plt.plot(t, X, label='Capital Ratio')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Capital Ratio')
plt.title('Eco-Goodwin Cycles')



from phaseportrait import PhasePortrait2D
from phaseportrait import PhasePortrait3D
from phaseportrait.streamlines import *
from phaseportrait import Trajectory2D, Trajectory3D

def df(w, e, X):
    return (w*(theta*e-gamma), e*(a*((lam*(1-X/Gamma) - (1-tau)*(X**(a-1))) - (s*(X**(a))*(1 - w - tau*X**(1-a)))) + ((s*(X**(a))*(1 - w - tau*X**(1-a)))) - l), X*((lam*(1-X/Gamma) - (1-tau)*(X**(a-1))) - (s*(X**(a))*(1 - w - tau*(X**(1-a))))))

dist_conflict = PhasePortrait3D(df, [-1,1], MeshDim=10, Title='Eco-Goodwin Cycles', xlabel='Wage Share', ylabel='Employment Rate', zlabel = 'Capital Ratio')
dist_conflict.plot(color='viridis', grid=True)
plt.show()


goodwin = Trajectory3D(
    df, 
    lines=True, 
    n_points=1300, 
    size=3, 
    mark_start_position=True, 
    Title='Eco-Goodwin Cycles'
    )

goodwin.initial_position(0.4,0.8,10)
goodwin.initial_position(0.5,0.6,10.0001)
goodwin.plot(color = 'viridis')

