# week04-5.py
# LeetCode 75: Prefix Sum Q2 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) # 陣列的長度
        prefix = [0] # 一開始 prefix sum 只有一個 [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i]) # 陣列變長了

        postfix = [0] * (n+1)
        for i in range(n-1, -1, -1): # 倒過來的迴圈
            postfix[i] = postfix[i+1] + nums[i]
        for i in range(n):
            if prefix[i] == postfix[i+1]: return i

        return -1
