def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)



def merge_two_lists(a,b):
    merged_list=[]
    j=0
    i=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            merged_list.append(a[i])
            i+=1
        else:
            merged_list.append(b[j])
            j+=1
    if i==len(a):
        merged_list = merged_list+b[j:]
    if j==len(b):
        merged_list = merged_list + a[i:]
    return(merged_list)

print(merge_two_lists([1,3,5,7,9,11,18,20],[2,4,6,8,9,10]))