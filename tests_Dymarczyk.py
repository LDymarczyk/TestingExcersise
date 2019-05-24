from TestingExcercise import *

##Tests with square function##

TestInstance = ToBeTested(10, mathFunction = square)
for i in range(-5, 6, 1):
    try: 
        assert TestInstance.thisDoesSomethingImportant(i) == pow(i, 2)
    except AssertionError:
        print "Square function doesn't work properly"

assert TestInstance.thisDoesSomethingImportant(3.0) == pow(3, 2)
assert TestInstance.thisDoesSomethingImportant(3.123445) == pow(3.123445, 2)

##Tests with randomMultiplicator function##

TestInstance = ToBeTested(10)

test_data = [None, 0, "a", 1.1, 500]

for data in test_data:
    try:
        TestInstance.thisNeedsToBeTested(data)
    except:
        print "didin't get parameter"

assert [TestInstance.thisNeedsToBeTested(i) for i in range(-5, 6, 1)] == range(-50, 60, 10)

try:
    TestInstance.thisDoesSomethingImportant(3.123445)
except ImportError:
    print("used bad module")
