# -*- coding: utf-8 -*-
# 1147. 段式回文 https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/
class Solution:
    def longestDecomposition(self, text: str) -> int:
        i, j = 0, len(text) - 1
        count = 0
        left, right = '', ''
        while i <= j:
            left += text[i]
            right = text[j] + right
            if i == j:
                break
            else:
                if left == right:
                    left = ''
                    right = ''
                    count += 2
            i += 1
            j -= 1
        if left != '' and right != '':  # 奇数个，中间剩余一个无配对的
            count += 1
        return count


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestDecomposition('ghiabcdefhelloadamhelloabcdefghi'))  # 7
