# -*- coding: utf-8 -*-
# 1732. 找到最高海拔 https://leetcode.cn/problems/find-the-highest-altitude/
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        ans = max(0, gain[0])
        for i in range(1, n):
            gain[i] = gain[i] + gain[i - 1]
            ans = max(ans, gain[i])
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.largestAltitude([-5, 1, 5, 0, -7]))  # 1
    print(obj.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # 0
