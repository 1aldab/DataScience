import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    mean = np.mean(data)
    r_squared = 1 - ((data - predictions)**2).sum() / ((data - mean)**2).sum()
    return r_squared

data = np.array([10, 25, 30])
pred = np.array([11, 26, 33])
print compute_r_squared(data, pred)