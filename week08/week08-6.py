# week08-6.py
# LeetCode 75: Binary Search Q4 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 準備一個函式 helper(k) 看答案對不對
        def helper(k): # 1小時吃 k 個香蕉, 能成功在 h 小時內吃完嗎?
            total = 0 # 妳猜 k, 它會用多少時間
            for pile in piles: # 很多堆香蕉, 逐一檢查
                total += pile // k # 要吃掉這堆香蕉 pile 要花多少時間
                if pile % k > 0: total += 1 # 有餘數, 再多 1 小時
            return total <= h # 符合條件 (在 h 小時內吃完)

        # 使用 bisect_left 在 [1, max(piles)] 範圍內找最小的符合條件的 k
        # 因為 range 從 1 開始, 索引會偏移, 所以最後要 +1
        return bisect_left(range(1, max(piles)), True, key=helper) + 1
