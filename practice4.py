#Write a Programme to find how many number a divisible by 3,4,5 between 200 to 300
x=3
y=4
z=5
p=0
q=0
r=0
l=0
m=0
n=0
c=0

for i in range(200,301):
    if (i%x==0):
       p=p+1
    if (i%y==0):
       q=q+1
    if (i%z==0):
       r=r+1
for a in range(200,301):
    if(a%(x*y)==0):
       l=l+1
    if(a%(y*z)==0):
        m=m+1
    if(a%(x*z)==0):
        n=n+1
    if(a%(x*y*z)==0):
        c=c+1
        

print(p,q,r)
print(l,m,n,c)
result=p+q+r-l-m-n+c
print(result)


    
