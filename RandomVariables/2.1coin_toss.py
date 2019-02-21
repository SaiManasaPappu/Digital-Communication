#Let X {1, -1}. Generate X such that the numbers 1 and -1 appear with equal probability.
#This is a random variable formulation of the coin tossing experiment.

#!/usr/bin/env python

#importing numpy, scipy, mpmath and pyplot

import numpy as np
import mpmath as mp
import scipy 
import scipy.stats as sp
#from scipy.integrate import quad
#import scipy.integrate as spint
import matplotlib.pyplot as plt
import subprocess

#function for generating coin toss
def coin(x):
	return 2 * np.random.randint(2, size = x) - 1	#func generates *1* number, range [0,2),  Z
	
print coin(1)
