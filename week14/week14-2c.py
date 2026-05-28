# week14-2c.py
# LeetCode 75: DP - 1D Q1 1137. N-th Tribonacci Number

class Solution:
    @cache  # 使用記憶化（Memoization）直接裝飾類別方法
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]  # 初始化基礎情況的前三項值
        if n < 3:
            return a[n]  # 若 n 為 0, 1, 2 則直接回傳對應值

        # 直接遞迴呼叫自身的類別方法，並將前三項結果相加
        return (
            self.tribonacci(n - 1)
            + self.tribonacci(n - 2)
            + self.tribonacci(n - 3)
        )
