#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1054. 距离相等的条形码 https://leetcode.cn/problems/distant-barcodes/
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n, counter = 0, {}
        max_count = 0
        for barcode in barcodes:
            n += 1
            counter[barcode] = counter.get(barcode, 0) + 1
            max_count = max(max_count, counter[barcode])
        even, odd = 0, 1
        half = n // 2
        for x, count in counter.items():
            while 0 < count <= half and odd < n:  # 元素出现次数超过数组长度的一半，必须放在偶数下标
                barcodes[odd] = x
                count -= 1
                odd += 2
            while count > 0:
                barcodes[even] = x
                count -= 1
                even += 2
        return barcodes


if __name__ == '__main__':
    obj = Solution()
    print(obj.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
