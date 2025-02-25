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