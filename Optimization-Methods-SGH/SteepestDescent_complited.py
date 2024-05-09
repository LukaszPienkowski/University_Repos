import numpy as np
import matplotlib.pyplot as plt

n_grid = 100

f = lambda x: (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2; #Rosenbrock function
x0 = np.array([1, 1], dtype = float) #Starting point

def num_gradient(f, x, h=10**(-6)): #Numeric Gradient calculated with Central derrivative
    n = x.size
    e_i = np.identity(n)
    g = [(f(x + e_i[i,]*h/2) - f(x - e_i[i,]*h/2)) / (h) for i in range(n)]
    return(np.array(g, dtype = float))

def line_search(f, x0, x1, grid_size = 100): #Line search to find local minimum of x
    out = x0
    for i in range(grid_size):
        t = (i+1)/grid_size 
        x_t = x0 * (1-t) + x1 * t
        if f(x_t) < f(out):
            out = x_t
        else:
            break;
    return(out)

def steepest_descent(f, x, a = 1, grid_size = 100, max_num_iterations = 100): #Steepest descent method
    results = {'x_opt': x, 
               'y_opt': f(x),
               'x_hist': [x], 
               'y_hist': [f(x)]}
    
    for k in range(max_num_iterations):
        x = line_search(f, x, x - a * num_gradient(f, x))
    
        results['x_opt'] = x 
        results['y_opt'] = f(x)
        results['x_hist'].append(x) 
        results['y_hist'].append(f(x))
    
    return(results)

sd = steepest_descent(f, x0)

print(f(x0)) #Output

