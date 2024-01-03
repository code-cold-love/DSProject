# -*- coding: utf-8 -*-
# 466. 统计重复个数 https://leetcode.cn/problems/count-the-repetitions/
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # 第 i 个 s1 中 s1[j] -> str1[idx1]
        # idx1 = i * len(s1) + j
        # j = idx1 - i * len(s1) = idx1 % len(s1)
        len_s1 = len(s1)
        len_s2 = len(s2)
        j = cnt = 0
        for idx1 in range(n1 * len_s1):
            i = idx1 % len_s1
            if s1[i] == s2[j]:
                j += 1
            if j == len_s2:
                cnt += 1
                j = 0
        return cnt // n2


if __name__ == '__main__':
    obj = Solution()
    print(obj.getMaxRepetitions('acb', 4, 'ab', 2))  # 2
    print(obj.getMaxRepetitions('acb', 1, 'acb', 1))  # 1
