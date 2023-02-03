from CodeKit import timer
from CodeKit import builder
from CodeKit.to_string import to_string


@timer
def time_test(args):
    for i in range(args):
        print(str(i))


time_test(999)


@builder
@to_string
class TestClass(object):
    def __init__(self, name, age, school):
        pass


test_class = TestClass(name="ErickRen", age=19, school="TYUT")
print([attr for attr in dir(test_class) if not attr.startswith('__')])
print(test_class)
