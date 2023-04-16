# -*- coding: utf-8 -*-
# 70. 爬楼梯 https://leetcode.cn/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 <= n <= 45
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2  # dp[2] = max(dp[0] + 2, dp[1] + 1)
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs_optimize(self, n: int) -> int:
        """动态规划优化"""
        p, q, r = 0, 0, 1
        if n < 1:
            return 0
        for i in range(1, n + 1):
            p = q
            q = r
            r = p + q
        return r


if __name__ == '__main__':
    obj = Solution()
    print(obj.climbStairs(2))  # 2
    print(obj.climbStairs(4))  # 5
    print(obj.climbStairs_optimize(4))  # 5
