def missing(n,arr):
    test=[i for i in range(1,n+1)]
    for i in test:
        if i not in arr:
            return i
n=int(input())
a=list(map(int, input().rstrip().split()))
print(missing(n,a))