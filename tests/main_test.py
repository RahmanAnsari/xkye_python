from xkye import *
import pytest
import os

#To test the missing file
def test_read_missing_file():
    xkyFile = "../test/test.xky"
    with pytest.raises(Exception):
        m = io(xkyFile)
        assert m.read() == None


#To test the read operation
def test_read_file():
    xkyFile = "test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    dictionary = xkye.read()
    assert dictionary != {}


