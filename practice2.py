#Using Operater with the list
even_numbers = [2,4,6,8,10]
odd_numbers=[1,3,5,7,9]
prime=[1,2,3,5,7,11]
final=[]
all_numbers=even_numbers+odd_numbers
for i,x,y in zip(odd_numbers,even_numbers,prime):
    final.append(i)
    final.append(x)
    print(y)
print(final)
    
print(all_numbers)
