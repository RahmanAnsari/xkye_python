from xkye import *
import pytest

#To test the missing file
def test_read_missing_file():
    xkyFile = "/home/rahi/Desktop/lang/xkye_python/test/test.xky"
    with pytest.raises(Exception):
        m = io(xkyFile)
        assert m.read() == None


#To test the read operation
def test_read_file():
    xkyFile = "/home/rahi/Desktop/lang/xkye_python/tests/test.xky"

    xkye = io(xkyFile)
    dictionary = xkye.read()
    assert dictionary != {}


