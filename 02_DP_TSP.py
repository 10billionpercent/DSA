n=int(input())
d=[list(map(int,input().split()))for _ in range(n)]
dp=[[1e9]*n for _ in range(1<<n)]
dp[1][0]=0
for mask in range(1<<n):
 for u in range(n):
  if mask&(1<<u):
   for v in range(n):
    if mask&(1<<v)==0:
     dp[mask|(1<<v)][v]=min(dp[mask|(1<<v)][v],dp[mask][u]+d[u][v])
print(min(dp[-1][i]+d[i][0]for i in range(n)))