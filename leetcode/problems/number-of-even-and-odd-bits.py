# -*- coding: utf-8 -*-
# 2595. 奇偶位数 https://leetcode.cn/problems/number-of-even-and-odd-bits/
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # 1 <= n <= 1000
        binary = [int(i) for i in bin(n).lstrip('0b')]
        ans = [0, 0]
        n = len(binary)
        for i in range(n):
            if binary[n - i - 1] == 0:
                continue
            elif i % 2 == 0:
                ans[0] += 1
            else:
                ans[1] += 1
        return ans

    def evenOddBit_1(self, n: int) -> List[int]:
        """数学"""
        ans = [0, 0]
        i = 0
        while n:
            ans[i] += n & 1  # & 按二进制位与，n & 1 -> n 为奇数得 1，n 为偶数得 0
            n >>= 1  # 除以 2
            i ^= 1  # ^ 按二进制位异或，每一位相同取 0，不同取 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.evenOddBit(2))  # [0, 1]
    print(obj.evenOddBit(17))  # [2, 0]
    print(obj.evenOddBit_1(2))  # [0, 1]
    print(obj.evenOddBit_1(17))  # [2, 0]
