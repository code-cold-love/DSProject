# -*- coding: utf-8 -*-
# 11. 盛最多水的容器 https://leetcode.cn/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        left, right = 0, n - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:  # 向内移动短板
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
