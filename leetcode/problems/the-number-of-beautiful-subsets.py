# -*- coding: utf-8 -*-
# 2597. 美丽子集的数目 https://leetcode.cn/problems/the-number-of-beautiful-subsets/
from typing import List
from collections import defaultdict, Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # 1 <= nums.length <= 20
        # 1 <= nums[i], k <= 1000
        groups = defaultdict(Counter)
        for i in nums:
            groups[i % k][i] += 1
        ans = 1
        for cnt in groups.values():
            g = sorted(cnt.items())
            m = len(g)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 1 << g[0][1]
            for i in range(1, m):
                if g[i][0] - g[i - 1][0] == k:
                    f[i + 1] = f[i] + f[i - 1] * ((1 << g[i][1]) - 1)
                else:
                    f[i + 1] = f[i] << g[i][1]
            ans *= f[m]
        return ans - 1  # 去掉空集

    def beautifulSubsets_1(self, nums: List[int], k: int) -> int:
        nums.sort()
        d1, d2, d3 = defaultdict(list), defaultdict(int), Counter(nums)
        for i in range(len(nums)):
            val = nums[i]
            if val in d2:
                continue
            elif val - k in d2:
                d2[val] = d2[val - k]
                d1[d2[val]].append(val)
            else:
                d2[val] = val
                d1[val] = [val]
        ans = 1
        for key, value in d1.items():
            dp = [2 ** d3[value[0]] - 1, 1]
            for i in range(1, len(value)):
                dp[0], dp[1] = dp[1] * (2 ** d3[value[i]] - 1), dp[0] + dp[1]
            ans *= sum(dp)
        return ans - 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.beautifulSubsets(nums=[1], k=1))  # 1
    print(obj.beautifulSubsets(nums=[2, 4, 6], k=2))  # 4

    print(obj.beautifulSubsets_1(nums=[1], k=1))  # 1
    print(obj.beautifulSubsets_1(nums=[2, 4, 6], k=2))  # 4
