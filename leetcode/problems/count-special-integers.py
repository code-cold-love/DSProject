#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2376. 统计特殊整数 https://leetcode.cn/problems/count-special-integers/
from functools import cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 特殊整数：正整数每一个数位都是互不相同的
        if n < 11:
            return n

        @cache
        def dp(mask: int, prefix_smaller: bool) -> int:
            """
            计算以某些数字组合为前缀的特殊整数的数量
            :param mask: 表示前缀中使用过的数字，二进制表示下，从最低位开始，第 i 位如果为 1 则表示数字 i 已经被使用过
            :param prefix_smaller: 表示当前的前缀是否小于 n 的前缀
            :return:
            """
            if mask.bit_count() == k:
                return 1
            res = 0

            # 如果前面没有数字，则必须从 1 开始，不能有前导零
            lower_bound = 1 if mask == 0 else 0

            # prefix_smaller 为 True，则接下来的数字可以任意选择；如果不是，即当前的前缀等于 n 的前缀，则接下来的数字只能小于等于 n 同数位的数字
            upper_bound = 9 if prefix_smaller else int(n_str[mask.bit_count()])
            for i in range(lower_bound, upper_bound + 1):
                if mask >> i & 1 == 0:  # 是 0 说明数字 i 尚未被使用
                    res += dp(mask | (1 << i), prefix_smaller or i < upper_bound)
            return res

        n_str = str(n)
        k = len(n_str)  # n 十进制表示下的位数
        ans = 0
        prod = 9
        # 位数小于 k 的特殊整数的数量
        for j in range(k - 1):
            ans += prod
            prod *= 9 - j

        # 位数等于 k 的特殊整数的数量
        ans += dp(0, False)
        dp.cache_clear()
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSpecialNumbers(5))  # 5
    print(solution.countSpecialNumbers(20))  # 19
    print(solution.countSpecialNumbers(135))  # 110
