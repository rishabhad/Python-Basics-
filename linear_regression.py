import numpy as np
import pandas as pd

df =pd.read_csv('ex1data1.txt' , header = None )
df = df.values
pop = df[:,[0]]
#print(pop.shape)
Y = df[:,[1]]
#print(Y.shape)
#print(pop.shape);
nr_X,nc_X = pop.shape
x1 = np.ones((nr_X,1))
X = np.hstack((x1,pop))
#print(X);
nr_X,nc_X = X.shape
#print(nc_X)
#print(X.shape)
df_theta=pd.read_csv("theta.txt",header=None);
theta=df_theta.values;
#print(theta.shape);
#print(theta)

from compute_cost import cost_function 
result = cost_function(X,Y,theta)
#print(result)
                                    
                                   
                                                                       
