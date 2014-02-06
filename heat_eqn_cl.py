from __future__ import division

import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

def calc_params(nx, nt, alpha, length, tmax):
    # Compute mesh spacing and time step.
    dx = length / (nx-1)
    dt = tmax / (nt-1)
    return (dx, dt)

def create_arrays(nx, nt):
    # Create arrays to save data in process.
    x = np.linspace(0, length+1e-15, nx)
    t = np.linspace(0, tmax+1e-15, nt)
    u = np.zeros([nx, nt])
    return (x, t, u)

def set_ic(x, length):
    # Set initial and boundary conditions.
    u[:, 0] = np.sin(np.pi*x/length)**2
    #boundaries are implicitly set by this initial condition
    return u

def plot_results(u, x):
    # Plot the results (initial and final conditions).
    mpl.rcParams['figure.figsize']=[15,3]
    plt.plot(x, u[:,0], 'k-', lw=2)
    plt.plot(x, u[:,-1],  'b-', lw=2)
    
    #import matplotlib.cm as cm
    #for i in range(len(u[:,0:-1:10])-1):
    #    c = cm.rainbow(i/len(u[:,0:-1:10]), 1)
    #    plt.plot(x[:], u[:,i], color=c, lw=2)
    
    plt.ylim((0,1))
    plt.xlim((0,1))
    plt.show()

def gen_matrix(nx, alpha, dt, dx):
    r  = alpha * dt / (dx*dx)
    s  = 1 - 2*r
    A = np.zeros((nx, nx), dtype=np.float128)
    i,j = np.indices(A.shape)
    A[i==j]   = s
    A[i==j-1] = r
    A[i==j+1] = r
    return A

# Set default values for simulation parameters.
nt = 10
nx = 20
alpha = 0.1
length = 1.0
tmax = 0.5

# Get command-line arguments.
usage = """
This program can be invoked with the following options:
    -t, --nt=       number of time steps
    -x, --nx=       number of spatial intervals
    -a, --alpha=    value of alpha in heat equation
    -l, --length=   length of beam (m)
    -m, --tmax=     maximum time value calculated

Example usage:
    python heat_eqn_cl.py --nt=10 --nx=20 --alpha=0.1 --length=1.0 --tmax=0.5

"""
import getopt, sys
options, args = getopt.getopt(sys.argv[1:],'ht:x:a:l:m:', \
                              ['help','nt=','nx=','alpha=','length=','tmax='])
for option, value in options:
    if option in ('-h','--help'):
        print(usage)
        sys.exit(0)
    elif option in ('-t', '--nt'):
        nt = int(value)
    elif option in ('-x', '--nx'):
        nx = int(value)
    elif option in ('-a', '--alpha'):
        alpha = float(value)
    elif option in ('-l', '--length'):
        length = float(value)
    elif option in ('-m', '--tmax'):
        tmax = float(value)
    else:
        print(usage)
        sys.exit('Invalid command-line argument detected.')

(dx, dt) = calc_params(nx, nt, alpha, length, tmax)
(x, t, u ) = create_arrays(nx, nt)
u = set_ic(x, length)
A = gen_matrix(nx, alpha, dt, dx)

# Loop through each time step.
for n in range(1, nt):
    u[:,n] = A.dot(u[:,n-1])

plot_results(u, x)
