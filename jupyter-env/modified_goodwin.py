import matplotlib.pyplot as plt
import phaseportrait
from phaseportrait.streamlines import *
import sympy as sp
import scipy as scp
from scipy.integrate import solve_ivp
from scipy.integrate import odeint




def dF(w,e,x, *, gam=3,
O=4,
a=1,
s=1,
p=3,
d=0.1,
n=0.01,
lam=0.1,
Gam=100,
damp=0.5,
b=1):
    return -gam+O*x/(1-e)-a, s*(1-w)*p-(a+d+n), lam*(1-x/Gam)-damp*b

p1 = phaseportrait.PhasePortrait3D(dF, [-3, 3], xlabel='Wage Share', ylabel='Employment Rate', zlabel='Natural Capital Stock', Title='Fallout of Distributional Conflict', MeshDim=6, maxLen=2500, deltat=0.1)
p1.plot(color='viridis', grid=True)
plt.show()



#def dF(x,y,z, *, w=1):
 #   return -y, x, -z + w


#p2 = phaseportrait.PhasePortrait3D(dF, [-3, 3], MeshDim=8, maxLen=2500, deltat=0.05)

#p2.add_slider('w')

#p2.plot(color='viridis', grid=False)
#plt.show()