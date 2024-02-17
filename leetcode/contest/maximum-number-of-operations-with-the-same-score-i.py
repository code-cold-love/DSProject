# -*- coding: utf-8 -*-
# 100221. 相同分数的最大操作数目 I https://leetcode.cn/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-i/
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        pre_sum = nums[0] + nums[1]
        for i in range(0, n, 2):
            if i == n - 1:
                break
            cur_sum = nums[i] + nums[i + 1]
            if cur_sum == pre_sum:
                ans += 1
            else:
                break
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxOperations([3, 2, 1, 4, 5]))  # 2
    print(obj.maxOperations([3, 2, 6, 1, 4]))  # 1
