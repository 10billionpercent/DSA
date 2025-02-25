import math
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
arr.sort()
diff=[]
for i in arr:
    diff.append(math.fabs(i-k))
closest=diff.index(min(diff))
print(arr[closest])
