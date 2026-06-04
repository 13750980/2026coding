# week15-1a.py
# LeetCode 75: DP - Multidimensional Q1 62. Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache  # 記憶化 Top-Down DP

        def helper(i, j):  # 函式呼叫函式，現在若在 (i,j)座標
            if i == m - 1 and j == n - 1:
                return 1  # 走到終點，成功
            if i == m or j == n:
                return 0  # 走超過邊界，失敗
            return helper(i + 1, j) + helper(i, j + 1) # 函式呼叫函式

        return helper(0, 0)  # 函式呼叫函式，從起點 (0, 0) 開始出發
