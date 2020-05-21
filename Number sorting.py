def random_number_sorter_course(number_of_numbers):
    import random as ra
    import time as ti
    starting_time=ti.time()
    lis_number=[]
    for i in range(0,number_of_numbers):
        lis_number.append(ra.random())

    for i in range(0,len(lis_number)):
        j=i
        while j>0 and lis_number[j-1]>lis_number[j]:
            lis_number[j],lis_number[j-1]=lis_number[j-1],lis_number[j]
            j -= 1
    for n in range(0,len(lis_number)):
        if lis_number[n+1]<lis_number[n]:
            return('not correct')
        else:
           return('Correct, the time is',ti.time()-starting_time)

def random_number_sorter_own(number_of_numbers):
    import random as ra
    list_number=[]
    import time as ti
    starting_time2 = ti.time()
    for i in range(0,number_of_numbers):
        list_number.append(ra.random())
        for j in range(0,len(list_number)):
            for i in range(0,len(list_number)):
                if list_number[j]<list_number[i]:
                    list_number[i],list_number[j]=list_number[j],list_number[i]
    for n in range(0,len(list_number)):
        if list_number[n+1]<list_number[n]:
            return('not correct')
        else:
            return ('Correct, the time for own code is', ti.time() - starting_time2)





print(random_number_sorter_course(500))
print(random_number_sorter_own(500))



