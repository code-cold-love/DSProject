#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2207. 字符串中最多数目的子序列 https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        # len(pattern) == 2
        x, y = pattern
        cnt_x = 0  # 表示 text 中 pattern[0] 的数量
        prefix = suffix = 0  # prefix 表示只把 x 加在最左边，suffix 表示只把 y 加在最右面
        for c in text:
            # 优先处理 pattern[1]，text 中出现的 pattern[1] 会产生阻断，没法和该元素后面的 pattern[0] 组合
            if c == y:
                # cnt 表示当前 pattern[1] 前面 text 中自有的 pattern[0]，再加上插在最前面的一个 x
                prefix += (cnt_x + 1)

                # 对于 y 加在最后面，每次遇到 pattern[1] 时，出现的 pattern[0] 要被统计进来
                suffix += cnt_x

            # 由于可能存在 x==y 的情况，所以这里不能用 elif
            if c == x:
                cnt_x += 1

        return max(prefix, suffix + cnt_x)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumSubsequenceCount('aabb', 'ab'))  # 6
    print(solution.maximumSubsequenceCount('abdcdbc', 'ac'))  # 4
    print(solution.maximumSubsequenceCount(
        'vnedkpkkyxelxqptfwuzcjhqmwagvrglkeivowvbjdoyydnjrqrqejoyptzoklaxcjxbrrfmpdxckfjzahparhpanwqfjrpbslsyiwbldnpjqishlsuagevjmiyktgofvnyncizswldwnngnkifmaxbmospdeslxirofgqouaapfgltgqxdhurxljcepdpndqqgfwkfiqrwuwxfamciyweehktaegynfumwnhrgrhcluenpnoieqdivznrjljcotysnlylyswvdlkgsvrotavnkifwmnvgagjykxgwaimavqsxuitknmbxppgzfwtjdvegapcplreokicxcsbdrsyfpustpxxssnouifkypwqrywprjlyddrggkcglbgcrbihgpxxosmejchmzkydhquevpschkpyulqxgduqkqgwnsowxrmgqbmltrltzqmmpjilpfxocflpkwithsjlljxdygfvstvwqsyxlkknmgpppupgjvfgmxnwmvrfuwcrsadomyddazlonjyjdeswwznkaeaasyvurpgyvjsiltiykwquesfjmuswjlrphsdthmuqkrhynmqnfqdlwnwesdmiiqvcpingbcgcsvqmsmskesrajqwmgtdoktreqssutpudfykriqhblntfabspbeddpdkownehqszbmddizdgtqmobirwbopmoqzwydnpqnvkwadajbecmajilzkfwjnpfyamudpppuxhlcngkign',
        'rr'))  # 496
