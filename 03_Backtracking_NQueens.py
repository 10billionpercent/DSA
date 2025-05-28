def solve(r):
 if r==n:
  print(sol)
  return
 for c in range(n):
  if c in col or r+c in pos or r-c in neg:continue
  col.add(c);pos.add(r+c);neg.add(r-c);sol.append(c)
  solve(r+1)
  col.remove(c);pos.remove(r+c);neg.remove(r-c);sol.pop()
n=int(input())
col,pos,neg,sol=set(),set(),set(),[]
solve(0)