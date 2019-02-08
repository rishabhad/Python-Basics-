import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def l_cost(X,Y,df_theta):
    print(X.shape)
    
    z=np.dot(X,df_theta)
   
    from sigmoid_pract import sigmoid
    hx = sigmoid(z)
    print(hx)
    J_theta = ((- np.multiply(np.log(hx),Y) - np.multiply(np.log(1-hx),(1-Y))))
    cost=J_theta.sum()/X.shape[0]
    return cost












