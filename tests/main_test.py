from xkye import __main__

#To test the positive status
def test_success_main():
    assert __main__.main() == "This is the main routine"


#To test the none status
def test_none_main():
    assert __main__.main('test') == None

