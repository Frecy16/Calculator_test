import pytest


@pytest.fixture(scope='function', autouse=True)
def before_test():
    print("开始计算")
    yield
    print("计算结束")