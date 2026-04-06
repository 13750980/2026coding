# week06-1b.py 學習計畫 Bit Manipulation 第1題
# LeetCode 338. Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 利用「倒裝句」直接生成整個列表並回傳
        # [ 結果 for 變數 in 範圍 ]
        return [bin(i).count('1') for i in range(n + 1)]
