# week06-4b.py 學習計畫 Array / String 最後1題
# LeetCode 605. Can Place Flowers
# 在長長的花壇 flowerbed 裡，1 已經種花、0 還沒種花。花要間隔放
# 問：能不能再種 n 盆花
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)  # 有幾個格子
        if N == 1 and flowerbed[0] == 0: return n <= 1  # 特殊狀況

        for i in range(N):  # 逐一檢查
            # (左邊在邊界外 or 左邊空的)                   (右邊在邊界外 or 右邊是空的)
            if (i-1 < 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i+1 >= N or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0
