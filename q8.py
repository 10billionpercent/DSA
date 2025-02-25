def inversion(n,arr):
    count=0
    for i in range(n):
        for j in range(n):
            if i<j and arr[i]>arr[j]:
                count+=1
    return count
n=int(input())
arr=list(map(int, input().rstrip().split()))
print(inversion(n,arr))