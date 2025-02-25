"""You are given an array of integers and a target integer k. Write a function to find the element in the array that is closest to k. If there are multiple elements equidistant from k, return the smallest of them."""


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
