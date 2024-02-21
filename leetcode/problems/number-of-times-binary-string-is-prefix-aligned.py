#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1375. 二进制字符串前缀一致的次数 https://leetcode.cn/problems/number-of-times-binary-string-is-prefix-aligned/
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = right = 0
        for i, flip in enumerate(flips):
            right = max(right, flip)
            if right == i + 1:
                ans += 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.numTimesAllBlue([3, 2, 4, 1, 5]))  # 2
    print(obj.numTimesAllBlue([4, 1, 2, 3]))  # 1
