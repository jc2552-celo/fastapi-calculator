from app import operations

def test_add():
    assert operations.add(2, 3) == 5

def test_subtract():
    assert operations.subtract(5, 3) == 2

def test_multiply():
    assert operations.multiply(4, 2) == 8

def test_divide():
    assert operations.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        operations.divide(5, 0)
        assert False  # Should never reach here
    except ValueError:
        assert True
