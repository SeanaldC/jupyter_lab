import numpy as np
def eco_goodwin(y, t, s, n, delta, sig, phi0, phi1, phi2, a0, a1, a2, a3, theta0, theta1, lam, X, G, d):
    omega, eta, e, gx, gk, gv, gz = y
    dydt = [phi0+phi1/(1-e)+(phi2-1)*(a0+a1/(1-e)+a2*omega+a3*eta), theta0+theta1*eta+(v^(-sig/(sig-1)))/(1-sig)*(gx-(1-omega-eta-delta*z)/(s*k-z)), (1-omega-eta-delta*z)/(s*k-z)-n, lam*(1-X/G)-d, (1-omega-eta-delta*z)/(s*k-z), gx - (1-omega-eta-delta*z)/(s*k-z), gk-(1-omega-eta-delta*z)/(s*k-z)]
    return dydt


# Initialize parameters
