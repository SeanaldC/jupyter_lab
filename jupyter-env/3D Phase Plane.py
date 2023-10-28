import numpy as np
from matplotlib import pyplot as plt
from phaseportrait import PhasePortrait2D
from phaseportrait import Trajectory2D, Trajectory3D


def dFDampedPendulum(theta, v):
    return v, -0.75*v-np.sin(theta)

DampedPendulum = PhasePortrait2D(dFDampedPendulum, [-4, 4], MeshDim=100, Title='Damped pendulum', xlabel=r"$\Theta$", ylabel=r"$\dot{\Theta}$")
DampedPendulum.plot()







