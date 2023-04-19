# -*- coding: utf-8 -*-
# 443. 压缩字符串 https://leetcode.cn/problems/string-compression/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        start = write = 0  # write 写入位置
        while start < n:
            end = start
            while end < n and chars[end] == chars[start]:
                end += 1
            chars[write] = chars[start]
            write += 1
            if end - start > 1:
                for c in str(end - start):
                    chars[write] = c
                    write += 1
            start = end
        return write


if __name__ == '__main__':
    obj = Solution()
    print(obj.compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']))  # 6
