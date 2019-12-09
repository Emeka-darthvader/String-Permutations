
from String_Engine_API import getErrorStatements

def test_error_functions():
    assert getErrorStatements(1) == "You have entered a wrong format. Kindly retry request using string format"
    #uncomment to test negatives
    #assert getErrorStatements(1) == "Test1","Should be--> You have entered a wrong format. Kindly retry request using string format"
    assert getErrorStatements(2) == "You used a wrong format for the request, kindly use a GET request to the route /permutation-index"
    assert getErrorStatements(3) == "You have gone to the wrong route, kindly visit /permutation-index"
    assert getErrorStatements(4) == "Something went wrong, please contact the administrator"

if __name__ == "__main__":
    test_error_functions()
    print("All tests passed")