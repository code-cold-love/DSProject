# -*- coding: utf-8 -*-
# 1027. 最长等差数列 https://leetcode.cn/problems/longest-arithmetic-subsequence/
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        diff = max_val - min_val
        ans = 1
        for d in range(-diff, diff + 1):
            dp = dict()
            for num in nums:
                if (prev := num - d) in dp:  # := 海象运算符，特殊的赋值表达式
                    dp[num] = max(dp.get(num, 0), dp[prev] + 1)
                    ans = max(ans, dp[num])
                dp[num] = max(dp.get(num, 0), 1)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestArithSeqLength([3, 6, 9, 12]))  # 4
    print(obj.longestArithSeqLength([9, 4, 7, 2, 10]))  # 3
    print(obj.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))  # 4
