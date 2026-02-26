# week01-2.py
# LeetCode 75: Array / String Q1 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""    # 答案塞在 ans 裡
        n1, n2 = len(word1), len(word2)
        i, j = 0, 0           # word1[i] vs. word2[j]
        while i<n1 or j<n2:   # 只要任一個還有剩
            if i<n1: ans += word1[i]     # 沒用完
            if j<n2: ans += word2[j]     # 沒用完
            i, j = i+1, j+1   # 都換下一位
        return ans # 答案在這裡
