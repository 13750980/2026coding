# week08-4.py
# LeetCode 75: Binary Search Q2 2300. Successful Pairs of Spells and Potions
# 想知道某種 spells[i] 魔法, 配幾種藥水可以成功?
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # 藥水「小到大」排好
        p =len(potions) # 有 P 個藥水
        ans = []
        for spell in spells: # 每一個魔法, 都試一次
            # 使用二分搜尋找出第一個符合「藥水能量 * 魔法 >= success」的位置
            # 移項後：藥水能量 >= (success / spell)
            now = p - bisect_left(potions, success/spell)
            ans.append(now) # 全部藥水 P 瓶 - 會失敗的藥水(??瓶), 便是成功的藥水數量

        return ans
