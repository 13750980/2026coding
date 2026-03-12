# week03-2.py
# LeetCode 75: Sliding Window Q1 643. Maximum Average Subarray I
# 用Sliding Window 毛毛蟲的解法
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums) # 陣列的長度
        total = sum(nums[:k])   # 加總 [:k] 前 k 項
        maxTotal = total

        for i in range(k, n): # 右邊的頭
            total = total + nums[i] - nums[i-k]
            # nums[i]右邊的頭(往右吃), nums[i-k]左邊的尾巴, 吐出來
            maxTotal = max(maxTotal, total)  # 持續更新

        return maxTotal/k # 回傳最大平均
