from heapq import*
n=int(input())
d=[list(map(int,input().split()))for _ in range(n)]
q=[(0,0,[0],set([0]))]
best=1e9
while q:
 c,u,path,vis=heappop(q)
 if len(path)==n:
  best=min(best,c+d[u][0]);continue
 for v in range(n):
  if v not in vis:
   heappush(q,(c+d[u][v],v,path+[v],vis|{v}))
print(best)