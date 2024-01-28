# -*- coding: utf-8 -*-
# 184. 部门工资最高的员工 https://leetcode.cn/problems/department-highest-salary/
import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 合并表以及重命名
    df = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)

    # 选择工资等于部门最高工资的员工
    max_salary = df.groupby('Department')['Salary'].transform('max')
    df = df[df['Salary'] == max_salary]

    return df[['Department', 'Employee', 'Salary']]


if __name__ == '__main__':
    data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2],
            [5, 'Max', 90000, 1]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})

    data = [[1, 'IT'], [2, 'Sales']]
    department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    print(department_highest_salary(employee, department))
