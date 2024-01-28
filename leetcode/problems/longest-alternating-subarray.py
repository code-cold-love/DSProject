# -*- coding: utf-8 -*-
# 2765. 最长交替子数组 https://leetcode.cn/problems/longest-alternating-subarray/
from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)  # n >= 2
        ans, left = -1, 0
        for i in range(1, n):
            length = i - left + 1
            if nums[i] - nums[left] == (length - 1) % 2:
                ans = max(ans, length)
            else:
                if nums[i] - nums[i - 1] == 1:
                    left = i - 1
                    ans = max(ans, 2)
                else:
                    left = i
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.alternatingSubarray([4, 5, 6]))  # 2
    print(obj.alternatingSubarray([2, 3, 4, 3, 4]))  # 4
