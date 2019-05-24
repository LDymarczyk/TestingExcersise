#python 2.7.12

####ToBeTested.py

def square(x):
    return x*x
def randomMultiplicator(x):
    from rand import randint
    return x*randint(0,100)
class ToBeTested:
    class TestMeException(Exception):
        pass
    def __init__(self, held_value, mathFunction = randomMultiplicator):
        self.held_value = held_value
        self.__mathFunction = mathFunction
    def thisNeedsToBeTested(self, some_value = None):
        if some_value is not None:
            return self.held_value * some_value
        else:
            raise ToBeTested.TestMeException(self.held_value)
            
    def thisDoesSomethingImportant(self, some_value):
        return self.__mathFunction(some_value)
