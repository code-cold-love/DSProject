# -*- coding: utf-8 -*-
# 1493. 删掉一个元素以后全为 1 的最长子数组 https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 1
        has_zero = 1 - nums[left]
        ans = 0
        while left < right < n:
            if nums[right] == 0:
                if has_zero:
                    for i in range(left, right):
                        if nums[i] == 0:
                            left = i + 1
                has_zero = 1
            right += 1
            ans = max(ans, right - left - 1)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestSubarray([1, 1, 1]))  # 2
    print(obj.longestSubarray([1, 1, 0, 1]))  # 3
    print(obj.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
