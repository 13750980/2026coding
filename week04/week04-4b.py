# week04-4b.py (糶 week04-3.py)
# 1732. more Challenges 3866. First Unique Even Element
# т皚 nums 柑瞷筁1Ω案计琌街
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        h = [0] * 200
        for nn in nums: # р皚硋ㄓ
            h[nn] += 1 # 参璸计秖
        for nn in nums: # ㄓΩ硋ㄓ
            if nn % 2 == 0 and h[nn] == 1: # 案计 and 辅虫
                return nn
        return -1
