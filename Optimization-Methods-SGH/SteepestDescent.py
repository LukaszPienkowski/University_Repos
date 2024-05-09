from math import pi
import numdifftools as nd
import numpy as np
from numpy.core.fromnumeric import transpose

s_point = [3, 3] #Starting point [x0, x1]
s_point1 = s_point #For Hessian
i = 1 #Iteration number
optimum = np.array([[0], [0]]) #For checking the optimum
nsc = np.array([[1], [1]]) #For loop

## Algorithm
while nsc[0, 0] != optimum[0, 0] and nsc[1, 0] != optimum[1, 0]: #While loop - The gradient components at xi must be close to 0
    #then the loop is over
    def rosen(x): #Function for gradient
        return x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2
    
    s = nd.Gradient(rosen)(s_point)*-1 #Negative Gradient
    h = nd.Hessian(rosen)(s_point1) #Hessian
    ns = np.array([[s[0]], [s[1]]]) #Calculate s, beacause numdifftools does not want to work with numpy transposition
    tns = transpose(ns) #Same here for transposition
    c_l = np.matmul(tns, ns) #Counter of lambda equation
    d_l = np.matmul(np.matmul(tns, h), ns)#Denominator of lambda equation
    l = c_l/d_l #Compute lambda - analytical optimization
    s_point = s_point + l*s #Compute the new point
    sc = nd.Gradient(rosen)(s_point) #Check the optimum
    nsc = np.array([[sc[0]], [sc[1]]]) #New point in numpy-understandable formula
    i = i + 1 #Count iterations
    print("Iter",i,"\nX point = ", nsc)





