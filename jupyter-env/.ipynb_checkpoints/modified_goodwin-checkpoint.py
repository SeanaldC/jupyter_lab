import matplotlib.pyplot as plt
import phaseportrait
from phaseportrait.streamlines import *

gam=1
O=1
a=1
s=0.1
p=2
d=0.1
n=0.01
lam=2
Gam=100
damp=0.3
b=1


def dF(w,e,x):
    return -gam+O*x/(1-e)-a, s*(1-w)*p-(a+d+n), lam*(1-x/Gam)-damp*b

p1 = phaseportrait.PhasePortrait3D(dF, [0, 3])
p1.plot()
plt.show()



#def dF(x,y,z, *, w=1):
 #   return -y, x, -z + w


#p2 = phaseportrait.PhasePortrait3D(dF, [-3, 3], MeshDim=8, maxLen=2500, deltat=0.05)

#p2.add_slider('w')

#p2.plot(color='viridis', grid=False)
#plt.show()