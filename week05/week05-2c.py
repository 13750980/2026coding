# week05-2c.py
# LeetCode 75: Hash Map / Set Q1 2215. Find the Difference of Two Arrays 第三個版本
# 谁在左邊, 谁在右邊
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2) # 2b: 加速版本
        return [list(nums1 - nums2), list(nums2 - nums1)] # 2c: 用 list 的
