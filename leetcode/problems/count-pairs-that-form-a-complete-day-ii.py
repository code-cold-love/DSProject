#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3185. 构成整天的下标对数目 II https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # 遍历 hours 的同时，用一个哈希表记录元素的出现次数
        # 对于 hours[i]，需要知道左边有多少个模 24 是 24 - hours[i] % 24 的数
        H = 24
        ans = 0
        cnt = [0] * H  # 维护 hours[i] % 24 的出现次数
        for h in hours:
            # (H - h % H) % H 最后多进行了一次取模运算
            # 是因为如果 hours[i] % 24 是 0，那么需要知道左边有多少个模 24 也是 0 的数
            ans += cnt[(H - h % H) % H]
            cnt[h % H] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countCompleteDayPairs([72, 48, 24, 3]))  # 3
    print(solution.countCompleteDayPairs([12, 12, 30, 24, 24]))  # 2
