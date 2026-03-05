# week02-3.py
# LeetCode 75: Two Pointers Q2 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t) # 字串長度
        if n1==0: return True   # 有陷阱: 如果左邊字串是空的, 就不用比較了
        i = 0 # 宣告 i 從 0 開始
        for k in range(n2): # 右邊一個個去試
            if s[i] == t[k]: # 找到 1 個左右, 符合的
                i += 1 # 左邊的 i 往右升一級
            if i==n1: # 左邊的 i 有走到左邊就結束
                return True
        # 否則沒有對比成功
        return False
