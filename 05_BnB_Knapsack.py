def knapsack_bb(w, v, W):
    n = len(w)
    ans = [0]

    def bound(i, cap, p):
        b = p
        while i < n and w[i] <= cap:
            b += v[i]
            cap -= w[i]
            i += 1
        if i < n:
            b += v[i] * cap / w[i]
        return b

    def dfs(i, cap, p):
        if i == n:
            ans[0] = max(ans[0], p)
            return
        if w[i] <= cap:
            dfs(i + 1, cap - w[i], p + v[i])
        if bound(i + 1, cap, p) > ans[0]:
            dfs(i + 1, cap, p)

    items = sorted(zip(v, w), key=lambda x: x[0] / x[1], reverse=True)
    v, w = zip(*items)
    dfs(0, W, 0)
    return ans[0]

w = [10, 20, 30]
v = [60, 100, 120]
W = 50

print("Knapsack BnB:", knapsack_bb(w, v, W))