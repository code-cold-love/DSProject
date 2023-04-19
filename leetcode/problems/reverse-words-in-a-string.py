# -*- coding: utf-8 -*-
# 151. 反转字符串中的单词 https://leetcode.cn/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        return ' '.join([c for c in s if c][::-1])


if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseWords('a good   example'))  # example good a
    print(obj.reverseWords('the sky is blue'))  # blue is sky the
