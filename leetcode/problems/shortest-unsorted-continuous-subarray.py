# -*- coding: utf-8 -*-
# 581. 最短无序连续子数组 https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        high, low = 0, n - 1  # 需要调整的最大位置为 high，需要调整的最小位置为 low
        max_num, min_num = nums[0], nums[-1]
        for i in range(1, n):
            max_num = max(max_num, nums[i])  # 从左到右循环，记录最大值
            min_num = min(min_num, nums[n - 1 - i])  # 从右到左循环，记录最小值
            if nums[i] < max_num:  # 当前值小于从左往右已遍历的数中的最大值，更改要参与重排的元素的下标
                high = i
            if nums[n - 1 - i] > min_num:  # 当前值大于从右往左已遍历的数中的最小值，更改要参与重排的元素的下标
                low = n - 1 - i
        return high - low + 1 if high > low else 0


if __name__ == '__main__':
    obj = Solution()
    print(obj.findUnsortedSubarray([1]))  # 0
    print(obj.findUnsortedSubarray([1, 2, 3, 4]))  # 0
    print(obj.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
