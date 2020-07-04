import pytest
#组合参数
@pytest.mark.parametrize("x",{1,2})
@pytest.mark.parametrize("y",{1,2,3})
def test_foo(x,y):
    print(f"x:{x},y:{y}")
