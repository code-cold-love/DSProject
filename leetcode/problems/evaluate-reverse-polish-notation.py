#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 150. 逆波兰表达式求值 https://leetcode.cn/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        evals = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in evals:
                stk.append(int(token))
            else:
                right = stk.pop()
                left = stk.pop()
                if token == '/':
                    stk.append(int(left / right))  # python 中负数除法的表现与题目不一致
                else:
                    stk.append(eval('{}{}{}'.format(left, token, right)))
        return stk[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.evalRPN(['2', '1', '+', '3', '*']))  # 9
    print(solution.evalRPN(['4', '13', '5', '/', '+']))  # 6
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
