# week14-3b.py
# LeetCode 75: DP - 1D Q2 746. Min Cost Climbing Stairs
# 踩在第i格的梯子上，要付出 cost[i] 的代價，每次可跨1格 or 2格
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        a = [0] * (N + 1)  # 用來查表的表格

        a[0] = cost[0]
        a[1] = cost[1]  # 幸好題目規格「一定有2格」

        for i in range(2, N + 1):
            a[i] = min(a[i - 1], a[i - 2])
            if i < N:
                a[i] += cost[i]

        return a[N]
