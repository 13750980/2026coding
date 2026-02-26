# week01-3.py
# LeetCode 75: Array / String Q2 1071. Greatest Common Divisor of Strings
# 程そ计 gcd ﹃
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       # 蛤程そ计 gcd Τ闽
       n1, n2 = len(str1), len(str2) # ㄢ﹃
       n = gcd(n1, n2) # 程そ计
       ans = str1[:n]  # ﹃ 1 玡 n ダ

    # ぃ才, 碞ア毖
       if ans*(n1//n) != str1: return ""
       if ans*(n2//n) != str2: return ""
       return ans
