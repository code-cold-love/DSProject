#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2390. 从字符串中移除星号 https://leetcode.cn/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c == '*':
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)


if __name__ == '__main__':
    obj = Solution()
    print(obj.removeStars('leet**cod*e'))  # lecoe
    print(obj.removeStars('erase*****'))
