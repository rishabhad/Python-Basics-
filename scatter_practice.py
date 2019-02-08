import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('ex2data1.txt', header = None )
print(df)
df = df.values
x0=df[:,[0]]
x1=df[:,[1]]
y=df[:,[2]]
y0= np.where(y==0)
y1=np.where(y==1)
#plt.scatter(x0, x1, y0, marker='o')
#plt.scatter(x0, x1, y1, marker='+')
#plt.show()

x0=df[:,[0]];
x1=df[:,[1]];
y=df[:,[2]];
m=[u'+', u'o']
col=['r','g']
for col,m in zip(col,m) :
    plt.scatter(x0,x1,s=50,c=col,marker=m);


plt.xlabel('X')
plt.ylabel('Y')
plt.show();
