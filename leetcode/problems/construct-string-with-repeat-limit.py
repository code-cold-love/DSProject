# -*- coding: utf-8 -*-
# 2182. 构造限制重复的字符串 https://leetcode.cn/problems/construct-string-with-repeat-limit/
class Solution:
    def repeatLimitedString(self, s: str, repeat_limit: int) -> str:
        count = [0] * 26  # 26 个英文字母出现次数
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans = []
        i, j, freq = 26 - 1, 26 - 2, 0  # i 指向字典序最大的字符，j 指向字典序次最大的字符
        while i >= 0 and j >= 0:
            if count[i] == 0:  # 当前字符已经填完
                freq = 0
                i = i - 1
            elif freq < repeat_limit:  # count[i] != 0，当前字符未超过限制
                count[i] -= 1
                ans.append(chr(ord('a') + i))
                freq += 1
            elif j >= i or count[j] == 0:
                j -= 1
            else:  # j < i and count[j] > 0 and count[i] > 0 and freq == repeat_limit
                count[j] -= 1
                ans.append(chr(ord('a') + j))
                freq = 0
        return ''.join(ans)


if __name__ == '__main__':
    obj = Solution()
    print(obj.repeatLimitedString('cczazcc', 3))  # zzcccac
    print(obj.repeatLimitedString('aababab', 2))  # bbabaa
