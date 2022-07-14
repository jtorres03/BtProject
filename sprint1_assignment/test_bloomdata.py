"""import method"""
import Bloomdata_jtorres.bloomdata as bd


def test_increment():
    """this is a test function"""

    assert bd.increment(5) == 6 
    assert bd.increment(100) == 101

def test_increment_float():
    """This is also a test function"""

    assert bd.increment(5.5) == 6.5
    