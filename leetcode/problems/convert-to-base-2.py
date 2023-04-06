# -*- coding: utf-8 -*-
# 1017. 负二进制转换 https://leetcode.cn/problems/convert-to-base-2/
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = []
        while n:
            remainder = n & 1  # & 按二进制位与，n & 1 -> n 为奇数得 1，n 为偶数得 0
            res.append(str(remainder))
            n -= remainder
            n //= -2
        return ''.join(res[::-1])


if __name__ == '__main__':
    obj = Solution()
    print(obj.baseNeg2(2))  # 110
