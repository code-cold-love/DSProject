# -*- coding: utf-8 -*-
# 2859. 计算 K 置位下标对应元素的和 https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits/
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def bit_count(x: int) -> int:
            cnt = 0
            while x:
                cnt += (x % 2)
                x //= 2
            return cnt

        ans = 0
        for i, v in enumerate(nums):
            if bit_count(i) == k:
                ans += v
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.sumIndicesWithKSetBits([4, 3, 2, 1], 2))  # 1
