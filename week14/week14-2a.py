# week14-2a.py
# LeetCode 75: DP - 1D Q1 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        # 初始化動態規劃（DP）陣列，前三項為 [0, 1, 1]，後面補上 n 個 0
        a = [0, 1, 1] + [0] * n

        # 從索引 3 開始計算到 n
        for i in range(3, n + 1):
            # 泰波那契數公式：前三項總和
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]

        return a[n]  # 回傳第 n 個泰波那契數



