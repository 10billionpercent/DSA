"""You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers. You should return the array of nums such that the the array follows the given conditions: . Every consecutive pair of integers have opposite signs."""
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