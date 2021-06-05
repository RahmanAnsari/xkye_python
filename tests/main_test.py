from xkye import *
import pytest
import os

#To test the missing file
def test_missing_input_file():
    xkyFile = "../test/test.xky"
    with pytest.raises(Exception):
        m = io(xkyFile)
        assert m.read() == None


#To test the read operation
def test_input_file_success():
    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    dictionary = xkye.read()
    assert dictionary == True


#To test the read operation failure
def test_input_file_failure_1():
    xkyFile = "in/read_test1.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    with pytest.raises(Exception):
        xkye = io(xkyFile)
        dictionary = xkye.read()
        assert dcitionary == None


#To test the read operation failure
def test_input_file_failure_2():
    xkyFile = "in/read_test2.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    with pytest.raises(Exception):
        xkye = io(xkyFile)
        dictionary = xkye.read()
        assert dcitionary == None


#To test the read operation failure
def test_input_file_failure_3():
    xkyFile = "in/read_test3.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    with pytest.raises(Exception):
        xkye = io(xkyFile)
        dictionary = xkye.read()
        assert dcitionary == None


#To test the read operation failure
def test_input_file_failure_4():
    xkyFile = "in/read_test4.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    with pytest.raises(Exception):
        xkye = io(xkyFile)
        dictionary = xkye.read()
        assert dcitionary == None


#To test the outputs1
def test_get_1_method_success():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    valued = xkye.get("key1")

    assert valued == "value"


#To test the outputs1
def test_get_1_method_failure_1():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("net")
        assert valued == None


#To test the outputs2
def test_get_2_method_success():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    valued = xkye.get("shardip","shard")

    assert str(valued) == "127.0.0.1"


#To test the outputs2
def test_get_2_method_failure_1():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("net","shard")
        assert valued == None


#To test the outputs2
def test_get_2_method_failure_2():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("net","net")
        assert valued == None



#To test the outputs3
def test_get_3_method_success():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    valued = xkye.get("shardsubnet","shard", 3)

    assert str(valued) == "192.168.0.0/24"


#To test the outputs3
def test_get_3_method_success_2():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    valued = xkye.get("shardip","shard", 3)

    assert str(valued) == "127.0.0.1"


#To test the outputs3
def test_get_3_method_failure_1():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("shardip","shard", 6)
        assert valued == None


#To test the outputs3
def test_get_3_method_failure_2():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("shardip","net",3)
        assert valued == None

#To test the outputs3
def test_get_3_method_failure_3():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("net","net",3)
        assert valued == None


#To test the outputs3
def test_get_3_method_failure_4():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("net","shard",6)
        assert valued == None


#To test the outputs3
def test_get_3_method_failure_5():

    xkyFile = "in/test.xky"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    xkyFile = dir_path+"/"+xkyFile

    xkye = io(xkyFile)
    xkye.read()

    with pytest.raises(Exception):
        valued = xkye.get("net","shard",3)
        assert valued == None


