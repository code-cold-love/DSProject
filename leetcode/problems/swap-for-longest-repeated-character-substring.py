# -*- coding: utf-8 -*-
# 1156. 单字符重复子串的最大长度 https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/
from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n, ans, counter = len(text), 0, Counter(text)
        i = 0
        while i < n:
            j = i  # 每一次将指针 j 指向 i
            while j < n and text[j] == text[i]:
                j += 1  # 不断向右移动 j，直到 j 指向的字符与 i 指向的字符不同
            left = j - i  # text[i ... j-1] 中所有字符都相同
            k = j + 1  # 跳过 j 指向的字符
            while k < n and text[k] == text[i]:
                k += 1  # 用指针 k 继续向右移动，直到 k 指向的字符与 i 指向的字符不同
            right = k - j - 1  # text[j+1 ... k-1] 中所有字符都相同
            ans = max(ans, min(left + right + 1, counter[text[i]]))
            i = j  # 将指针 i 移动到 j 继续寻找下一个子串
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxRepOpt1('ababa'))  # 3
    print(obj.maxRepOpt1('aaabaaa'))  # 6
    print(obj.maxRepOpt1('abcedfg'))  # 1
    print(obj.maxRepOpt1('aaabbaaa'))  # 4
