# -*- coding: utf-8 -*-
# 1419. 数青蛙 https://leetcode.cn/problems/minimum-number-of-frogs-croaking/
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5:
            return -1
        res, frog_num = 0, 0
        cnt = [0] * 4
        mp = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        for c in croakOfFrogs:
            t = mp[c]
            if t == 0:
                cnt[t] += 1
                frog_num += 1
                if frog_num > res:
                    res = frog_num
            else:
                if cnt[t - 1] == 0:
                    return -1
                cnt[t - 1] -= 1
                if t == 4:
                    frog_num -= 1
                else:
                    cnt[t] += 1
        if frog_num > 0:
            return -1
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.minNumberOfFrogs('croakcroak'))  # 1
    print(obj.minNumberOfFrogs('crcoakroak'))  # 2
    print(obj.minNumberOfFrogs('croakcrook'))  # -1
