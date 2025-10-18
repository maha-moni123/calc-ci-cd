from calc_app.core import sqrt, power, sin, cos, tan
import math, pytest

def test_sqrt():
    assert sqrt(9) == pytest.approx(3.0)
    with pytest.raises(ValueError):
        sqrt(-1)

def test_power():
    assert power(2, 3) == pytest.approx(8.0)

def test_trig():
    assert sin(math.pi/2) == pytest.approx(1.0)
    assert cos(0) == pytest.approx(1.0)
    assert tan(0) == pytest.approx(0.0)
