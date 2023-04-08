# -*- coding: utf-8 -*-
# 2399. 检查相同字母间的距离 https://leetcode.cn/problems/check-distances-between-same-letters/
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # s 仅由小写字母组成，其中的每个字母恰好出现两次
        # distance 长度为 26
        n = len(s)
        first_index = [0] * 26
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first_index[idx] and i - first_index[idx] != distance[idx]:
                return False
            first_index[idx] = i + 1
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.checkDistances('abaccb', [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # True
