# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# week08-2.py
# LeetCode 75: Binary Search Q1 374. Guess Number Higher or Lower
# 給你 guess() 你可以呼叫他, 找出 1 ... n 裡面的答案
class Solution:
    def guessNumber(self, n: int) -> int:
        # 方法1: 神奇的 bisect_left() 寫法, 只要1行
        # for i in range(n+1): print( -guess(i), end=' ' ) # 做實驗, 不計算
        return bisect_left( range(n+1), 0, key=lambda x:-guess(x) ) # 一行抵下面7行

        # for i in range(1, n+1): # 「錯誤」的方法, for 迴圈找答案
        #     if guess(i)==0: return i # 猜中了, 答案是 i
        # 不能用上面的 for 迴圈, 因為 n 有 20 億倍變大, 試不完
        # 要用小學「猜數字」每次範圍摘一半, 比它大、比它小, 縮小範圍

        # 方法2: while left < right: 去逼近
        left, right = 1, n + 1 # 左右的範圍 ([ '包含' , ) '不包含' )

        while left < right: # 左右的範圍還沒有「撞在一起」
            mid = (left + right) // 2 # (猜) 中間的數

            if guess(mid) == 0:
                return mid # 猜到中間的數了

            if guess(mid) > 0:
                left = mid + 1 # (暗示你) 再高一點 (中點設成下界)
            else:
                right = mid # (暗示你) 再低點 (中點設成上界)

        return left
        # week08-3 是要在紙上, 把這題 Easy 題的 left, right, mid 跟猜的數字弄懂
