# -*- coding: utf-8 -*-
# 786. 第 K 个最小的素数分数 https://leetcode.cn/problems/k-th-smallest-prime-fraction/
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # arr 严格递增且由素数组成
        n = len(arr)
        left, right = 0.0, 1.0
        while True:
            mid = (left + right) / 2  # 确定一个实数，使得恰好有 k 个素数分数小于 mid
            i, count = -1, 0
            numerator, denominator = 0, 1  # 记录最大的分数
            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:  # -1 <= i <= j - 1
                    i += 1
                    if arr[i] * denominator > arr[j] * numerator:  # 即 arr[i]/arr[j] > numerator/denominator
                        numerator, denominator = arr[i], arr[j]
                count += i + 1
            if count == k:
                return [numerator, denominator]
            elif count < k:
                left = mid
            else:
                right = mid


if __name__ == '__main__':
    obj = Solution()
    print(obj.kthSmallestPrimeFraction([1, 7], 1))  # [1, 7]
    print(obj.kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # [2, 5]
