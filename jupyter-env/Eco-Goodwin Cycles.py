import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



# Initialize parameters
s=0.8
n=0.01
delta=0.01
sig=-100000000
phi0=-1
phi1=1
phi2=2 #Captures worker power
a0=1
a1=1
a2=1
a3=1
theta0=0
theta1=1
G=100
lam=0.1
d=1
rho=1

# solve the system dy/dt = f(y, t)
def f(y, t):
     wi = y[0]
     etai = y[1]
     ei = y[2]
     xi = y[3]
     ki = y[4]
     vi = y[5]
     zi = y[6]
     bi = y[7]
     y_outi = y[8]
     # the model equations 
     f0 = wi*(phi0+phi1/(1-ei)+(phi2-1)*(a0+a1/(1-ei)+a2*wi+a3*etai))
     f1 = etai*(theta0+theta1*etai+((vi**(sig/(1-sig)))/(sig-1))*(lam*(1-xi/G)-d-(1-wi-etai-delta*zi)/(s*ki-zi)))
     f2 = ei*((1-wi-etai-delta*zi)/(s*ki-zi)-n)
     f3 = xi*(lam*(1-xi/G)-d)
     f4 = ki*((1-wi-etai-delta*zi)/(s*ki-zi))
     f5 = vi*(lam*(1-xi/G)-d - (1-wi-etai-delta*zi)/(s*ki-zi))
     f6 = zi*((1-wi-etai-delta*zi)/zi-(1-wi-etai-delta*zi)/(s*ki-zi))
     f7 = bi*(theta0+theta1*etai)
     f8 = y_outi*((1-wi-etai-delta*zi)/(s*ki-zi))
     return [f0, f1, f2, f3, f4, f5, f6, f7, f8]

# Initial conditions

w0 = 0.3
eta0 = 0.3
e0 = 0.8
x0 = 400
k0 = 100
b0=1
y_init=(rho*k0**((sig-1)/sig)+b0*x0**(sig/(sig-1)))**(sig/(sig-1))
z0=k0/y_init
v0=x0/y_init


y0 = [w0,eta0,e0,x0,k0,v0,z0,b0,y_init]

t = np.linspace(0, 100, 101) # Fails after 2.3

# Solve ODEs

soln = odeint(f, y0, t, atol=1e-10, rtol=1e-10)
w = soln[:, 0]
eta = soln[:, 1]
e = soln[:, 2]
x = soln[:, 3]
k = soln[:, 4]
v = soln[:, 5]
z = soln[:, 6]
b = soln[:, 7]
y_out = soln[:, 8]

# plot results
plt.figure()
plt.plot(t, w, label='Wage Share')
plt.plot(t, eta, label='Nature Share')
plt.plot(t, e, label='Employment Rate')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Percent')
plt.title('Eco-Goodwin Cycles')
plt.savefig('goodwin_model_plot.png')  # Save the plot as an image


# Compute Jacobian matrix at the final time point
J = np.zeros((len(y0), len(y0)))
for i in range(len(y0)):
    y_perturbed = y0.copy()
    y_perturbed[i] += 1e-6  # Perturb the ith component
    J[:, i] = (f(y_perturbed, t[-1])[0] - f(y0, t[-1])[0]) / 1e-6

# Compute and print eigenvalues
eigenvalues = np.linalg.eigvals(J)
print("Eigenvalues of the Jacobian at the final time point:", eigenvalues)
