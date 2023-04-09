# -*- coding: utf-8 -*-
# 557. 反转字符串中的单词 III https://leetcode.cn/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(s.split(' ')[::-1])[::-1]  # 先反转单词列表，再反转字符串
        return ' '.join(s[::-1].split(' ')[::-1])  # 先反转字符串，再反转单词列表
        # return ' '.join(word[::-1] for word in s.split(' '))


if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseWords('LeetCode & GitHub'))
