import numpy as nu

def martix_one(A,B,n):
    c=nu.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                c[i,j]+=A[i,k]*B[k,j]
    return(c)

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def Strassens_algorithm(A,B,n):
    split_A=split(A)
    split_B=split(B)
    p1=split_A[0]*(split_B[1]-split_B[3])
    p2= split_B[3] * (split_A[0] + split_A[1])
    p3= split_B[0] * (split_A[2] + split_A[3])
    p4= split_A[3] * (split_B[2] - split_B[1])
    p5= (split_A[0]+split_A[3]) * (split_B[1] + split_B[3])
    p6 = (split_A[1] - split_A[3]) * (split_B[2] +split_B[3])
    p7 = (split_A[0] - split_A[2]) * (split_B[0] * split_B[2])
    solution_matrix=([p5+p4-p2+p6,p1+p2,p3+p4,p1+p5-p3-p7])
    return(solution_matrix)


A = nu.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
B = nu.random.rand(4,4)
print(martix_one(A,B,len(A)))
print(Strassens_algorithm(A,B,len(A)))
