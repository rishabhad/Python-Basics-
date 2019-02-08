#how to convert binary to int
value=[]
item=[x for x in input().split(',')]
for p in item:
    intp = int(p,2)
    if(intp%5==0):
       value.append(intp)
print(value)

   
