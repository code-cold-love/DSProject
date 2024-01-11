# -*- coding: utf-8 -*-
# 2645. 构造有效字符串的最少插入数 https://leetcode.cn/problems/minimum-additions-to-make-valid-string/
class Solution:
    def addMinimum(self, word: str) -> int:
        n, ans = len(word), 0
        base = 'abc'
        i = j = 0  # 双指针
        while j < n:
            if word[j] != base[i]:
                ans += 1
            else:
                j += 1
            i = (i + 1) % 3
        return ans + ord('c') - ord(word[-1])  # 判断最后一个字符


if __name__ == '__main__':
    obj = Solution()
    print(obj.addMinimum('b'))  # 2
    print(obj.addMinimum('aaa'))  # 6
    print(obj.addMinimum('abc'))  # 0
