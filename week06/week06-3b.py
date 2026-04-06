# week06-3b.py 學習計畫 Bit Manipulation 第3題
# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
# 你可在 a 和 b 動手腳，flip切換一些bits，希望 a OR b 得到 c
class Solution:  # 目標「最少flip次數」
    def minFlips(self, a: int, b: int, c: int) -> int:
        # 善用 Bit 運算：AND OR NOT XOR
        # 0010 (a)
        # 0110 (b)
        # 先 OR 起來
        # 0110 (a | b)

        # 把 c「反過來」，所有的 0 都變成 1，再看 a,b 對應項有幾個 1
        c2 = ~c  # bitwise NOT 反過來
        # 需要「把 1 變成 0」有幾個？
        ans = bin(a & c2).count('1') + bin(b & c2).count('1')

        # 需要「把 0 變成 1」有幾個？
        ans += bin(c & ~(a | b)).count('1')

        # 合併的結果中，有 1 的項，都是有的，但若沒有，要補 1
        return ans
