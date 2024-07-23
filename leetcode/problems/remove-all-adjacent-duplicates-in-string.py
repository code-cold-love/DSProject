#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1047. 删除字符串中的所有相邻重复项 https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        stk = []
        for c in s:
            if stk and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates("abbaca"))  # "ca"
