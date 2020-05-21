def count_n2(array):
    k=0
    l=0
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if array[i]>array[j]:
                k+=1
            else:
                l+=1
    return(k,l)






array=[6,5,4,3,2,1]
print(count_n2(array))