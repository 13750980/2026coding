# week02-2.py
# LeetCode 75: Two Pointers Q1 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums) # 陣列大小
        k = 0         # 宣告 k 已開始在最左邊待者
        for i in range(n): # 把 nums[i] 逐一檢查
            if nums[i] != 0:        # 遇到不是 0 的數, 要搬到左邊
                nums[k] = nums[i]   # 左邊 nums[k] 右邊 nums[i]
                k += 1              # 換下一個位置

        for i in range(k, n): # 剩下的格子
            nums[i] = 0       # 全部補 0
        """
        Do not return anything, modify nums in-place instead.
        """
