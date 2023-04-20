# -*- coding: utf-8 -*-
# 1679. K 和数对的最大数目 https://leetcode.cn/problems/max-number-of-k-sum-pairs/
from typing import List
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for num in counter:
            if num * 2 < k:  # 处理小于 k // 2 的那一半
                ans += min(counter[num], counter.get(k - num, 0))
            elif num * 2 == k:
                ans += counter[num] // 2
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxOperations([1, 2, 3, 4], 5))  # 2
    print(obj.maxOperations([3, 1, 3, 4, 3], 6))  # 1
