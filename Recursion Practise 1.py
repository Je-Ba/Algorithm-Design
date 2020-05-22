import numpy

def appen_array(k,n=0,array=[]):
    if n == k:
        return
    else:
        array.append(n)
        fun(k,n+1,array)
    return(array)

def sum(n, total=0):
    if n==0:
        return(total)
    else:
        return(sum(n-1,total+n))

def factorial(x):
    if x==1:
        return(1)
    else:
        return(x*factorial(x-1))

def fibonacci(n):
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

def power(k):
    if k==0:
        return(1)
    else:
        return(2*power(k-1))

def bineary_search_sortedarray(array,k):
    mid=len(array)//2
    if array[mid]==k:
        return(array[mid],mid)
    elif array[mid]>k:
        return(bineary_search(array[:mid],k),'left half')
    elif array[mid]<k:
        return(bineary_search(array[mid:], k),'right half')
    else:
        return('k not found ')

def bineary_search_itterative(array,k):
    for i in range(0,len(array)):
        if array[i]==k:
            return(k)
    else:
        return 'K not found'



print(bineary_search_unsortedarray([1,2,3,4,5],5))
