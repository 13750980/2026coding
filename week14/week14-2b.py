# week14-2b.py
# LeetCode 75: DP - 1D Q1 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]  # 初始化前三項的基礎值

        @cache  # 函式呼叫函式（不要重複問答案，自動記錄算過的值）
        def helper(i):
            if i < 3:
                return a[i]  # 基礎情況：直接回傳 a 陣列裡的值
            # 遞迴計算前三項之和
            return helper(i - 1) + helper(i - 2) + helper(i - 3)

        return helper(n)  # 呼叫輔助函式並回傳第 n 個泰波那契數
