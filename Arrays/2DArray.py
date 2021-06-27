# Program to show 2D Array Operations in Python

from array import * 

arrayval = [[30,20,10,5], [50,40,30,20], [60,40,20,10], [100,30,50,70]]

print(arrayval[0])

print(arrayval[2][3])

arrayval.insert(2, [8,10,12,14,16])
print(arrayval)

for c in arrayval:
    for i in c:
        print(i, end=" ")
        print()


 # Delete the 2D Array element value

del arrayval[2]

for e in arrayval:
     for n in c:
         print(n, end=" ")
         print()  
       
