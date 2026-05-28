# week14-3a.py
# LeetCode 75: DP - 1D Q2 746. Min Cost Climbing Stairs
# 踩在第i格的梯子上，要付出 cost[i] 的代價，每次可跨1格 or 2格
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache  # 函式呼叫函式，把大問題，拆成小問題
        def helper(i):  # 現在踩在第i格，之後要多少錢？
            if i >= len(cost):
                return 0  # 終止條件：已經跨過樓梯頂端，不需花費

            # 當前階梯代價 + 往後跨1格或2格的最小花費
            return cost[i] + min(helper(i + 1), helper(i + 2))

        # 可以選擇從第 0 格或第 1 格開始起跳，取兩者花費較小者
        return min(helper(0), helper(1))
