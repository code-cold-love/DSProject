# -*- coding: utf-8 -*-
# 2865. 美丽塔 I https://leetcode.cn/problems/beautiful-towers-i/
from typing import List


class Solution:
    def maximumSumOfHeights(self, max_heights: List[int]) -> int:
        n = len(max_heights)
        ans = 0
        for i in range(n):
            pre, tmp_sum = max_heights[i], max_heights[i]
            for j in range(i - 1, -1, -1):  # 0 <= j < i
                pre = min(pre, max_heights[j])
                tmp_sum += pre
            suf = max_heights[i]
            for k in range(i + 1, n):  # i < k < n
                suf = min(suf, max_heights[k])
                tmp_sum += suf
            ans = max(ans, tmp_sum)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumSumOfHeights([5, 3, 4, 1, 1]))  # 13
    print(obj.maximumSumOfHeights([3, 2, 5, 5, 2, 3]))  # 18
    print(obj.maximumSumOfHeights([6, 5, 3, 9, 2, 7]))  # 22
    print(obj.maximumSumOfHeights([3, 6, 3, 5, 5, 1, 2, 5, 5, 6]))  # 24
