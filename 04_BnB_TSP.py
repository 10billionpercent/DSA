def tsp_bb(cost):
    n = len(cost)
    best = [float('inf')]

    def dfs(path, vis, curr, cost_so_far):
        if len(path) == n:
            best[0] = min(best[0], cost_so_far + cost[curr][0])
            return
        if cost_so_far >= best[0]:
            return
        for i in range(n):
            if not vis[i]:
                vis[i] = 1
                dfs(path + [i], vis, i, cost_so_far + cost[curr][i])
                vis[i] = 0

    vis = [0] * n
    vis[0] = 1
    dfs([0], vis, 0, 0)
    return best[0]

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("TSP Branch and Bound:", tsp_bb(cost))