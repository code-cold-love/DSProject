# -*- coding: utf-8 -*-
# 2413. 最小偶倍数 https://leetcode.cn/problems/smallest-even-multiple
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n & 1 == 0 else n << 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.smallestEvenMultiple(7))  # 14
    print(obj.smallestEvenMultiple(12))
