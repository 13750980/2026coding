# week02-5.py
# LeetCode 75: Two Pointers Q4 1679. Max Number of K-Sum Pairs
# 希望找到加起來==k 的 pair 兩兩一組, 共幾組
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() # 小到大排序, 等一下左邊挑 1 個, 右邊挑 1 個
        i, j = 0, len(nums)-1 # 最左邊 i 對應最小, 最右邊 j 對應最大
        ans = 0 # 宣告 ans

        while i<j: # 還沒撞在一起, 就可以左右各挑 1 個
            if nums[i] + nums[j] == k:  # 剛剛好
                ans += 1
                i, j = i+1, j-1 # 右邊用了, 往右; 左邊用了, 往左
            if nums[i] + nums[j] < k:   # 加起來太小了, 那左邊小的 i 加 1
                i += 1
            if nums[i] + nums[j] > k:   # 加起來太小了, 那左邊小的 i 減 1
                j -= 1
        return ans
