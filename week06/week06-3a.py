# week06-3a.py 學習計畫 Bit Manipulation 第3題
# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
# 你可在 a 和 b 動手腳，flip切換一些bits，希望 a OR b 得到 c
class Solution:  # 目標「最少flip次數」
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0  # 先用之前教過的「剝皮法」試試 while 配合 %2 及 //2 取出每個 bit
        while a or b or c:  # 只要還有任一個數還有，就繼續「剝皮」
            # 觀察「剝下來的皮」a%2 b%2 c%2
            if c%2==1:  # 目標「做出 1」
                if a%2==0 and b%2==0:  # 不幸，都還是 0
                    ans += 1  # 可挑任 1 個，變成 1
            else:  # c%2==0 目標「做出 0」
                ans += a%2 + b%2  # 只要有 1，都要付出代價（若 a,b 都是 1 就得付 2 次）
            a, b, c = a//2, b//2, c//2  # 要小心這一行，要「剝皮」
        return ans
