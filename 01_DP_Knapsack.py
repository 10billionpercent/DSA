n,W=map(int,input().split())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
dp=[[0]*(W+1)for _ in range(n+1)]
for i in range(n):
 for w in range(W+1):
  if wt[i]<=w:dp[i+1][w]=max(dp[i][w],dp[i][w-wt[i]]+val[i])
  else:dp[i+1][w]=dp[i][w]
print(dp[n][W])