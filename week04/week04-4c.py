# week04-4c.py (重寫 week04-4b.py)
# 1732. more Challenges 3866. First Unique Even Element
# 找到陣列 nums 裡「只出現過1次的偶數」是誰
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        h = Counter(nums) # 使用進階資料結構，可以統計數量 Counter
        for nn in nums:
            if nn % 2 == 0 and h[nn] == 1: return nn
        return -1
