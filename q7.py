"""You are given a n x m sparse matrix A with the majority of its elements being zero. Your task is to find the k-th smallest non-zero element in this matrix.

The matrix is represented as a list of non-zero elements along with their positions, i.e., A[i][j] = val for each non-zero element. If k is greater than the number of non-zero elements, return -1.

"""
def ksmallest(nmk,arr):
    nonzero=[]
    for i in arr:
        nonzero.append(i[2])
    nonzero.sort()
    if nmk[2]<p:
        return nonzero[nmk[2]-1]
    else:
        return -1
nmk=list(map(int, input().rstrip().split()))
p=int(input())
arr=[]
for i in range(p):
    arr.append(list(map(int, input().rstrip().split())))
print(ksmallest(nmk,arr))