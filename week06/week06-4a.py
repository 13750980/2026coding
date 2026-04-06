# week06-4a.py 學習計畫 Array / String 最後1題
# LeetCode 605. Can Place Flowers
# 在長長的花壇 flowerbed 裡，1 已經種花、0 還沒種花。花要間隔放
# 問：能不能再種 n 盆花
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)  # 有幾個格子
        if N == 1 and flowerbed == [0]: return True  # 特殊狀況：只有一格且是空的，必能種 1 盆

        # 1. 檢查最左邊：如果前兩格都是空的，就可以種在第 0 格
        if N > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1  # 可以，種在最左邊
            n -= 1  # 解決掉 1 盆

        # 2. 檢查中間的部分：每格逐一檢查（從索引 1 到 N-2）
        for i in range(1, N-1):
            # 如果左、中、右全部都是空的 0
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1  # 多種一盆花
                n -= 1  # 解決掉 1 盆

        # 3. 檢查最右邊：如果最後兩格都是空的，就可以種在最後一格
        if N > 1 and flowerbed[N-2] == 0 and flowerbed[N-1] == 0:
            flowerbed[N-1] = 1  # 可以，種在最右邊
            n -= 1  # 解決掉 1 盆

        return n <= 0  # 把目標要種的花，都種完了，完成任務，開心
