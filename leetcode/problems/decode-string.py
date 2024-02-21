#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 394. 字符串解码 https://leetcode.cn/problems/decode-string/
class Solution:
    def decodeString_stack(self, s: str) -> str:
        """辅助栈"""
        stk, res, multi = [], '', 0
        for c in s:
            if c == '[':
                stk.append([multi, res])
                res, multi = '', 0
            elif c == ']':
                cur_multi, last_res = stk.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.decodeString_stack('3[a]2[bc]'))  # aaabcbc
