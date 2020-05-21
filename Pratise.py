#import random as ra
#lis_number = []
#for i in range(0, 10):
#    lis_number.append(ra.random())

lis_number=[5,2,6,3,1,7,12]
for i in range(0, len(lis_number)):
    j = i
    while j > 0 and lis_number[j - 1] > lis_number[j]:
        lis_number[j], lis_number[j - 1] = lis_number[j - 1], lis_number[j]
        j -= 1

print(lis_number)
