# -*- coding: utf-8 -*-
# 724. 寻找数组的中心下标 https://leetcode.cn/problems/find-pivot-index/
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = left_sum = right_sum = 0
        for num in nums:
            n += 1
            right_sum += num
        for pivot in range(n):
            right_sum -= nums[pivot]
            if left_sum == right_sum:
                return pivot
            left_sum += nums[pivot]
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.pivotIndex([1, 2, 3]))  # -1
    print(obj.pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
