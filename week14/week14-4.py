# week14-4.py
# LeetCode 75: DP - 1D Q3 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache  # 遇到 DP 的題目，就用 Top-Down DP 來思考，特別簡單
        def helper(i):  # 如果搶到第 i 間房，最後可以拿到多少錢？
            if i >= len(nums):
                return 0  # 整個街走完了，沒得搶了

            return nums[i] + max(helper(i + 2), helper(i + 3))
            # 函式呼叫函式，來解 Top-Down DP

        return max(helper(0), helper(1))
