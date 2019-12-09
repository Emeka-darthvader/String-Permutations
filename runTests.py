
from String_Engine_API import getErrorStatements,createUniqueList,findIndex,sortList

def test_error_functions():
    assert getErrorStatements(1) == "You have entered a wrong format. Kindly retry request using string format"
    #uncomment to test negatives
    #assert getErrorStatements(1) == "Test1","Should be--> You have entered a wrong format. Kindly retry request using string format"
    assert getErrorStatements(2) == "You used a wrong format for the request, kindly use a GET request to the route /permutation-index"
    assert getErrorStatements(3) == "You have gone to the wrong route, kindly visit /permutation-index"
    assert getErrorStatements(4) == "Something went wrong, please contact the administrator"

def test_createUniqueList():
    assert createUniqueList(['abc','abc','abc']) == ['abc']

def test_findIndex():
    assert findIndex('a',['a','b','c']) == 0
def test_sortList():
    assert sortList(['z','y','x']) == ['x','y','z']

if __name__ == "__main__":
    test_error_functions()
    test_createUniqueList()
    test_findIndex()
    test_sortList
    print("All tests passed")