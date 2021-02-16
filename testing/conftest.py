# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: conftest.py
import pytest
from pytest_cal.cal import Calculator
import yaml

with open("./datas/calc.yaml") as f:  # 获取 yaml 文件中相应方法的数值

    data = yaml.safe_load(f)
    add_values = data['add_value']
    add_id = data['add_id']

    div_values = data['div_value']
    div_id = data['div_id']

    sub_values = data['sub_value']
    sub_id = data['sub_id']

    mul_values = data['mul_value']
    mul_id = data['mul_id']

# 定义 获取数据的方法（通过request.param）
@pytest.fixture(scope='class')  # 设置为模块级别
def get_calc():
    print("计算开始")  # 执行测试用例前打印"计算开始"
    calc = Calculator()
    yield calc
    print("结束计算")  # 执行测试用例后打印"结束计算"


@pytest.fixture(params=add_values, ids=add_id)
def get_add_datas(request):
    print("这里进行加法计算")
    data = request.param  # 用 data 接收获取的数据
    print(f"测试数据为: {data}")
    yield data  # 返回列表数据值

@pytest.fixture(params=div_values, ids=div_id)
def get_div_datas(request):
    print("这里进行除法计算")
    data = request.param
    print(f"测试数据为: {data}")
    yield data

@pytest.fixture(params=sub_values, ids=sub_id)
def get_sub_datas(request):
    print("这里进行减法计算")
    data = request.param
    print(f"测试数据为: {data}")
    yield data


@pytest.fixture(params=mul_values, ids=mul_id)
def get_mul_datas(request):
    print("这里进行乘法计算")
    data = request.param
    print(f"测试数据为: {data}")
    yield data



