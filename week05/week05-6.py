# week05-6.py
# LeetCode 75: Hash Map / Set Q4 2352. Equal Row and Column Pairs
# 橫的、直的，完全相同「有幾組」
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() # Hash Map 可以知道有哪些 row 出現幾次

        for row in grid: # 每個 row 逐一處理
            counter[ tuple(row) ] += 1
            # tuple() 把陣列[3,1,2,2], 變不會動 (3,1,2,2)

        ans = 0 # 有幾組?

        for col in zip(*grid): # 矩陣 transpose 再取出 col
            ans += counter[ tuple(col) ]

        return ans
