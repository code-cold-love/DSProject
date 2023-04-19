# -*- coding: utf-8 -*-
# 1768. 交替合并字符串 https://leetcode.cn/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        ans = ''
        for i in range(min(n1, n2)):
            ans += word1[i] + word2[i]
        return ans + word1[n2:] if n1 > n2 else ans + word2[n1:]


if __name__ == '__main__':
    obj = Solution()
    print(obj.mergeAlternately('abc', 'pqr'))  # apbqcr
