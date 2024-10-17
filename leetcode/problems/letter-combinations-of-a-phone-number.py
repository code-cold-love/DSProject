#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 17. 电话号码的字母组合 https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def __init__(self):
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def combination(self, digits: str, idx: int, s: str, ans: list) -> None:
        # 终止条件
        if idx == len(digits):
            ans.append(s)
            return

        digit = int(digits[idx])  # idx 指向的数字
        letters = self.mapping[digit]  # 取数字对应的字符串
        for letter in letters:
            # 下面一行递归代码隐含处理和回溯
            self.combination(digits, idx + 1, s + letter, ans)

    def letterCombinations(self, digits: str) -> List[str]:
        # 0<= len(digits) <= 4, digits[i] 是范围 ["2", "9"] 的一个数字
        ans = []
        if not digits:
            return ans
        self.combination(digits, 0, "", ans)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(solution.letterCombinations(""))  # []
    print(solution.letterCombinations("2"))  # ["a", "b", "c"]
