# week02-4.py
# LeetCode 75: Two Pointers Q3 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i, j = 0, len(height) -1 # 左邊 i 右邊 j
        while i<j: # 只要左右邊還沒撞在一起
            area = (j-i)*min(height[i], height[j]) # 算出現在的面積
            ans = max(ans, area)  # 更新答案
            if height[i] < height[j]: i += 1 # 小的 i , 往右
            else: j -= 1 # 小的 j , 往左
        return ans
