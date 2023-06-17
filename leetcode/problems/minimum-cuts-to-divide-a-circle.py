# -*- coding: utf-8 -*-
# 2481. 分割圆的最少切割次数 https://leetcode.cn/problems/minimum-cuts-to-divide-a-circle/
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n <= 1:
            return 0
        elif n % 2 == 0:
            return n >> 1
        else:
            return n


if __name__ == '__main__':
    obj = Solution()
    print(obj.numberOfCuts(3))  # 3
    print(obj.numberOfCuts(4))  # 2
