from CodeKit import timer
from CodeKit import builder


@timer
def time_test(args):
    for i in range(args):
        print(str(i))


time_test(999)


@builder
class TestClass(object):
    def __init__(self, name, age, school):
        pass


test_class = TestClass(name="ErickRen", age=19, school="TYUT")
print([attr for attr in dir(test_class) if not attr.startswith('__')])
