def show(n,arr):
    p=[]
    n_=[]
    for i in arr:
        if i>0:
            p.append(i)
        else:
            n_.append(i)
    for i in range((n//2)):
        print(p[i],n_[i],end=' ')
n=int(input())
a=list(map(int,input().rstrip().split()))
show(n,a)