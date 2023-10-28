import matplotlib.pyplot as plt

from phaseportrait import PhasePortrait2D
from phaseportrait.streamlines import *
from phaseportrait import Trajectory2D, Trajectory3D

p=3
O=6
q=-1.5
s=1
sig=8
n=0.01
d=0.1


def dFdistconflict(w, e):
    return (p/(1-e)-O-q), (s*(1-w)*sig-(n+d-q))

dist_conflict = PhasePortrait2D(dFdistconflict, 1, MeshDim=25, Title='Goodwin Model', xlabel='Wage Share', ylabel='Employment Rate')
dist_conflict.plot()
plt.show()




