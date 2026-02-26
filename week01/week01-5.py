# week01-5.py
# LeetCode 75: Array / String Q7 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)   # 陣列的長度
        preSum = [1]    # 左邊累積乘起來的值
        postSum = [1]   # 右邊累積乘起來的值
        for i in range(n):
            preSum.append(preSum[-1]*nums[i]) # 每次多乘一個數
            #print(preSum) # 看一下乘出來的過程
            postSum.append(postSum[-1]*nums[n-1-i]) # 每次多乘右邊一個數
            #print(postSum) # 檢查
        ans = [] # 最後的答案
        for i in range(n):
            ans.append(preSum[i]*postSum[n-1-i]) # 左邊累積*右邊累積
        return ans
