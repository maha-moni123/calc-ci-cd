from calc_app.core import two_plus_two, add, sub, mul, div
import pytest

def test_two_plus_two():
    assert two_plus_two() == "2+2=4"
def test_add():  assert add(2,3)==5
def test_sub():  assert sub(5,2)==3
def test_mul():  assert mul(4,3)==12
def test_div():  assert div(8,2)==4
def test_div_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        div(1,0)
