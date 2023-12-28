# -*- coding: utf-8 -*-
# 906. 超级回文数 https://leetcode.cn/problems/super-palindromes/
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        magic = 100000  # 本题中对 right 长度有限制

        def reverse(x: int):  # 将整数 x 反转
            ret = 0
            while x:
                ret = 10 * ret + x % 10
                x //= 10
            return ret

        def is_palindrome(x: int):  # 判断 x 是否为回文数
            return x == reverse(x)

        cnt = 0
        # 统计偶数长度
        for k in range(magic):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > right:
                break
            elif v >= left and is_palindrome(v):
                cnt += 1

        # 统计奇数长度
        for k in range(magic):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > right:
                break
            elif v >= left and is_palindrome(v):
                cnt += 1
        return cnt


if __name__ == '__main__':
    obj = Solution()
    print(obj.superpalindromesInRange('4', '1000'))  # 4
