from app import Calculation

def test_add():
    assert_equal(Calculation.add(1, 2), 3)