#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 239. 滑动窗口最大值 https://leetcode.cn/problems/sliding-window-maximum/
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 每次滑动窗口只向右移动一位，1 <= k <= nums.length <= 10**5
        ans = []
        if not nums or k == 0:
            return ans
        dq = deque()  # 仅包含窗口内的元素，且非严格递减，构造单调队列

        for i in range(k):  # 未形成窗口时
            while dq and dq[-1] < nums[i]:  # 保持 dq 递减
                dq.pop()
            dq.append(nums[i])
        ans.append(dq[0])  # dq 非严格递减，最大值在队首

        for j in range(k, len(nums)):  # 形成窗口后
            if dq[0] == nums[j - k]:  # 最大值移出窗口
                dq.popleft()
            while dq and dq[-1] < nums[j]:  # 保持 dq 递减
                dq.pop()
            dq.append(nums[j])
            ans.append(dq[0])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1], 1))  # [1]
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
