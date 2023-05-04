# -*- coding: utf-8 -*-
# 2106. 摘水果 https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], start_pos: int, k: int) -> int:
        left = 0
        right = 0
        n = len(fruits)
        total = 0
        ans = 0

        def step(l: int, r: int) -> int:
            if fruits[r][0] <= start_pos:
                return start_pos - fruits[l][0]
            elif fruits[l][0] >= start_pos:
                return fruits[r][0] - start_pos
            else:
                return min(abs(start_pos - fruits[r][0]), abs(start_pos - fruits[l][0])) + fruits[r][0] - fruits[l][0]

        while right < n:  # 每次固定住窗口右边界
            total += fruits[right][1]
            while left <= right and step(left, right) > k:  # 移动左边界
                total -= fruits[left][1]
                left += 1
            ans = max(ans, total)
            right += 1

        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxTotalFruits([[2, 8], [6, 3], [8, 6]], 5, 4))  # 9
