n,W=map(int,input().split())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
dp=[[0]*(W+1)for _ in range(n+1)]
for i in range(n):
 for w in range(W+1):
  if wt[i]<=w:dp[i+1][w]=max(dp[i][w],dp[i][w-wt[i]]+val[i])
  else:dp[i+1][w]=dp[i][w]
print(dp[n][W])

#alt

def knapsack(wt, val, W):
    n = len(wt)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

print("0/1 Knapsack:", knapsack(wt, val, W))