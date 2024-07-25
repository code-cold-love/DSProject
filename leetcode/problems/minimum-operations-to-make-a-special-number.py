#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2844. 生成特殊数字的最少操作 https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/
class Solution:
    def minimumOperations(self, num: str) -> int:
        # num 表示非负整数，不含任何前导零
        # 位数为 1，那必须是 0
        # 位数为 2，那必须是 25、50、75
        # 位数大于等于 3，必须以 00、25、50、75 结尾
        n = len(num)
        exist0 = exist5 = False  # 标记是否已经遍历到 0 或 5
        for i in range(n - 1, -1, -1):  # 从右到左遍历
            if num[i] in ['0', '5']:
                if exist0:  # 在这之前也遇到了 0，凑出 00 结尾
                    return n - i - 2
                if num[i] == '0':  # 在这之前没有遇到 0，标记一下状态
                    exist0 = True
                else:  # 在这之前没有遇到 5，标记一下状态
                    exist5 = True
            elif num[i] in ['2', '7']:
                if exist5:  # 在这之前遇到了 5，凑出 25 或 75 结尾
                    return n - i - 2

        # 遍历完都没有找到最少操作数，说明 num 不可能变得以 00、25、50、75 结尾
        if exist0:  # 如果遍历中遇到了 0，则只保留 0
            return n - 1
        return n  # 否则将所有数字都删除


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumOperations("10"))  # 1
    print(solution.minimumOperations("2245047"))  # 2
    print(solution.minimumOperations("2908305"))  # 3
