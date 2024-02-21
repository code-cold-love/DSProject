#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 443. 压缩字符串 https://leetcode.cn/problems/string-compression/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        window = write = 0
        pre = chars[0]
        for c in chars:
            if c == pre:
                window += 1
            else:  # 当前字符与前一个字符不相等
                chars[write] = pre
                write += 1  # 前一个字符
                if window > 1:
                    temp = str(window)
                    for t in temp:
                        chars[write] = t
                        write += 1
                pre = c  # 更新 pre
                window = 1  # 重新记录 window
        chars[write] = pre
        write += 1  # 最后一个字符
        if window > 1:
            temp = str(window)
            for t in temp:
                chars[write] = t
                write += 1
        chars = chars[:write]
        return write


if __name__ == '__main__':
    obj = Solution()
    print(obj.compress(['a']))  # 1
    print(obj.compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']))  # 6
    print(obj.compress(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']))  # 4
