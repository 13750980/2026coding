# week16-4.py
# LeetCode 75: Intervals Q2 452. Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort( key = lambda x:x[1] ) # 氣球隔「右邊界」排序
        ans = 0
        previous_end = -inf
        for start, end in points: # 逐一取出氣球
            if previous_end < start: # 氣球有距離哦! 只好再多射1箭
                ans += 1 # 要為現在的 [start, end] 的氣球, 射1箭
                previous_end = end
        return ans
