# -*- coding: utf-8 -*-
# 2707. 字符串中的额外字符 https://leetcode.cn/problems/extra-characters-in-a-string/
from sys import maxsize
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [maxsize] * (n + 1)
        dp[0] = 0
        hash_dict = dict()
        for word in dictionary:
            hash_dict[word] = hash_dict[word] + 1 if word in hash_dict else 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # 将 s[i] 当作额外字符
            for j in range(i - 1, -1, -1):  # 0 <= j <= i - 1
                if s[j:i] in hash_dict:  # s[j...i-1]
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.minExtraChar('sayhelloworld', ['hello', 'world']))  # 3
    print(obj.minExtraChar('leetscode', ['leet', 'code', 'leetcode']))  # 1
