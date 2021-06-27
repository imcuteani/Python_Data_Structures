# Python program to display simple Array 

from array import * 

arrayval  = array('i', {20, 40, 60, 80, 100})
print(arrayval[0])
print(arrayval[2])

for x in arrayval:
    print(x)


# Insert operation
arrayval.insert(1, 30)
print(arrayval[1])

#reverse an array
arrayval.reverse()
print(arrayval)

#Remove an array element
arrayval.remove(20)
print(arrayval)

# Update Array element
arrayval[4] = 120

for y in arrayval:
    print(y)