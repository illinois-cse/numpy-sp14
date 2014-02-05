#!/usr/bin/env python
"""
Hooke's law is named after the 17th century British physicist Robert Hooke. He first stated this law in 1660 as a Latin anagram "ceiiinosssttuv", whose solution he published in 1678 as "Ut tensio, sic vis"; literally translated as: "As the extension, so the force". (Wikipedia)

Herein we estimate the spring constant for a given spring from experimental data.  The data consist of displacements of the spring observed for different imposed masses.  We can write F = mg = kd; thus, k = m*g/d.  We will use first-order curve fitting to obtain k.
"""
from __future__ import division
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

# Mass / g
m = np.array((5,10,20,50,100))
# Displacement / mm
d = np.array((15.5,33.07,53.39,140.24,301.03))
# Accel. of gravity / kg m^2 s^-1
g = 9.81

# Calculate the force due to each point and fit a line to these data.
F = m / 1000 * g
a = np.polyfit(d,F,1)

# From this fit, prepare a data set for comparison.
d_fit = np.linspace(0,300,31)
F_fit = np.polyval(a,d_fit)

# Plot both the experimental data (as dots) and the fitted line (as line).
plt.plot(d,F,'bo',d_fit,F_fit,'r-')
plt.show()

print("k = %s" % a[0])

