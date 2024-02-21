#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2600. K 件物品的最大和 https://leetcode.cn/problems/k-items-with-the-maximum-sum/
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes + numZeros:
            return min(k, numOnes)
        else:
            return numOnes - (k - numOnes - numZeros)


if __name__ == '__main__':
    obj = Solution()
    print(obj.kItemsWithMaximumSum(3, 2, 0, 2))  # 2
    print(obj.kItemsWithMaximumSum(3, 2, 0, 4))  # 3
    print(obj.kItemsWithMaximumSum(6, 6, 6, 13))  # 5
