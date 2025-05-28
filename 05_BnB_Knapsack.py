from heapq import*
n,W=map(int,input().split())
w=list(map(int,input().split()))
p=list(map(int,input().split()))
idx=sorted(range(n),key=lambda i:-p[i]/w[i])
def bound(i,cw,cp):
 b=cp
 while i<n and cw<w[idx[i]]:
  cw+=w[idx[i]]
  cp+=p[idx[i]]
  i+=1
 if i<n:b=cp+(W-cw)*p[idx[i]]/w[idx[i]]
 return b
q=[(-bound(0,0,0),0,0,0)]
res=0
while q:
 _,i,cw,cp=heappop(q)
 if i==n:res=max(res,cp);continue
 if cw+w[idx[i]]<=W:
  heappush(q,(-bound(i+1,cw+w[idx[i]],cp+p[idx[i]]),i+1,cw+w[idx[i]],cp+p[idx[i]]))
 heappush(q,(-bound(i+1,cw,cp),i+1,cw,cp))
print(res)