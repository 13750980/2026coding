# week05-2a.py
# LeetCode 75: Hash Map / Set Q1 2215. Find the Difference of Two Arrays 爛版本
# 谁在左邊, 谁在右邊
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = [] # 放「在nums1 但不在 nums2」的數
        for n in nums1: # 逐一取出
            if n not in nums2: # 沒在裡面
                ans1.append(n) # 放入答案
        ans2 = [] # 放「在nums2 但不在 nums1」的數
        for n in nums2:
            if n not in nums1:
                ans2.append(n)

        return [list(set(ans1)), list(set(ans2))] # 把方括號list變set,再變回list，重覆的就不見了
