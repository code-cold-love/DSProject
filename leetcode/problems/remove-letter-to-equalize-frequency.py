# -*- coding: utf-8 -*-
# 2423. 删除字符使频率相同 https://leetcode.cn/problems/remove-letter-to-equalize-frequency/
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for c in counter.keys():
            counter[c] -= 1
            if len(set(v for v in counter.values() if v)) == 1:  # 只有一种 value
                return True
            counter[c] += 1
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.equalFrequency('abcc'))  # True
