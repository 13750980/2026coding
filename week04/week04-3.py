# week04-3.py
# 1732. more Challenges 3866. First Unique Even Element
# 找到陣列 nums 裡「只出現過1次的偶數」是誰
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n = len(nums) # 有 N 個數
        # 第1種寫法，用陣列，先統計出現的次數
        h = [0] * 200 # 很多很多格，H[??] 對應 ?? 出現幾次

        for i in range(n): # 第一次處理
            h[nums[i]] += 1 # 把出現的數字，塞進 H[??] 裡
        # 再逐個檢查「偶數」出現幾次
        for i in range(n): # 逐一檢查
            if nums[i]%2 == 0 and h[nums[i]] == 1: # 偶數，只出現一次
                return nums[i] # 找到答案了
        return  -1
