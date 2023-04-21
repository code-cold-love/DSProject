# -*- coding: utf-8 -*-
# 1004. 最大连续1的个数 III https://leetcode.cn/problems/max-consecutive-ones-iii/
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # nums[i] 不是 0 就是 1
        n, left = len(nums), 0
        l_sum = r_sum = 0  # 前缀和
        ans = 0
        for right in range(n):
            r_sum += 1 - nums[right]  # 将数组中的 0 变成 1，1 变成 0
            while r_sum - l_sum > k:  # 单个窗口里，0 的数量不能超过 k
                l_sum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestOnes([0, 0, 1, 1, 1, 0, 0], 0))  # 3
    print(obj.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
