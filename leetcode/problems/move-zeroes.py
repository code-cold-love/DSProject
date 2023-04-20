# -*- coding: utf-8 -*-
# 283. 移动零 https://leetcode.cn/problems/move-zeroes/
from typing import List
from collections import deque


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_idx = deque()
        for i in range(n):
            if nums[i] == 0:
                zero_idx.append(i)
            elif zero_idx:
                idx = zero_idx.popleft()
                nums[idx], nums[i] = nums[i], 0
                zero_idx.append(i)

    def moveZeroes_1(self, nums: List[int]) -> None:
        """双指针"""
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]  # 将非 0 的都移动到前面，后面的都是 0
                left += 1
            right += 1


if __name__ == '__main__':
    obj = Solution()
    arr = [0, 1, 0, 3, 12]
    obj.moveZeroes_1(arr)
    print(arr)  # [1, 3, 12, 0, 0]
