#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
# 测试文件
# 测试计算器功能
import pytest
import yaml
from pythonCode.calc import Calculator


class TestCalc:
    calc = Calculator()

    def test_add(self, a, b):
        r = self.calc.add(a, b)
        print(a, "+", b, "+", r)
        assert r == a + b

    # @pytest.mark.run(order=1)
    # @pytest.mark.dependency(depands=['test_add'])
    @pytest.mark.parametrize('a, b',
                             yaml.safe_load(open("./data2.yaml"))["add_sub_mul"])
    def test_sub(self, a, b):
        r = self.calc.sub(a, b)
        print(a, "-", b, "=", r)
        assert r == a - b

    @pytest.mark.parametrize('a, b',
                             yaml.safe_load(open("./data2.yaml"))["add_sub_mul"])
    def test_multi(self, a, b):
        r = self.calc.multi(a, b)
        print(a, "*", b, "=", r)
        assert r == a * b

    @pytest.mark.parametrize('a, b', yaml.safe_load(open("./data2.yaml"))["div"])
    def test_div(self, a, b):
        try:
            r = self.calc.div(a, b)
            print(a, "/", b, "=", r)
            assert r == a / b
        except Exception as e:
            print("ERROR")
            return e
