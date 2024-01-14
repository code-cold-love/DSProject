# -*- coding: utf-8 -*-
# 2696. 删除子串后的字符串最小长度 https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/
class Solution:
    def minLength(self, s: str) -> int:
        n, stack = 0, []
        for c in s:
            n += 1
            stack.append(c)
            if n >= 2 and ((stack[-2] == 'A' and stack[-1] == 'B') or (stack[-2] == 'C' and stack[-1] == 'D')):
                n -= 2
                stack.pop()
                stack.pop()
        return len(stack)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minLength('ABFCACDB'))  # 2
