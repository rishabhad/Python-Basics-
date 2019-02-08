import math
D= input('Enter any temprature by comma seperation').split(",")
print(type(D))
c=50
h=30
Q=[]

for i in D :
    print(type(i))
    p=round(math.sqrt(2*c* int(i)/h))
    Q.append(p)
print(str(Q))
#print(",".join(str(Q)))

