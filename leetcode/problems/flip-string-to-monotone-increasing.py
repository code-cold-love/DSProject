# -*- coding: utf-8 -*-
# 926. 将字符串翻转到单调递增 https://leetcode.cn/problems/flip-string-to-monotone-increasing/
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 动态规划
        n = len(s)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = s[0] == '1'  # dp[i][0] 表示 s[i] 为 0 时的最小翻转次数
        dp[0][1] = s[0] == '0'  # dp[i][1] 表示 s[i] 为 1 时的最小反转次数
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + (s[i] == '1')
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + (s[i] == '0')
        return min(dp[-1][0], dp[-1][1])

    def minFlipsMonoIncr_opt(self, s: str) -> int:
        # # 动态规划-空间优化
        dp_0 = dp_1 = 0
        for c in s:
            new_dp_0, new_dp_1 = dp_0, min(dp_0, dp_1)
            if c == '1':
                new_dp_0 += 1
            else:
                new_dp_1 += 1
            dp_0, dp_1 = new_dp_0, new_dp_1
        return min(dp_0, dp_1)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minFlipsMonoIncr('00110'))  # 1
    print(obj.minFlipsMonoIncr('010110'))  # 2
    print(obj.minFlipsMonoIncr('00011000'))  # 2
    print(obj.minFlipsMonoIncr('0101100011'))  # 3
