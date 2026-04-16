# week08-5.py
# LeetCode 75: Binary Search Q3 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
         # 笨方法: for 迴圈不行嗎?(因為這題只有 1000 個數)
        n = len(nums) # 陣列大小 n
        if n == 1: return 0   # if N==1: i=0 最大 (只有1個數, 就是最大, 別再 nums[i-1] nums[i+1]了啦)

        for i in range(n):
            if i == 0: # 第一個元素：沒有左鄰，只測右鄰 (要比右鄰大)
                if nums[i] > nums[i+1]: return i

            elif i == N-1: # 最後一個元素：沒有右鄰，只測左鄰 (要比左鄰大)
                if nums[i] > nums[i-1]: return i

            # 下面可能會當機，因 i-1 或 i+1 會超過範圍，所以加上上面的 if
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

        # 快速法:
        N = len(nums)
        def is_peak_slope(i):
            # 如果 i 是最後一項，我們假設它右邊是負無窮大，所以一定是 True
            if i == N - 1:
                return True
            # 判斷當前位置是否處於「下坡」 (即當前比右邊大)
            return nums[i] > nums[i+1]

        # 使用 bisect_left 尋找第一個 True (即第一個下坡點)
        # key 參數會對 range(N) 裡的每個 index 執行 is_peak_slope
        return bisect_left(range(N), True, key=is_peak_slope)
