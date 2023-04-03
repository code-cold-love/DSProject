# -*- coding: utf-8 -*-
# 1574. 删除最短的子数组使剩余数组有序 https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        for i in range(right, 0, -1):
            if arr[i - 1] > arr[i]:
                right = i
                break
            else:
                right -= 1
        if right == 0:
            return 0
        res = right
        while left == 0 or arr[left - 1] <= arr[left]:
            while right < n and arr[right] < arr[left]:
                right += 1
            res = min(res, right - left - 1)
            left += 1
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.findLengthOfShortestSubarray([1, 2, 3]))  # 0
    print(obj.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))  # 4
    print(obj.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))  # 3
