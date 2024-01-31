# -*- coding: utf-8 -*-
# 610. 判断三角形 https://leetcode.cn/problems/triangle-judgement/
import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(lambda x: 'Yes' if max(x) < sum(x) - max(x) else 'No', axis=1)
    return triangle


if __name__ == '__main__':
    data = [[13, 15, 30], [10, 20, 15]]
    triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})
    print(triangle_judgement(triangle))
