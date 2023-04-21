# -*- coding: utf-8 -*-
# 1456. 定长子串中元音的最大数目 https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(c):
            return int(c in 'aeiou')

        n = len(s)
        tmp = sum(1 for i in range(k) if is_vowel(s[i]))
        ans = tmp
        for i in range(k, n):
            tmp += is_vowel(s[i]) - is_vowel(s[i - k])
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxVowels('abciiidef', k=3))  # 3
