# week03-3.py
# LeetCode 75: Sliding Window Q2 1456. Maximum Number of Vowels in a Substring of Given Length
# 母音 Vowels: a e i o u 長度 k 的字串, 最多有幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')   # 把 5 個字母, 變成 set
        # 以後用 if c in vowels: 就可以快速確認它是母音
        # 以前 if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        count = 0 # 記錄目前有幾個母音
        for i in range(k): # 找前面 k 個字母, 逐一檢查, 看是不是母音
            if s[i] in vowels: count += 1 # 找到1個母音, 開心!!
        ans = count # 離開迴圈時, 確認前k個字母, 有 count 個母音, 先當答案
        n = len(s) # 全部字串的長度
        for i in range(k, n): # 右邊的每一個字母, 逐一檢查
            if s[i] in vowels: count += 1 # 右邊的頭 s[i] 又吃到1個母音, 開心
            if s[i-k] in vowels: count -= 1 # 左邊屁股 s[i-k] 吐掉, 失去1個母音QQ
            ans = max(ans, count) # 更新答案, 找最大值

        return ans



