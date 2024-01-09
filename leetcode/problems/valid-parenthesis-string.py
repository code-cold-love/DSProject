# -*- coding: utf-8 -*-
# 678. 有效的括号字符串 https://leetcode.cn/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        # 贪心
        left_min = left_max = 0  # 未匹配的左括号数量的最大值和最小值
        for c in s:
            if c == '(':  # 遇到左括号，最大值和最小值分别加 1
                left_min += 1
                left_max += 1
            elif c == ')':  # 遇到右括号，最大值和最小值分别减 1
                left_min = max(left_min - 1, 0)  # 当未匹配的左括号最小值为 0 时，不应将最小值继续减少
                left_max -= 1
                if left_max < 0:  # 当未匹配的左括号最大值变成负数时，说明没有左括号可以和右括号匹配
                    return False
            elif c == '*':  # 星号可以看成左括号、右括号、空字符串
                left_min = max(left_min - 1, 0)  # 当未匹配的左括号最小值为 0 时，不应将最小值继续减少
                left_max += 1
        return left_min == 0  # 遍历结束时，所有的左括号都应和右括号匹配


if __name__ == '__main__':
    obj = Solution()
    print(obj.checkValidString('()'))  # True
    print(obj.checkValidString('(*)'))  # True
