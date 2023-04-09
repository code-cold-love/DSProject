# -*- coding: utf-8 -*-
# 344. 反转字符串 https://leetcode.cn/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # return s.reverse()
        n = len(s)
        if n == 1:
            ...
        else:
            left, right = 0, n - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1


if __name__ == '__main__':
    obj = Solution()
    l = ['a', '', 'b', 'a']
    obj.reverseString(l)
    print(l)
