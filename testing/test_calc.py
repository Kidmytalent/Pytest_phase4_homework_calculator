# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: test_calc.py
import allure
import pytest

@allure.feature("测试计算器")  # 标记测试场景
class TestCalc:

    @pytest.mark.run(order=1) # 执行加法计算顺序为第一个
    @allure.story("测试加法")   # 标记测试功能
    @pytest.mark.add    # 给每个方法加上标签
    def test_add(self, get_calc, get_add_datas):
        with allure.step("计算两个数的相加和"):   # 将result 添加至 allure.step 步骤中
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
        if isinstance(result, float):  # 判断 result 是否浮点数，作出保留2位小数点处理
            result = round(result, 2)
        assert result == get_add_datas[2] # 断言得到的结果

    # 除法
    @pytest.mark.run(order=4) # 执行除法计算顺序为第四个
    @allure.story("测试除法")
    @pytest.mark.div
    def test_div(self, get_calc, get_div_datas):
        with allure.step("计算两个数相除"):
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_datas[2]

    # 减法
    @pytest.mark.second  # 执行减法计算顺序为第二个
    @allure.story("测试减法")
    @pytest.mark.sub
    def test_sub(self, get_calc, get_sub_datas):
        with allure.step("计算两个数相减"):
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_datas[2]

    # 乘法
    @pytest.mark.run(order=3)  # 执行乘法计算顺序为第三个
    @allure.story("测试乘法")
    @pytest.mark.mul
    def test_mul(self, get_calc, get_mul_datas):
        with allure.step("计算两个数相乘"):
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_datas[2]



