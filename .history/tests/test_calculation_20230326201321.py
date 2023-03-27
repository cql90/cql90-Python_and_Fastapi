from app.Calculation Calculation import add

def test_add():
    sum = add(6, 2)
    assert sum == 8
    
test_add()    