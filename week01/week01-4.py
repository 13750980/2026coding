# week01-4.py
# LeetCode 75: Array / String Q3 1431. Kids With the Greatest Number of Candies
# 你給額外的 extraCandies 後, 小朋友手上的糖果, 會不會最多?
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = [] # 答案的 True 和 False 塞在裡面
        best = max(candies) # 目前小朋友最多有幾顆糖?
        for candy in candies:   # 逐一檢查, 如果把 extraCandies 給小朋友
            if candy + extraCandies >= best: ans.append(True)
            else: ans.append(False) # 會不會 >= 最多的, 依序塞入 ans
        return ans
